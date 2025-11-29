import os
import shutil

path = "C:/Users/LA TOUR MSI DU TURFU/Desktop/python/Nouveau_Webtoons/"
folders = ["duplicates_removed", "merged_zones", "only_img_with_interest", "static", "zones"]

for folder in folders :
    shutil.rmtree(os.path.join(path, folder))
    print(f'folder "{path}{folder}" was removed')