@echo off
setlocal EnableDelayedExpansion

echo ========================================
echo Python Installer - Windows 10 / 11
echo ========================================

:: Vérifier droits admin
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Ce script doit etre execute en tant qu administrateur.
    pause
    exit /b
)

:: Vérifier si Python est deja installe
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python est deja installe.
    goto INSTALL_DEPS
)

echo Python non detecte. Telechargement...

set PYTHON_VERSION=3.12.8
set INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%INSTALLER%

powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%URL%' -OutFile '%INSTALLER%'"

if not exist %INSTALLER% (
    echo Echec du telechargement.
    pause
    exit /b
)

echo Installation de Python...
start /wait %INSTALLER% /quiet InstallAllUsers=1 PrependPath=1

if %errorlevel% neq 0 (
    echo Erreur lors de l installation de Python.
    pause
    exit /b
)

del %INSTALLER%

:: Rafraichir environnement
set PATH=%PATH%;C:\Program Files\Python312\

pip install notebook requests
:INSTALL_DEPS
echo Installation des dependances...

python install_dependencies.py

if %errorlevel% neq 0 (
    echo Erreur lors de l execution du script Python.
    pause
    exit /b
)

echo Installation terminee avec succes.
pause