# To use this project you need to coppy in a new folder :

- download_images.ipynb
- cut_into_zones.py
- tryMerge.py
- remove_useless_and_blank.py
- app.py
- move_images.py
- remove_old_folder.py
- generateIndex.py
- templates/index.html
- Allimages/

## Zero:
 - install anaconda navigator
 - install jupyter "Notebook"
 - install Python3
 - install Flask (python's server)
 
## First:
- open "download_images.ipynb" with Jupyter notebook
  change the webtoons URL to the first one of wich one you want
  change the "output_dir" to the correct path
  launch all the script with jupiter notebook //very slow
  (wait a very long time)

⚠️if all image have the same size and they are never cut skip the "Second" step.

## Second:
 - launch "cut_into_zones.py" //fast
 - launch "tryMerge.py"       //fast

## Third:
 - launch "remove_useless_and_blank.py"  // slow and can make mistake with "duplicated img" ~1%
(les images peuvent être naturellement les mêmes, il faudrait sauvegarder les images et si elle finit par avoir un doublons alors il faut aussi supprimer la première, copier chaque image dans un dossier différent, si à la fin il y a minimum 3(tolérence variable) images, qui sont donc les même alors, supprimer toutes les images de ce dossier)
(faire un script qui reprend toutes les images correcte et les place dans le bon dossier pour le prochain script)
   
⚠️if you don't mind to do "Fourth" step, you can skip it but you need to :
 - launch "move_images.py"

## Fourth:
 - copy all images of the folder "only_img_with_interest/" into "static/zones/"
 - launch "app.py" to be sure only good images are saved
   take so much time to sort them and try to have almost the same size on all your images

## Fifth:
 - launch "generateIndex.py"
 - open "galery.html" with your browser
 - Enjoy !