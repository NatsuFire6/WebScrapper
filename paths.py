"""Centralise les chemins d'accès aux dossiers utilisés par les scripts.

Modifier les valeurs ici permet de rediriger tous les scripts vers de nouveaux dossiers
sans avoir à éditer chaque fichier individuellement.
"""
import os

# base workspace for webtoons project
BASE_DIR = r"C:/Users/UserName/Desktop/python/Nouveau_Webtoons"

# dossiers d'entrée / sortie utilisés fréquemment
ALL_IMAGES = os.path.join(BASE_DIR, "AllImages")
MERGED_ZONES = os.path.join(BASE_DIR, "merged_zones")
ZONES = os.path.join(BASE_DIR, "zones")
ONLY_IMG_WITH_INTEREST = os.path.join(BASE_DIR, "only_img_with_interest")
DUPLICATES_REMOVED = os.path.join(BASE_DIR, "duplicates_removed")
VALIDATED_ZONES = os.path.join(BASE_DIR, "validated_zones")
REMOVED_IMG = os.path.join(BASE_DIR, "removed_img")
TEMP_IMG = os.path.join(BASE_DIR, "static", "temp_zones")

# exemple :
# from paths import MERGED_ZONES, ONLY_IMG_WITH_INTEREST
# input_folder = MERGED_ZONES
# output_dir = ONLY_IMG_WITH_INTEREST
