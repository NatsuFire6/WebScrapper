import os
import shutil
from paths import BASE_DIR

path = BASE_DIR
folders = ["duplicates_removed", "merged_zones", "only_img_with_interest", "static", "zones"]

for folder in folders :
    shutil.rmtree(os.path.join(path, folder))
    print(f'folder "{path}{folder}" was removed')