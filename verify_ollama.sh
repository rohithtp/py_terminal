#!/usr/bin/env bash

# Verify Ollama installation and wire environment variables for this shell.
# Usage:
#   source ./verify_ollama.sh
# or:
#   ./verify_ollama.sh

set -eu

print_header() {
  echo
  echo "========================================"
  echo " $1"
  echo "========================================"
}

verify_ollama_cli() {
  print_header "Ollama CLI Verification"

  if ! command -v ollama >/dev/null 2>&1; then
    echo "❌ Ollama CLI not found on PATH."
    echo "   Install Ollama from https://ollama.ai/ and make sure 'ollama' is available in your shell."
    return 1
  fi

  if ! ollama --version >/dev/null 2>&1; then
    echo "❌ Ollama CLI is installed but failed to execute."
    echo "   Try running: ollama --version"
    return 1
  fi

  echo "✅ Ollama CLI found and executable."
  return 0
}

verify_ollama_server() {
  print_header "Ollama Server Verification"

  if ollama ls >/dev/null 2>&1; then
    echo "✅ Ollama server appears to be running."
    return 0
  fi

  echo "⚠️  Ollama server does not appear to be running."
  echo "   Start it in another terminal with:"
  echo "     ollama serve > ollama.log 2>&1 &"
  return 1
}

wire_environment() {
  export LLM_PROVIDER="ollama"
  export LLM_MODEL="${LLM_MODEL:-qwen2.5-coder:1.5b}"

  print_header "Environment Wiring"
  echo "✅ Set LLM_PROVIDER=ollama"
  echo "✅ Set LLM_MODEL=${LLM_MODEL}"
  echo
  echo "To keep these settings for later, add them to your shell profile or source this script:" 
  echo "  source ./verify_ollama.sh"
}

main() {
  local cli_ok=0
  local server_ok=0

  if verify_ollama_cli; then
    cli_ok=1
  fi

  if verify_ollama_server; then
    server_ok=1
  fi

  if [[ ${cli_ok} -eq 1 && ${server_ok} -eq 1 ]]; then
    echo
    echo "✅ Ollama is installed and available."
  else
    echo
    echo "⚠️  Some Ollama checks did not pass. Fix the issues above and rerun this script."
  fi
}


# Run checks
main "$@"

# If the script is being sourced, export environment variables into the
# current shell. If it's executed directly, print instructions instead.
is_sourced=0
if [[ -n "${ZSH_VERSION:-}" ]]; then
  if [[ "${ZSH_EVAL_CONTEXT:-}" == *"file"* ]]; then
    is_sourced=1
  fi
elif [[ -n "${BASH_VERSION:-}" ]]; then
  if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    is_sourced=1
  fi
fi

if [[ ${is_sourced} -eq 1 ]]; then
  wire_environment
else
  echo
  echo "Run 'source ./verify_ollama.sh' to export Ollama environment variables into your current shell."
  exit 0
fi
