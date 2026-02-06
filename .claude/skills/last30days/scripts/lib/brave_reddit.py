"""Brave Search API client for Reddit discovery.

Replaces openai_reddit.py - uses Brave Search API instead of OpenAI
to find Reddit threads. Output format is identical so the rest of
the pipeline (normalize, score, dedupe, enrich) works unchanged.
"""

import json
import re
import sys
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse, urlencode

from . import http

# Brave Search API
BRAVE_SEARCH_URL = "https://api.search.brave.com/res/v1/web/search"

# Depth configurations: how many results to request from Brave
DEPTH_CONFIG = {
    "quick": 10,
    "default": 20,
    "deep": 50,
}


def _log_error(msg: str):
    """Log error to stderr."""
    sys.stderr.write(f"[REDDIT ERROR] {msg}\n")
    sys.stderr.flush()


def _log_info(msg: str):
    """Log info to stderr."""
    sys.stderr.write(f"[REDDIT] {msg}\n")
    sys.stderr.flush()


def _extract_subreddit(url: str) -> str:
    """Extract subreddit name from a Reddit URL."""
    match = re.search(r'/r/([^/]+)', url)
    return match.group(1) if match else ""


def _is_reddit_thread_url(url: str) -> bool:
    """Check if URL is a Reddit thread (not just a subreddit or user page)."""
    parsed = urlparse(url)
    if "reddit.com" not in parsed.netloc:
        return False
    # Must contain /r/ and /comments/ to be a thread
    path = parsed.path
    return "/r/" in path and "/comments/" in path


def _extract_core_subject(topic: str) -> str:
    """Extract core subject from verbose query for retry."""
    noise = ['best', 'top', 'how to', 'tips for', 'practices', 'features',
             'killer', 'guide', 'tutorial', 'recommendations', 'advice',
             'prompting', 'using', 'for', 'with', 'the', 'of', 'in', 'on']
    words = topic.lower().split()
    result = [w for w in words if w not in noise]
    return ' '.join(result[:3]) or topic


def _parse_brave_date(result: Dict) -> Optional[str]:
    """Extract date from Brave Search result in YYYY-MM-DD format."""
    # Try page_age first (ISO datetime)
    page_age = result.get("page_age")
    if page_age:
        match = re.match(r'(\d{4}-\d{2}-\d{2})', str(page_age))
        if match:
            return match.group(1)

    # Try age field (relative like "2 days ago", "January 15, 2026")
    age = result.get("age")
    if age:
        match = re.match(r'(\d{4}-\d{2}-\d{2})', str(age))
        if match:
            return match.group(1)

    return None


def search_reddit(
    api_key: str,
    topic: str,
    from_date: str,
    to_date: str,
    depth: str = "default",
    mock_response: Optional[Dict] = None,
) -> Dict[str, Any]:
    """Search Reddit for relevant threads using Brave Search API.

    Args:
        api_key: Brave Search API key
        topic: Search topic
        from_date: Start date (YYYY-MM-DD)
        to_date: End date (YYYY-MM-DD)
        depth: Research depth - "quick", "default", or "deep"
        mock_response: Mock response for testing

    Returns:
        Raw Brave API response
    """
    if mock_response is not None:
        return mock_response

    count = DEPTH_CONFIG.get(depth, DEPTH_CONFIG["default"])

    headers = {
        "X-Subscription-Token": api_key,
        "Accept": "application/json",
    }

    # Search Reddit specifically
    query = f"{topic} site:reddit.com"

    params = {
        "q": query,
        "count": min(count, 20),  # Brave API max per request is 20
        "freshness": "pm",  # Past month
        "text_decorations": "false",
    }

    url = f"{BRAVE_SEARCH_URL}?{urlencode(params)}"

    try:
        response = http.get(url, headers=headers, timeout=30)
    except http.HTTPError as e:
        _log_error(f"Brave Search API error: {e}")
        raise

    # If we need more results for deep mode, do additional searches
    if depth == "deep" and count > 20:
        # Do a second query with different phrasing
        core = _extract_core_subject(topic)
        if core.lower() != topic.lower():
            params2 = {
                "q": f"reddit {core}",
                "count": 20,
                "freshness": "pm",
                "text_decorations": "false",
            }
            url2 = f"{BRAVE_SEARCH_URL}?{urlencode(params2)}"
            try:
                response2 = http.get(url2, headers=headers, timeout=30)
                # Merge results
                results1 = response.get("web", {}).get("results", [])
                results2 = response2.get("web", {}).get("results", [])
                seen_urls = {r.get("url") for r in results1}
                for r in results2:
                    if r.get("url") not in seen_urls:
                        results1.append(r)
                if "web" not in response:
                    response["web"] = {}
                response["web"]["results"] = results1
            except http.HTTPError:
                pass  # Use first results only

    return response


def parse_reddit_response(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Parse Brave Search response to extract Reddit items.

    Args:
        response: Raw Brave API response

    Returns:
        List of item dicts in the same format as openai_reddit
    """
    items = []

    web_results = response.get("web", {}).get("results", [])

    if not web_results:
        _log_info("No web results found in Brave Search response")
        return items

    for i, result in enumerate(web_results):
        url = result.get("url", "")

        # Only keep actual Reddit thread URLs
        if not _is_reddit_thread_url(url):
            continue

        # Skip non-standard Reddit domains
        parsed = urlparse(url)
        if any(sub in parsed.netloc for sub in ["developers.reddit.com", "business.reddit.com"]):
            continue

        title = result.get("title", "").strip()
        description = result.get("description", "").strip()
        subreddit = _extract_subreddit(url)
        date = _parse_brave_date(result)

        clean_item = {
            "id": f"R{len(items) + 1}",
            "title": title,
            "url": url,
            "subreddit": subreddit,
            "date": date,
            "why_relevant": description[:200] if description else "Found via Brave Search",
            "relevance": max(0.3, min(1.0, 0.9 - (len(items) * 0.03))),  # Decay by position
        }

        items.append(clean_item)

    return items
