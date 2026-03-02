import os
import shutil
from paths import ONLY_IMG_WITH_INTEREST, TEMP_IMG

input_folder = ONLY_IMG_WITH_INTEREST
output_folder = TEMP_IMG
os.makedirs(output_folder, exist_ok=True)

extensions = (".png", ".jpg", ".jpeg", ".bmp")

files = [f for f in os.listdir(input_folder) if f.lower().endswith(extensions)]
files.sort(key=lambda f: os.path.getctime(os.path.join(input_folder, f)))

for filename in files:
    image_path = os.path.join(input_folder, filename)
    shutil.copy(image_path, os.path.join(output_folder, filename))
    print(f"{filename} déplacée vers → {output_folder}")