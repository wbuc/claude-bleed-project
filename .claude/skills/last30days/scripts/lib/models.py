"""Model auto-selection for last30days skill.

Only handles xAI model selection. Reddit search uses Brave Search API (no model needed).
"""

from typing import Dict, List, Optional

from . import cache, http

# xAI API - Agent Tools API requires grok-4 family
XAI_MODELS_URL = "https://api.x.ai/v1/models"
XAI_ALIASES = {
    "latest": "grok-4-1-fast",  # Required for x_search tool
    "stable": "grok-4-1-fast",
}


def select_xai_model(
    api_key: str,
    policy: str = "latest",
    pin: Optional[str] = None,
    mock_models: Optional[List[Dict]] = None,
) -> str:
    """Select the best xAI model based on policy.

    Args:
        api_key: xAI API key
        policy: 'latest', 'stable', or 'pinned'
        pin: Model to use if policy is 'pinned'
        mock_models: Mock model list for testing

    Returns:
        Selected model ID
    """
    if policy == "pinned" and pin:
        return pin

    # Use alias system
    if policy in XAI_ALIASES:
        alias = XAI_ALIASES[policy]

        # Check cache first
        cached = cache.get_cached_model("xai")
        if cached:
            return cached

        # Cache the alias
        cache.set_cached_model("xai", alias)
        return alias

    # Default to latest
    return XAI_ALIASES["latest"]


def get_models(
    config: Dict,
    mock_xai_models: Optional[List[Dict]] = None,
) -> Dict[str, Optional[str]]:
    """Get selected models for providers.

    Returns:
        Dict with 'xai' key (Brave Search doesn't need model selection)
    """
    result = {"xai": None}

    if config.get("XAI_API_KEY"):
        result["xai"] = select_xai_model(
            config["XAI_API_KEY"],
            config.get("XAI_MODEL_POLICY", "latest"),
            config.get("XAI_MODEL_PIN"),
            mock_xai_models,
        )

    return result
