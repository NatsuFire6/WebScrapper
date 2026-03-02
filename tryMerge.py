from PIL import Image
import os
from paths import ZONES, MERGED_ZONES

# Dossier contenant les images à traiter (défini dans paths.py)
input_folder = ZONES
output_dir = MERGED_ZONES
os.makedirs(output_dir, exist_ok=True)

extensions = (".png", ".jpg", ".jpeg", ".bmp")
files = [f for f in os.listdir(input_folder) if f.lower().endswith(extensions)]
files.sort(key=lambda f: os.path.getctime(os.path.join(input_folder, f)))

global_image_count = 0
accumulated_images = []
tolerance = 10  # Tolérance pour la détection de la couleur blanche

def is_last_line_white(image):
    width, height = image.size
    for x in range(width):
        r, g, b = image.getpixel((x, height - 1))
        if not (255 - tolerance <= r <= 255 and
                255 - tolerance <= g <= 255 and
                255 - tolerance <= b <= 255):
            return False
    return True


def merge_images_vertically(images):
    total_height = sum(img.height for img in images)
    width = max(img.width for img in images)
    merged = Image.new("RGB", (width, total_height), (255, 255, 255))
    y_offset = 0
    for img in images:
        merged.paste(img, (0, y_offset))
        y_offset += img.height
    return merged

for filename in files:
    image_path = os.path.join(input_folder, filename)
    image = Image.open(image_path).convert("RGB")
    accumulated_images.append(image)

    if is_last_line_white(image):
        merged_image = merge_images_vertically(accumulated_images)
        output_path = os.path.join(output_dir, f"merged_{global_image_count}.png")
        merged_image.save(output_path)
        print(f"{filename} → Image {global_image_count} enregistrée avec {len(accumulated_images)} image(s)")
        global_image_count += 1
        accumulated_images = []

# Enregistrer les images restantes s'il n'y a pas de ligne blanche finale
if accumulated_images:
    merged_image = merge_images_vertically(accumulated_images)
    output_path = os.path.join(output_dir, f"merged_{global_image_count}_unfinished.png")
    merged_image.save(output_path)
    print(f"Image incomplète enregistrée sous merged_{global_image_count}_unfinished.png")
