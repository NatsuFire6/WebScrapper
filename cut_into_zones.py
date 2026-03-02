from PIL import Image
import os
from paths import ALL_IMAGES, ZONES

# Dossier contenant les images à traiter (défini dans paths.py)
input_folder = ALL_IMAGES
# Dossier de sortie pour toutes les zones
output_dir = ZONES
os.makedirs(output_dir, exist_ok=True)

# Extensions d’image acceptées
extensions = (".png", ".jpg", ".jpeg", ".bmp")

global_zone_count = 0  # Numéro global pour toutes les zones

files = [f for f in os.listdir(input_folder) if f.lower().endswith(extensions)]
files.sort(key=lambda f: os.path.getctime(os.path.join(input_folder, f)))
for filename in files:
    if filename.lower().endswith(extensions):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path).convert("RGB")
        width, height = image.size

        in_zone = False
        start_h = 0

        for h in range(height):
            ligne_est_blanche = True
            for w in range(width):
                r, g, b = image.getpixel((w, h))
                if (r, g, b) != (255, 255, 255):
                    ligne_est_blanche = False
                    break

            if not ligne_est_blanche and not in_zone:
                in_zone = True
                start_h = h

            if ligne_est_blanche and in_zone:
                end_h = h
                zone = image.crop((0, start_h, width, end_h))
                zone.save(os.path.join(output_dir, f"zone_{global_zone_count}.png"))
                print(f"{filename} → Zone {global_zone_count} enregistrée de {start_h} à {end_h}")
                global_zone_count += 1
                in_zone = False

        if in_zone:
            zone = image.crop((0, start_h, width, height))
            zone.save(os.path.join(output_dir, f"zone_{global_zone_count}.png"))
            print(f"{filename} → Zone {global_zone_count} enregistrée de {start_h} à {height}")
            global_zone_count += 1
