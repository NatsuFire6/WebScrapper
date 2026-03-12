@echo off
REM Script d'assistance interactif pour lancer les scripts dans l'ordre.
REM L'utilisateur choisit pour chaque fichier s'il souhaite l'exécuter.

set SCRIPTS=cut_into_zones.py tryMerge.py remove_blank.py remove_duplicated.py

REM handle app.py separately with pre-check question

for %%F in (%SCRIPTS%) do (
    set /p answer=Do you want to run %%F? [Y/n] : 
    if /I "%%answer%%"=="Y" (
        echo Running %%F...
        python %%F
        echo.
    ) else (
        echo Skip %%F
        echo.
    )
)

REM special handling for app.py step
set /p check=Would you like to verify all images before putting them in the gallery? [Y/n] : 
if /I "%check%"=="Y" (
    echo Running move_images_for_app.py then app.py
    python move_images_for_app.py
    python app.py
    echo It is preferable to finish sorting before continuing.
) else (
    echo running move_images.py
    python move_images.py
)

REM continue with remaining
set SCRIPTS2=generateIndex.py remove_old_folders
for %%F in (%SCRIPTS2%) do (
    set /p answer=Do you want to run %%F? [Y/n] : 
    if /I "%%answer%%"=="Y" (
        echo Running %%F...
        python %%F
        if "%%F"=="generateIndex.py" (
            echo Opening gallery file...
            call :openGallery
        )
        echo.
    ) else (
        echo Skip %%F
        echo.
    )
)

goto :EOF

:openGallery
REM use path from environment variable set earlier
start "" "%GALLERY_HTML%"
exit /b

echo All scripts processed.
pause
