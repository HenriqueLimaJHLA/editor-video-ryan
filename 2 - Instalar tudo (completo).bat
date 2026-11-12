@echo off
chcp 65001 >nul
title Editor de Video Ryan - Instalacao completa
cd /d "%~dp0"
echo ============================================
echo   Editor de Video Ryan - Instalacao completa
echo ============================================
where python >nul 2>nul
if errorlevel 1 (
  echo.
  echo O Python nao esta instalado. Vou instalar agora...
  winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements
  echo.
  echo Python instalado. FECHE esta janela e clique de novo no arquivo.
  pause
  exit /b
)
python "scripts\instalar.py" --completo
echo.
pause
