# To use this project you need to coppy in a new folder :

- download_images.ipynb
- cut_into_zones.py
- tryMerge.py
- remove_useless_and_blank.py
- app.py
- generateIndex.py
- index.html

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

⚠️if all image have almost the same size and they are never cut skip the "Second" step.

## Second:
 - launch "cut_into_zones.py" //fast
 - launch "tryMerge.py"       //fast

## Third:
 - launch "remove_useless_and_blank.py"  //very slow
   copy all images of the folder "only_img_with_interest/" into "static/zones/"

## Fourth:
 - launch "app.py" to be sure only good images are saved
   take so much time to sort them and try to have almost the same size on all your images

  ⚠️if you don't mind to do "Fourth" step, you can skip it but you need to :
 - change the "merged_dir" to "only_img_with_interest"

## Fifth:
 - launch "generateIndex.py"
 - open "galery.html" with your browser
 - Enjoy !