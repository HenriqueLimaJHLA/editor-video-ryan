#!/bin/bash
cd "$(dirname "$0")"
command -v python3 >/dev/null || { echo "Instale o Python: https://www.python.org/downloads/"; read -p "Enter para sair"; exit 1; }
python3 scripts/instalar.py "$@"
read -p "Pressione Enter para fechar"
