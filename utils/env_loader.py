"""
Environment Variable Loader Utility

This module provides a centralized way to load and validate environment variables
for MCP AI Agents and RAG Tutorials.

Usage:
    from utils.env_loader import load_env, get_api_key

    # Load environment variables
    load_env()

    # Get API keys with validation
    openai_key = get_api_key('OPENAI_API_KEY')
"""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


def load_env(env_file: str = ".env", verbose: bool = False) -> bool:
    """
    Load environment variables from .env file.

    Args:
        env_file: Path to the .env file (default: .env in project root)
        verbose: Print loading status

    Returns:
        bool: True if .env file was loaded successfully
    """
    # Try to find .env file in current directory or parent directories
    current_dir = Path.cwd()
    env_path = None

    # Search up to 3 levels up
    for _ in range(3):
        potential_path = current_dir / env_file
        if potential_path.exists():
            env_path = potential_path
            break
        current_dir = current_dir.parent

    if env_path:
        load_dotenv(env_path)
        if verbose:
            print(f"✓ Loaded environment variables from: {env_path}")
        return True
    else:
        if verbose:
            print(f"⚠ No {env_file} file found. Using system environment variables.")
        return False


def get_api_key(
    key_name: str,
    default: Optional[str] = None,
    required: bool = True
) -> Optional[str]:
    """
    Get API key from environment with validation.

    Args:
        key_name: Name of the environment variable
        default: Default value if not found
        required: Raise error if key is missing and required

    Returns:
        str: API key value or None

    Raises:
        ValueError: If required key is missing
    """
    value = os.getenv(key_name, default)

    if required and not value:
        raise ValueError(
            f"❌ {key_name} not found in environment variables.\n"
            f"Please set it in your .env file or environment."
        )

    # Mask the key for display (show first 4 and last 4 characters)
    if value and len(value) > 8:
        masked = f"{value[:4]}...{value[-4:]}"
    else:
        masked = "***" if value else "Not Set"

    return value


def get_model_config(provider: str = "openai") -> dict:
    """
    Get model configuration for a specific provider.

    Args:
        provider: AI provider name (openai, anthropic, google, cohere, etc.)

    Returns:
        dict: Configuration dictionary with api_key and model
    """
    configs = {
        "openai": {
            "api_key": get_api_key("OPENAI_API_KEY", required=False),
            "model": os.getenv("OPENAI_MODEL", "gpt-4o"),
        },
        "anthropic": {
            "api_key": get_api_key("ANTHROPIC_API_KEY", required=False),
            "model": os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022"),
        },
        "google": {
            "api_key": get_api_key("GOOGLE_API_KEY", required=False),
            "model": os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp"),
        },
        "cohere": {
            "api_key": get_api_key("COHERE_API_KEY", required=False),
            "model": os.getenv("COHERE_MODEL", "command-r-plus"),
        },
        "xai": {
            "api_key": get_api_key("XAI_API_KEY", required=False),
            "model": os.getenv("XAI_MODEL", "grok-beta"),
        },
    }

    return configs.get(provider.lower(), {})


def get_service_config(service: str) -> dict:
    """
    Get configuration for external services.

    Args:
        service: Service name (github, notion, serp, tavily, etc.)

    Returns:
        dict: Service configuration
    """
    configs = {
        "github": {
            "token": get_api_key("GITHUB_TOKEN", required=False),
        },
        "notion": {
            "api_key": get_api_key("NOTION_API_KEY", required=False),
            "database_id": os.getenv("NOTION_DATABASE_ID"),
        },
        "serp": {
            "api_key": get_api_key("SERP_API_KEY", required=False),
        },
        "tavily": {
            "api_key": get_api_key("TAVILY_API_KEY", required=False),
        },
        "pinecone": {
            "api_key": get_api_key("PINECONE_API_KEY", required=False),
            "environment": os.getenv("PINECONE_ENVIRONMENT"),
            "index": os.getenv("PINECONE_INDEX"),
        },
        "weaviate": {
            "url": os.getenv("WEAVIATE_URL"),
            "api_key": get_api_key("WEAVIATE_API_KEY", required=False),
        },
    }

    return configs.get(service.lower(), {})


def validate_required_keys(*key_names: str) -> bool:
    """
    Validate that all required environment variables are set.

    Args:
        *key_names: Variable number of environment variable names

    Returns:
        bool: True if all keys are set

    Raises:
        ValueError: If any required key is missing
    """
    missing_keys = []

    for key in key_names:
        if not os.getenv(key):
            missing_keys.append(key)

    if missing_keys:
        raise ValueError(
            f"❌ Missing required environment variables:\n"
            f"{', '.join(missing_keys)}\n"
            f"Please set them in your .env file."
        )

    return True


# Example usage and testing
if __name__ == "__main__":
    # Load environment variables
    load_env(verbose=True)

    # Test API key loading
    try:
        openai_key = get_api_key("OPENAI_API_KEY", required=False)
        if openai_key:
            print(f"✓ OpenAI API Key loaded: {openai_key[:4]}...{openai_key[-4:]}")
        else:
            print("⚠ OpenAI API Key not found")

        # Get model configuration
        openai_config = get_model_config("openai")
        print(f"✓ OpenAI Config: {openai_config.get('model')}")

    except ValueError as e:
        print(e)
