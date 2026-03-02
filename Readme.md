I make a presentation'video for this project but she's in french, if you want to see it : "https://www.youtube.com/watch?v=XiLaqIsAz-Q"

# (English) To use this project you need to :

install the zip file at : "https://github.com/NatsuFire6/WebScrapper/releases/tag/1.0"
or to git clone this project : "git clone https://github.com/NatsuFire6/WebScrapper.git"

## Zero (install dependencies):
 - Launch "install_dependencies.bat"
  #### OR
 - install anaconda navigator
 - install jupyter "Notebook"
 - install Python3
 - install Flask (python's server)

 ## In paths.py :
 - The "BASE_DIR" path have to be changed to match the place where you want to see the result e.g: "C:/Users/UserName/Desktop/python/Nouveau_Webtoons" --> "C:/Users/JamesTheBest/Desktop/TheBestWebtoons"

## First (download images):
- open "download_images.ipynb" with Jupyter notebook
  change the webtoons URL to the first one of wich one you want
  change the "output_dir" to the correct path
  launch all the script with jupiter notebook //very slow
  (wait as long as necessary, the program should end with an error and that is normal)

## All process :
 - launch "run_steps.bat"
## OR
### Second (transform images):
⚠️If all image have the same size and they are never cut skip the "Second" step.

 - launch "cut_into_zones.py" //fast
 - launch "tryMerge.py"       //fast

### Third (remove useless images):
 - launch "remove_blank.py"  // slow
 
⚠️If there are multiple times the same images, the following ones will be deleted, so be careful when you do it, it is strongly recommended to even quickly check the images that have just been deleted !
  #### If you don't trust the process skip this step.
 - launch "remove_duplicated.py"  // slow
   
### Fourth (verify all images):
⚠️If you don't care about "Fourth" step, you can skip it but you need to :
 - launch "move_images.py"
   #### If you care of this step :
 - launch "move_images_for_app.py"
 - launch "app.py" to be sure only good images are saved
   take your time to sort them and try to have almost the same size on all your images

### Fifth (generate galery):
 - launch "generateIndex.py"
 - open "galery.html" with your browser
 - Enjoy !
 - Hint: launch "remove_old_folders.py" to remove all images and folders you no longer need !

# (Français) Pour utiliser ce projet vous devez :

installer le fichier zip : "https://github.com/NatsuFire6/WebScrapper/releases/tag/1.0"
ou git clone ce projet : "git clone https://github.com/NatsuFire6/WebScrapper.git"

## 0. (installer les dépendances):
 - Exécuter "install_dependencies.bat"
  ### OU
 - installer anaconda navigator : "https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe"
 - installer "jupyter Notebook" dans anaconda navigator
 - installer Python3 : "https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe"
 - installer Flask (python's server)
 

## Dans paths.py :
 - Le chemin "BASE_DIR" doit être modifié pour correspondre à l'emplacement où vous voulez voir le résultat ex : "C: Users/UserName/Desktop/python/Nouveau_Webtoons" --> "C:/Users/JamesTheBest/Desktop/TheBestWebtoons"

## 1. (téléchargez les images):
- ouvrez "download_images.ipynb" avec Jupyter notebook
  changez l'URL du webtoons pour le premier episode du webtoons que vous voulez
  changez le "output_dir" vers le chemin correct (changer le chemin)
  exécutez tout le script avec Jupyter notebook //très lent
  (attendez aussi longtemps que nécessaire, le programme devrait ce terminer avec une erreur et c'est normal)

## Tout faire d'un coup :
 - Exécuter "run_steps.bat"
## Ou
### 2. (transformer les images):
⚠️Si toutes les images ont la même taille et qu'elles ne sont jamais coupées, sautez cette l'étape.

 - Exécutez "cut_into_zones.py" //Rapide
 - Exécutez "tryMerge.py"       //Rapide

### 3. (supprimer les images inutiles):
 - Exécutez "remove_blank.py"  // Rapide
 
⚠️Si les mêmes images apparaissent plusieurs fois, les suivantes seront supprimées, alors faites attention lorsque vous le faites, il est fortement recommandé de vérifier même rapidement les images qui viennent d'être supprimées !
#### Si vous ne faites pas confiance au processus, passez cette étape.
  - Exécutez "remove_duplicated.py" // lent
   
### 4. (vérifiez toutes les images) :
⚠️Si cela ne vous dérange pas, vous pouvez passer cette étape, mais vous devrez :
  - Exécutez « move_images.py »
#### Si vous voulez faire cette étape :
  - copiez toutes les images du dossier « only_img_with_interest/ » dans « static/zones/ »
  - Exécutez « app.py » pour vous assurer que seules les bonnes images sont sauvegardées
  prenez votre temps pour les trier et essayez d'avoir presque la même taille pour toutes vos images

### 5. (générer la galerie) :
- Exécutez "generateIndex.py"
- ouvrez "galery.html" avec votre navigateur
- Profitez !
- Tip : Exécute le script "remove_old_folders.py" pour vider tout ce qui ne te sert plus !