#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/../docs/example-configs/ollama-langsmith.json"
ENV_FILE="$SCRIPT_DIR/../docs/example-configs/ollama-langsmith.env"

GREEN="$(tput setaf 10)"
RED="$(tput setaf 9)"
BLUE="$(tput setaf 12)"
BOLD="$(tput bold)"
RESET="$(tput sgr0)"

ok() { echo -e "${GREEN}✔ $1${RESET}"; }
fail() { echo -e "${RED}✖ $1${RESET}"; exit 1; }
step() { echo -e "${BLUE}${BOLD}➜ $1...${RESET}"; }

step "Checking prerequisites"

command -v codex >/dev/null 2>&1 && ok "codex CLI found" || fail "codex CLI not installed"
command -v ollama >/dev/null 2>&1 && ok "ollama found" || fail "ollama not installed"
command -v curl >/dev/null 2>&1 && ok "curl found" || fail "curl not installed"

[ -f "$CONFIG_FILE" ] && ok "config file located" || fail "config file missing: $CONFIG_FILE"

if curl -fsS http://localhost:11434/ >/dev/null; then
  ok "Ollama server reachable"
else
  fail "Ollama server not reachable on http://localhost:11434"
fi

if [ -f "$ENV_FILE" ]; then
  step "Loading environment from $ENV_FILE"
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
  ok "Environment loaded"
fi

[ -n "${LANGCHAIN_API_KEY:-}" ] || fail "LANGCHAIN_API_KEY not set"
[ -n "${LANGCHAIN_TRACING_V2:-}" ] || fail "LANGCHAIN_TRACING_V2 not set"
[ -n "${LANGCHAIN_ENDPOINT:-}" ] || fail "LANGCHAIN_ENDPOINT not set"
ok "LangSmith variables present"

step "Launching Codex"
cmd=(codex --config "$CONFIG_FILE" "$@")
printf "${BOLD}Running:%s${RESET}\n" " ${cmd[*]}"
"${cmd[@]}"

