from PIL import Image
import os
import shutil
import hashlib

# Dossiers
input_folder = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/Nouveau_Webtoons/merged_zones"
output_dir = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/Nouveau_Webtoons/only_img_with_interest"
duplicates_dir = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/Nouveau_Webtoons/duplicates_removed"
removed_dir = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/Nouveau_Webtoons/removed_img"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(duplicates_dir, exist_ok=True)
os.makedirs(removed_dir, exist_ok=True)

# Extensions autorisées
extensions = (".png", ".jpg", ".jpeg", ".bmp")

# Paramètres
white_tolerance = 20 # tolérance sur la nuance de blanc en RGB(255)
white_threshold = 0.98  # 98% de pixels blancs max

def is_white_page(image, tolerance=white_tolerance, threshold=white_threshold):
    width, height = image.size
    total_pixels = width * height
    white_pixels = 0

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            if (255 - tolerance <= r <= 255 and
                255 - tolerance <= g <= 255 and
                255 - tolerance <= b <= 255):
                white_pixels += 1

    return (white_pixels / total_pixels) >= threshold

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

    # Supprimer les très petites images (traits fins)
    if image.width <= 10 or image.height <= 10:
        print(f"{filename} → supprimée (image trop petite)")
        os.remove(image_path)
        continue

    # Supprimer si blanche
    if is_white_page(image):
        print(f"{filename} → supprimée (page blanche)")
        os.remove(image_path)
        continue

    # Vérifier les doublons par hash
    h = hash_image(image)
    if h in hashes_seen:
        print(f"{filename} → doublon détecté, déplacée vers {duplicates_dir}")
        shutil.move(image_path, os.path.join(duplicates_dir, filename))
    else:
        hashes_seen.add(h)
        print(f"{filename} → gardée")
        shutil.copy(image_path, os.path.join(output_dir, filename))
        
