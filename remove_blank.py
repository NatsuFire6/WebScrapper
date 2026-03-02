from PIL import Image
import os

# Dossiers
input_folder = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/images_after_GPT/merged_zones"
output_dir = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/images_after_GPT/only_img_with_interest"
duplicates_dir = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/images_after_GPT/duplicates_removed"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(duplicates_dir, exist_ok=True)

# Extensions autorisées
extensions = (".png", ".jpg", ".jpeg", ".bmp")

# Paramètres
white_tolerance = 20
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

# Traitement

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
        
