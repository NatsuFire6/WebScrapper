import os
import re

# Fonction de tri naturel
def natural_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

from paths import VALIDATED_ZONES, OUTPUT_HTML

# Dossier contenant les images fusionnées (depuis paths.py)
merged_dir = VALIDATED_ZONES
output_html = OUTPUT_HTML

# Filtres d'extension d'images valides
valid_extensions = ('.jpg', '.jpeg', '.png')

# Liste triée naturellement
images = sorted(
    [f for f in os.listdir(merged_dir) if f.lower().endswith(valid_extensions)],
    key=natural_key
)

# Début du contenu HTML
html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Affichage BD Reconstituée</title>
  <style>
    body {
      background: #eee;
      font-family: sans-serif;
      padding: 20px;
    }
    .bd-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
    }
    .bd-case {
      background: white;
      border: 4px solid black;
      box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
    }
    .bd-case img {
      width: 100%;
      height: auto;
      display: block;
    }
  </style>
</head>
<body>
  <button id="toggle-bg" style="position: fixed; top: 10px; left: 10px; z-index: 1000; padding: 10px; background: black; color: white; border: none; border-radius: 5px; cursor: pointer;">
    Inverser la couleur de fond
  </button>
  <h1>Affichage BD Reconstituée</h1>
  <div class="bd-container">
"""

# Ajout des images triées
for img in images:
    html += f'    <div class="bd-case"><img src="{merged_dir}/{img}" alt="{img}"></div>\n'

html += """  </div>
  <script>
    const button = document.getElementById('toggle-bg');
    button.addEventListener('click', () => {
      const body = document.body;
      const currentBg = getComputedStyle(body).backgroundColor;
      body.style.backgroundColor = currentBg === 'rgb(238, 238, 238)' ? 'black' : '#eee';
      body.style.color = currentBg === 'rgb(238, 238, 238)' ? 'white' : 'black';
    });
  </script>
</body>
</html>
"""

# Écriture dans le fichier HTML
with open(output_html, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Fichier HTML généré avec {len(images)} images triées dans '{output_html}'")
