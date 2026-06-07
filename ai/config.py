import os
from enum import Enum


class LLMProvider(Enum):
    """Supported LLM providers."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"
    HUGGINGFACE = "huggingface"


# === Primary Configuration ===
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")
LLM_API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")

# === Performance & Retry Settings ===
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", "30"))
LLM_MAX_RETRIES = int(os.getenv("LLM_MAX_RETRIES", "3"))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))

# === Caching ===
ENABLE_CACHE = os.getenv("ENABLE_CACHE", "true").lower() == "true"
CACHE_DIR = os.path.join(
    os.path.dirname(__file__),
    ".cache"
)

# === Model Aliases ===
MODEL_ALIASES = {
    "gpt4": "gpt-4",
    "gpt3": "gpt-3.5-turbo",
    "claude3": "claude-3-5-sonnet-20241022",
    "qwen": "qwen2.5-coder:1.5b",
    "llama2": "ollama/llama2",
}


def validate_config() -> bool:
    """Validate that required configuration is set."""
    if not LLM_API_KEY and LLM_PROVIDER != "ollama":
        print("⚠️  Warning: API key not found. Set OPENAI_API_KEY or ANTHROPIC_API_KEY")
        return False
    return True


def get_model_name(alias: str) -> str:
    """Resolve model alias to full model name."""
    return MODEL_ALIASES.get(alias.lower(), alias)
