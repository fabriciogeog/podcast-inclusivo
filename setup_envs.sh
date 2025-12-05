#!/usr/bin/env bash
# setup_envs.sh
# Script para criar e preparar ambientes virtuais para o projeto
# Uso: bash setup_envs.sh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Raiz do projeto: $ROOT_DIR"

# Backend venv
BACKEND_DIR="$ROOT_DIR/backend"
BACKEND_VENV="$BACKEND_DIR/venv"

if [ ! -d "$BACKEND_DIR" ]; then
  echo "Diretório backend não encontrado em $BACKEND_DIR"
else
  echo "Criando ambiente virtual para backend em $BACKEND_VENV"
  python3 -m venv "$BACKEND_VENV"
  echo "Ativando e instalando dependências do backend..."
  # shellcheck disable=SC1090
  source "$BACKEND_VENV/bin/activate"
  if [ -f "$BACKEND_DIR/requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r "$BACKEND_DIR/requirements.txt"
  else
    echo "Arquivo requirements.txt do backend não encontrado."
  fi
  deactivate
fi

# App venv
APP_DIR="$ROOT_DIR/app"
APP_VENV="$APP_DIR/venv"

if [ ! -d "$APP_DIR" ]; then
  echo "Diretório app não encontrado em $APP_DIR"
else
  echo "Criando ambiente virtual para app em $APP_VENV"
  python3 -m venv "$APP_VENV"
  echo "Ativando e instalando dependências do app..."
  # shellcheck disable=SC1090
  source "$APP_VENV/bin/activate"
  if [ -f "$APP_DIR/requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r "$APP_DIR/requirements.txt"
  else
    echo "Arquivo requirements.txt do app não encontrado."
  fi
  deactivate
fi

echo "Ambientes criados com sucesso."
echo "Para usar o backend:"
echo "  source \"$BACKEND_VENV/bin/activate\""
echo "  uvicorn app.main:app --reload --port 8000"
echo ""
echo "Para usar o app (desenvolvimento):"
echo "  source \"$APP_VENV/bin/activate\""
echo "  python app/main.py"
