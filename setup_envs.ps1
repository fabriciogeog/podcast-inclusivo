# setup_envs.ps1
# Script PowerShell para criar ambientes virtuais no Windows
# Uso: .\setup_envs.ps1
$ErrorActionPreference = "Stop"

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Write-Host "Raiz do projeto: $RootDir"

# Backend
$BackendDir = Join-Path $RootDir "backend"
$BackendVenv = Join-Path $BackendDir "venv"

if (Test-Path $BackendDir) {
    Write-Host "Criando ambiente virtual para backend em $BackendVenv"
    python -m venv $BackendVenv
    Write-Host "Ativando e instalando dependências do backend..."
    & "$BackendVenv\\Scripts\\Activate.ps1"
    $req = Join-Path $BackendDir "requirements.txt"
    if (Test-Path $req) {
        python -m pip install --upgrade pip
        python -m pip install -r $req
    } else {
        Write-Host "Arquivo requirements.txt do backend não encontrado."
    }
    Deactivate
} else {
    Write-Host "Diretório backend não encontrado."
}

# App
$AppDir = Join-Path $RootDir "app"
$AppVenv = Join-Path $AppDir "venv"

if (Test-Path $AppDir) {
    Write-Host "Criando ambiente virtual para app em $AppVenv"
    python -m venv $AppVenv
    Write-Host "Ativando e instalando dependências do app..."
    & "$AppVenv\\Scripts\\Activate.ps1"
    $req = Join-Path $AppDir "requirements.txt"
    if (Test-Path $req) {
        python -m pip install --upgrade pip
        python -m pip install -r $req
    } else {
        Write-Host "Arquivo requirements.txt do app não encontrado."
    }
    Deactivate
} else {
    Write-Host "Diretório app não encontrado."
}

Write-Host "Ambientes criados com sucesso."
Write-Host "Para usar o backend:"
Write-Host "  & `"$BackendVenv\\Scripts\\Activate.ps1`""
Write-Host "  uvicorn app.main:app --reload --port 8000"
Write-Host ""
Write-Host "Para usar o app (desenvolvimento):"
Write-Host "  & `"$AppVenv\\Scripts\\Activate.ps1`""
Write-Host "  python app\\main.py"
