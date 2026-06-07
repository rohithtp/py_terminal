#!/usr/bin/env python3
"""
LiteLLM Installation Verification Script

Run this script to verify LiteLLM setup and test the LLM client.
Usage: python3 verify_llm_setup.py
"""

import sys
import os

def print_header(text):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")


def verify_imports():
    """Verify 1: Check if litellm is installed."""
    print_header("Verification 1: Import Check")
    try:
        import litellm
        print(f"✅ LiteLLM imported successfully")
        try:
            print(f"   Version: {litellm.__version__}")
        except AttributeError:
            print(f"   (version info not available)")
        return True
    except ImportError as e:
        print(f"❌ Failed to import litellm: {e}")
        print("   Run: pip install litellm")
        return False


def verify_client_module():
    """Verify 2: Check if client module can be imported."""
    print_header("Verification 2: Client Module Import")
    try:
        from ai.client import LLMClient, get_client
        print(f"✅ Client module imported successfully")
        print(f"   LLMClient: {LLMClient.__name__}")
        return True
    except ImportError as e:
        print(f"❌ Failed to import client module: {e}")
        return False


def verify_config():
    """Verify 3: Check configuration values."""
    print_header("Verification 3: Configuration Check")
    try:
        from ai.config import (
            LLM_PROVIDER, LLM_MODEL, LLM_TIMEOUT,
            LLM_MAX_RETRIES, LLM_API_KEY
        )
        print(f"✅ Configuration loaded successfully:")
        print(f"   Provider: {LLM_PROVIDER}")
        print(f"   Model: {LLM_MODEL}")
        print(f"   Timeout: {LLM_TIMEOUT}s")
        print(f"   Max Retries: {LLM_MAX_RETRIES}")
        print(f"   API Key: {'Set' if LLM_API_KEY else '❌ NOT SET'}")
        
        if not LLM_API_KEY and LLM_PROVIDER != "ollama":
            print(f"\n   ⚠️  Warning: API key not found!")
            print(f"   Set environment variable for your provider:")
            if "openai" in LLM_PROVIDER:
                print(f"   export OPENAI_API_KEY='your-key-here'")
            elif "anthropic" in LLM_PROVIDER:
                print(f"   export ANTHROPIC_API_KEY='your-key-here'")
        
        return True
    except Exception as e:
        print(f"❌ Configuration check failed: {e}")
        return False


def verify_client_init():
    """Verify 4: Test client initialization."""
    print_header("Verification 4: Client Initialization")
    try:
        from ai.client import get_client
        client = get_client()
        print(f"✅ Client initialized successfully:")
        print(f"   Model: {client.model}")
        print(f"   Provider: {client.provider}")
        print(f"   Timeout: {client.timeout}s")
        return True
    except Exception as e:
        print(f"❌ Client initialization failed: {e}")
        return False


def verify_health_check():
    """Verify 5: Perform LLM health check."""
    print_header("Verification 5: LLM Health Check")
    try:
        from ai.client import get_client
        client = get_client()
        
        print(f"Testing connection to {client.model}...")
        is_healthy = client.health_check()
        
        if is_healthy:
            print(f"✅ LLM is accessible and responding")
            return True
        else:
            print(f"❌ LLM health check failed")
            return False
            
    except Exception as e:
        print(f"❌ Health check error: {e}")
        print(f"   Make sure your API key is set or Ollama is running")
        return False


def verify_simple_call():
    """Verify 6: Make a simple API call."""
    print_header("Verification 6: Simple API Call")
    try:
        from ai.client import get_client
        client = get_client()
        
        print(f"Sending test message to {client.model}...")
        response = client.call(
            messages=[{"role": "user", "content": "Say 'Setup complete' in exactly 2 words."}],
            max_tokens=10,
        )
        print(f"✅ Response received:")
        print(f"   {response}")
        return True
        
    except Exception as e:
        print(f"❌ API call failed: {e}")
        return False


def verify_json_call():
    """Verify 7: Test JSON mode."""
    print_header("Verification 7: JSON Mode")
    try:
        from ai.client import get_client
        import json
        
        client = get_client()
        print(f"Sending JSON request to {client.model}...")
        
        response = client.call_json(
            messages=[{
                "role": "user",
                "content": 'Return valid JSON: {"status": "ok", "message": "LiteLLM works", "verified": true}'
            }],
        )
        
        print(f"✅ JSON response parsed successfully:")
        print(f"   {json.dumps(response, indent=4)}")
        return True
        
    except Exception as e:
        print(f"❌ JSON call failed: {e}")
        return False


def main():
    """Run all verification steps."""
    print("\n" + "="*60)
    print("  LiteLLM Setup Verification")
    print("="*60)
    
    results = []
    
    # Run verifications
    results.append(("Import Check", verify_imports()))
    
    if not results[-1][1]:
        print("\n⚠️  LiteLLM not installed. Install with:")
        print("   pip install litellm")
        return 1
    
    results.append(("Client Module Import", verify_client_module()))
    results.append(("Configuration Check", verify_config()))
    results.append(("Client Initialization", verify_client_init()))
    results.append(("LLM Health Check", verify_health_check()))
    
    if results[-1][1]:  # If health check passed, try API calls
        results.append(("Simple API Call", verify_simple_call()))
        results.append(("JSON Mode", verify_json_call()))
    
    # Print summary
    print_header("Verification Summary")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {test_name}")
    
    print(f"\nTotal: {passed}/{total} passed")
    
    if passed == total:
        print("\n🎉 All verifications passed! LiteLLM is ready to use.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} verification(s) failed. See details above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
