#!/usr/bin/env bash

# Start Ollama in the background and capture logs, then run a model after a short delay.
set -eu

# Start the server manually in the background.
ollama serve > ollama.log 2>&1 &
server_pid=$!

echo "Started ollama serve with PID ${server_pid}. Logs are in ollama.log."

echo "Waiting 3 seconds for Ollama to boot..."
sleep 3

echo "Running model qwen2.5-coder:1.5b..."
ollama run qwen2.5-coder:1.5b
