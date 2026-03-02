"""Installe automatiquement les dépendances Python requises pour le projet.
Ce script peut être transformé en exécutable Windows (.exe) via pyinstaller :

    pyinstaller --onefile install_dependencies.py

Il suffit ensuite de lancer l'exécutable sur une machine disposant de Python.
"""
import subprocess
import sys

REQUIRED_PACKAGES = [
    "flask",
    "requests",
    "beautifulsoup4",
    "pillow",
]


def install(package):
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def main():
    """Installe chaque dépendance et affiche le résultat."""
    for pkg in REQUIRED_PACKAGES:
        try:
            install(pkg)
        except subprocess.CalledProcessError:
            print(f"Erreur lors de l'installation de {pkg}")
    print("\n✅ Toutes les dépendances tentées. Vérifiez les messages ci-dessus pour les erreurs.")


if __name__ == "__main__":
    main()
