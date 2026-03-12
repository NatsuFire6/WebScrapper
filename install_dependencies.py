import subprocess
import sys
import importlib.util

REQUIRED_PACKAGES = [
    "flask",
    "requests",
    "beautifulsoup4",
    "pillow",
]

def is_installed(package):
    """Vérifie si un package Python est déjà installé."""
    return importlib.util.find_spec(package) is not None

def install(package):
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    for pkg in REQUIRED_PACKAGES:
        if is_installed(pkg):
            print(f"{pkg} déjà installé.")
            continue
        try:
            install(pkg)
        except subprocess.CalledProcessError:
            print(f"Erreur lors de l'installation de {pkg}")
    print("\nInstallation terminée.")

if __name__ == "__main__":
    main()