from flask import Flask, render_template, redirect, url_for
from PIL import Image
import os
import shutil
import re

app = Flask(__name__)

from paths import ONLY_IMG_WITH_INTEREST, VALIDATED_ZONES, TEMP_IMG

ZONES_FOLDER = ONLY_IMG_WITH_INTEREST
VALIDATED_FOLDER = VALIDATED_ZONES
TEMP_FOLDER = TEMP_IMG

os.makedirs(VALIDATED_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)
os.makedirs(ZONES_FOLDER, exist_ok=True)

def get_image_files():
    def extract_number(filename):
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else float('inf')

    return sorted(
        [f for f in os.listdir(ZONES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))],
        key=extract_number
    )

@app.route("/")
def index():
    files = get_image_files()
    if not files:
        return "Aucune image disponible."

    current_image = files[0]
    next_image = files[1] if len(files) > 1 else None
    after_next_image = files[2] if len(files) > 2 else None

    def get_image_path(filename):
        if not filename:
            return None
        temp_path = os.path.join(TEMP_FOLDER, filename)
        if os.path.exists(temp_path):
            return url_for('static', filename=f"temp_zones/{filename}")
        return url_for('static', filename=f"zones/{filename}")

    current_image_path = get_image_path(current_image)
    next_image_path = get_image_path(next_image)
    after_next_path = get_image_path(after_next_image)

    return render_template(
    "index.html",
    current_image_path=current_image_path,
    next_image_path=next_image_path,
    after_next_path=after_next_path,
    remaining_images=len(files)
)


@app.route("/delete_current")
def delete_current():
    files = get_image_files()
    if not files:
        return redirect(url_for('index'))

    current_image = files[0]
    os.remove(os.path.join(ZONES_FOLDER, current_image))
    
    # Supprime la version temporaire si elle existe
    temp_path = os.path.join(TEMP_FOLDER, current_image)
    if os.path.exists(temp_path):
        os.remove(temp_path)

    return redirect(url_for('index'))

@app.route("/save_both")
def save_both():
    files = get_image_files()
    for img in files[:2]:  # current + next
        src = os.path.join(ZONES_FOLDER, img)
        dst = os.path.join(VALIDATED_FOLDER, img)
        if os.path.exists(src):
            shutil.move(src, dst)
        # Supprimer éventuelle version temporaire
        temp_path = os.path.join(TEMP_FOLDER, img)
        if os.path.exists(temp_path):
            os.remove(temp_path)
    return redirect(url_for('index'))

@app.route("/save")
def save():
    files = get_image_files()
    if not files:
        return redirect(url_for('index'))

    current_image = files[0]

    # Supprimer l'éventuelle version temp
    temp_path = os.path.join(TEMP_FOLDER, current_image)
    if os.path.exists(temp_path):
        os.remove(temp_path)

    shutil.move(os.path.join(ZONES_FOLDER, current_image), os.path.join(VALIDATED_FOLDER, current_image))
    return redirect(url_for('index'))

@app.route("/delete")
def delete():
    files = get_image_files()
    if len(files) < 2:
        return redirect(url_for('index'))

    next_image = files[1]
    os.remove(os.path.join(ZONES_FOLDER, next_image))
    return redirect(url_for('index'))

@app.route("/delete_both")
def delete_both():
    files = get_image_files()
    for img in files[:2]:  # supprime actuelle + suivante
        if img:
            img_path = os.path.join(ZONES_FOLDER, img)
            if os.path.exists(img_path):
                os.remove(img_path)
            # supprime version temporaire si elle existe
            temp_path = os.path.join(TEMP_FOLDER, img)
            if os.path.exists(temp_path):
                os.remove(temp_path)
    return redirect(url_for('index'))

@app.route("/merge")
def merge():
    files = get_image_files()
    if len(files) < 2:
        return redirect(url_for('index'))

    image1_path = os.path.join(ZONES_FOLDER, files[0])
    image2_path = os.path.join(ZONES_FOLDER, files[1])
    image1 = Image.open(image1_path).convert("RGB")
    image2 = Image.open(image2_path).convert("RGB")

    merged_image = Image.new("RGB", (max(image1.width, image2.width), image1.height + image2.height), (255, 255, 255))
    merged_image.paste(image1, (0, 0))
    merged_image.paste(image2, (0, image1.height))
    merged_image.save(image1_path)

    temp_image_path = os.path.join(TEMP_FOLDER, files[0])
    merged_image.save(temp_image_path)

    os.remove(image2_path)
    return redirect(url_for('index'))

@app.route("/merge_next")
def merge_next():
    files = get_image_files()
    if len(files) < 3:
        return redirect(url_for('index'))

    image2_path = os.path.join(ZONES_FOLDER, files[1])
    image3_path = os.path.join(ZONES_FOLDER, files[2])
    image2 = Image.open(image2_path).convert("RGB")
    image3 = Image.open(image3_path).convert("RGB")

    merged_image = Image.new("RGB", (max(image2.width, image3.width), image2.height + image3.height), (255, 255, 255))
    merged_image.paste(image2, (0, 0))
    merged_image.paste(image3, (0, image2.height))
    merged_image.save(image2_path)

    temp_image_path = os.path.join(TEMP_FOLDER, files[1])
    merged_image.save(temp_image_path)

    os.remove(image3_path)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
