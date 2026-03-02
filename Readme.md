# To use this project you need to copy or create in a new folder :

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

## Zero (install dependency):
 - install anaconda navigator
 - install jupyter "Notebook"
 - install Python3
 - install Flask (python's server)
 
## First (download images):
- open "download_images.ipynb" with Jupyter notebook
  change the webtoons URL to the first one of wich one you want
  change the "output_dir" to the correct path
  launch all the script with jupiter notebook //very slow
  (wait a very long time)

## Second (transform images):
⚠️If all image have the same size and they are never cut skip the "Second" step.

 - launch "cut_into_zones.py" //fast
 - launch "tryMerge.py"       //fast

## Third (remove images):
⚠️If there are multiple times the same images, the following ones will be deleted, so be careful when you do it, it is strongly recommended to even quickly check the images that have just been deleted !
  If you don't trust the process or don't care about blank skip the "Third" step.
 - launch "remove_useless_and_blank.py"  // slow
   
## Fourth (verify all images):
⚠️If you don't mind to do "Fourth" step, you can skip it but you need to :
 - launch "move_images.py"
   ### If you mind of this step :
 - copy all images of the folder "only_img_with_interest/" into "static/zones/"
 - launch "app.py" to be sure only good images are saved
   take your time to sort them and try to have almost the same size on all your images

## Fifth (generate galery):
 - launch "generateIndex.py"
 - open "galery.html" with your browser
 - Enjoy !
