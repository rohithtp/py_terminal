"""
LLM Client wrapper using LiteLLM.

Provides unified interface for OpenAI, Anthropic, Ollama, and other LLM providers.
Includes retry logic, timeout handling, and error recovery.
"""

import json
import litellm
from typing import Optional, Dict, Any, List
from ai.config import LLM_PROVIDER, LLM_MODEL, LLM_API_KEY, LLM_TIMEOUT, LLM_MAX_RETRIES, LLM_TEMPERATURE


class LLMClient:
    """Unified LLM client with retry logic and error handling."""

    def __init__(
        self,
        provider: str = LLM_PROVIDER,
        model: str = LLM_MODEL,
        api_key: Optional[str] = LLM_API_KEY,
        timeout: int = LLM_TIMEOUT,
        max_retries: int = LLM_MAX_RETRIES,
        temperature: float = LLM_TEMPERATURE,
    ):
        """
        Initialize LLM client.

        Args:
            provider: LLM provider name ("openai", "anthropic", "ollama", etc.)
            model: Model identifier (e.g., "gpt-4", "claude-3-5-sonnet-20241022")
            api_key: API key for the provider (if required)
            timeout: Timeout in seconds for API calls
            max_retries: Maximum number of retries on failure
            temperature: Sampling temperature (0.0-1.0)
        """
        self.provider = provider
        self.model = model
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.temperature = temperature

        # Set API key if provided
        if api_key:
            if "openai" in model.lower():
                litellm.openai_api_key = api_key
            elif "claude" in model.lower() or "anthropic" in provider.lower():
                litellm.anthropic_api_key = api_key

        # Optional: enable verbose logging for debugging
        # litellm.set_verbose = True

    def call(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> str:
        """
        Call the LLM with retry logic and timeout handling.

        Args:
            messages: List of message dicts with 'role' and 'content'
                     Example: [{"role": "user", "content": "Hello"}]
            temperature: Sampling temperature (uses instance default if None)
            max_tokens: Max response tokens (None = use model default)

        Returns:
            str: Model's response content

        Raises:
            Exception: If LLM call fails after max retries
        """
        temp = temperature if temperature is not None else self.temperature
        attempt = 0

        while attempt < self.max_retries:
            try:
                response = litellm.completion(
                    provider=self.provider,
                    model=self.model,
                    messages=messages,
                    temperature=temp,
                    max_tokens=max_tokens,
                    timeout=self.timeout,
                    api_key=self.api_key,
                )
                return response.choices[0].message.content

            except Exception as e:
                attempt += 1
                if attempt >= self.max_retries:
                    print(f"❌ LLM call failed after {self.max_retries} retries: {e}")
                    raise
                print(f"⚠️  Attempt {attempt} failed, retrying... ({str(e)[:50]})")

    def call_json(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        schema: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Call the LLM and parse JSON response.

        Args:
            messages: List of message dicts
            temperature: Sampling temperature (lower is better for JSON)
            schema: Optional JSON schema hint (for documentation)

        Returns:
            Dict: Parsed JSON response

        Raises:
            json.JSONDecodeError: If response is not valid JSON
        """
        temp = temperature if temperature is not None else 0.3  # Lower temp for JSON

        response_text = self.call(messages, temperature=temp)

        try:
            return json.loads(response_text)
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON: {e}")
            print(f"Raw response: {response_text[:200]}...")
            raise

    def stream(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ):
        """
        Stream LLM response (yields tokens as they arrive).

        Args:
            messages: List of message dicts
            temperature: Sampling temperature
            max_tokens: Max response tokens

        Yields:
            str: Response tokens
        """
        temp = temperature if temperature is not None else self.temperature

        try:
            response = litellm.completion(
                provider=self.provider,
                model=self.model,
                messages=messages,
                temperature=temp,
                max_tokens=max_tokens,
                timeout=self.timeout,
                api_key=self.api_key,
                stream=True,
            )

            for chunk in response:
                token = chunk.choices[0].delta.content
                if token:
                    yield token

        except Exception as e:
            print(f"❌ LLM stream failed: {e}")
            raise

    def health_check(self) -> bool:
        """
        Quick health check by making a minimal API call.

        Returns:
            bool: True if LLM is accessible, False otherwise
        """
        try:
            _ = self.call(
                [{"role": "user", "content": "ping"}],
                max_tokens=5,
            )
            return True
        except Exception:
            return False


# === Global Client Instance ===

_client: Optional[LLMClient] = None


def get_client() -> LLMClient:
    """
    Get or create the global LLM client instance.

    Returns:
        LLMClient: Singleton client instance
    """
    global _client
    if _client is None:
        _client = LLMClient()
    return _client


def reset_client():
    """Reset the global client instance (useful for testing)."""
    global _client
    _client = None


def set_client(client: LLMClient):
    """
    Set a custom client instance.

    Args:
        client: LLMClient instance to use
    """
    global _client
    _client = client
