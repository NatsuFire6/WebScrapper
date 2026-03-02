from PIL import Image
import os
import shutil
import hashlib
from paths import ONLY_IMG_WITH_INTEREST, DUPLICATES_REMOVED

# Dossiers (définis dans paths.py)
input_folder = ONLY_IMG_WITH_INTEREST
output_dir = ONLY_IMG_WITH_INTEREST
duplicates_dir = DUPLICATES_REMOVED
os.makedirs(output_dir, exist_ok=True)
os.makedirs(duplicates_dir, exist_ok=True)

# Extensions autorisées
extensions = (".png", ".jpg", ".jpeg", ".bmp")

def hash_image(image):
    # Calcule un hash MD5 de l’image pour identifier les doublons
    resized = image.resize((128, 128)).convert("RGB")  # Normaliser
    return hashlib.md5(resized.tobytes()).hexdigest()

# Traitement
hashes_seen = set()

files = [f for f in os.listdir(input_folder) if f.lower().endswith(extensions)]
files.sort(key=lambda f: os.path.getctime(os.path.join(input_folder, f)))

for filename in files:
    image_path = os.path.join(input_folder, filename)
    image = Image.open(image_path).convert("RGB")

    # Vérifier les doublons par hash
    h = hash_image(image)
    if h in hashes_seen:
        print(f"{filename} → doublon détecté, déplacée vers {duplicates_dir}")
        shutil.move(image_path, os.path.join(duplicates_dir, filename))
    else:
        hashes_seen.add(h)
        print(f"{filename} → gardée")
        shutil.copy(image_path, os.path.join(output_dir, filename))
        

