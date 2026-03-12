@echo off
echo Verification de Jupyter Notebook...

where jupyter >nul 2>nul
if %errorlevel% neq 0 (
    echo ERREUR : Jupyter Notebook n'est pas installe.
    pause
    exit
)

echo Lancement de Jupyter Notebook...

cd /d %~dp0

jupyter notebook download_images.ipynb