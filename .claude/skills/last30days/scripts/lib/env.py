"""Environment and API key management for last30days skill.

Uses Brave Search API for Reddit/web discovery (replaces OpenAI).
Uses xAI API for X/Twitter search.

Keys are loaded from the project .env file (current working directory).
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any


def load_env_file(path: Path) -> Dict[str, str]:
    """Load environment variables from a file."""
    env = {}
    if not path.exists():
        return env

    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, _, value = line.partition('=')
                key = key.strip()
                value = value.strip()
                # Remove quotes if present
                if value and value[0] in ('"', "'") and value[-1] == value[0]:
                    value = value[1:-1]
                if key and value:
                    env[key] = value
    return env


def get_config() -> Dict[str, Any]:
    """Load configuration from project .env and environment.

    Checks (in priority order):
    1. Environment variables
    2. .env in current working directory (project-level keys)
    """
    project_env = load_env_file(Path.cwd() / ".env")

    config = {
        'BRAVE_API_KEY': os.environ.get('BRAVE_API_KEY') or project_env.get('BRAVE_API_KEY'),
        'XAI_API_KEY': os.environ.get('XAI_API_KEY') or project_env.get('XAI_API_KEY'),
        'XAI_MODEL_POLICY': os.environ.get('XAI_MODEL_POLICY') or project_env.get('XAI_MODEL_POLICY', 'latest'),
        'XAI_MODEL_PIN': os.environ.get('XAI_MODEL_PIN') or project_env.get('XAI_MODEL_PIN'),
    }

    return config


def config_exists() -> bool:
    """Check if project .env file exists."""
    return (Path.cwd() / ".env").exists()


def get_available_sources(config: Dict[str, Any]) -> str:
    """Determine which sources are available based on API keys.

    Brave Search API handles Reddit + web discovery.
    xAI API handles X/Twitter search.

    Returns: 'both', 'reddit', 'x', or 'web'
    """
    has_brave = bool(config.get('BRAVE_API_KEY'))
    has_xai = bool(config.get('XAI_API_KEY'))

    if has_brave and has_xai:
        return 'both'
    elif has_brave:
        return 'reddit'  # Reddit via Brave Search
    elif has_xai:
        return 'x'
    else:
        return 'web'  # Fallback: Claude WebSearch only


def get_missing_keys(config: Dict[str, Any]) -> str:
    """Determine which API keys are missing.

    Returns: 'both', 'reddit', 'x', or 'none'
    """
    has_brave = bool(config.get('BRAVE_API_KEY'))
    has_xai = bool(config.get('XAI_API_KEY'))

    if has_brave and has_xai:
        return 'none'
    elif has_brave:
        return 'x'  # Missing xAI key
    elif has_xai:
        return 'reddit'  # Missing Brave key
    else:
        return 'both'  # Missing both keys


def validate_sources(requested: str, available: str, include_web: bool = False) -> tuple[str, Optional[str]]:
    """Validate requested sources against available keys.

    Args:
        requested: 'auto', 'reddit', 'x', 'both', or 'web'
        available: Result from get_available_sources()
        include_web: If True, add WebSearch to available sources

    Returns:
        Tuple of (effective_sources, error_message)
    """
    # No API keys at all
    if available == 'web':
        if requested == 'auto':
            return 'web', None
        elif requested == 'web':
            return 'web', None
        else:
            return 'web', f"No API keys configured. Using WebSearch fallback. Add keys to ~/.config/last30days/.env for Reddit/X."

    if requested == 'auto':
        if include_web:
            if available == 'both':
                return 'all', None
            elif available == 'reddit':
                return 'reddit-web', None
            elif available == 'x':
                return 'x-web', None
        return available, None

    if requested == 'web':
        return 'web', None

    if requested == 'both':
        if available not in ('both',):
            missing = 'xAI' if available == 'reddit' else 'Brave Search'
            return 'none', f"Requested both sources but {missing} key is missing. Use --sources=auto to use available keys."
        if include_web:
            return 'all', None
        return 'both', None

    if requested == 'reddit':
        if available == 'x':
            return 'none', "Requested Reddit but only xAI key is available. Add BRAVE_API_KEY for Reddit."
        if include_web:
            return 'reddit-web', None
        return 'reddit', None

    if requested == 'x':
        if available == 'reddit':
            return 'none', "Requested X but only Brave key is available. Add XAI_API_KEY for X."
        if include_web:
            return 'x-web', None
        return 'x', None

    return requested, None
