REM met la couleur à écriture verte sur fond noir
color 0A
REM n'affiche pas C:\... mais juste la comande
echo off
REM si votre disque dure se nome D il ira dedans
cd D:\
REM si votre disque dure se nome C il ira dans ce dernier et pas dans D
cd C:\
REM netoie l'écran
cls
REM première balise
:choice
echo si l'invite des comandes vous affiche "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x04A394D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/pygame/"
echo Essayez d'‚x‚cuter l'invite des comandes en mode administrateur ou d'activer votre wifi
REM question
echo Voulez-vous installer pygame? [(o)ui/(n)on/(m)ettre a jour]:
REM variable pour récupérer votre choix
set /p choice=
REM instructions
if %choice%==o goto i
REM instructions
if %choice%==O goto i
REM instructions
if %choice%==0 goto i
REM instructions
if %choice%==n goto n
REM instructions
if %choice%==N goto n
REM instructions
if %choice%==m goto m
REM instructions
if %choice%==M goto m
REM message d'erreur
echo Veuillez n'entrer que la lettre "o" ou la lettre "n" ou la lettre "m".
REM instructions
goto choice
REM balise
:i
REM texte
echo Installation:
REM affiche C:\....
echo on
REM première tentative d'installation
py -m pip install -U pygame --user
REM n'affiche pas C:\... mais juste la comande
echo off
REM test pour voir si pygame est installé
echo commandes pour jouer:
echo    - touche espace pour tirer
echo    - fleche droite pour aller a droite
echo    - fleche gauche pour aller a gauche
REM on met la commande en pause
pause
REM on va lancer le jeux pygame
py -m pygame.examples.aliens
REM texte
echo pygame a ‚t‚ install‚ sur votre ordinateur.
REM balise
:q
REM question
echo Voulez-vous mettre a jour pygame [(o)ui/(n)on]:
set /p choice=
REM instructions
if %choice%==o goto m
REM instructions
if %choice%==O goto m
REM instructions
if %choice%==0 goto m
REM instructions
if %choice%==n goto n
REM instructions
if %choice%==N goto n
REM message d'erreur
echo Veuillez n'entrer que la lettre "o" ou la lettre "n".
REM instructions
goto q
REM balise
:m
REM affiche C:\....
echo on
REM ligne de code pour mettre a jour pip
py -m pip install -U pygame --user
REM n'affiche pas C:\... mais juste la comande
echo off
REM test pour voir si pygame est installé
echo commandes pour jouer:
echo    - touche espace pour tirer
echo    - fleche droite pour aller a droite
echo    - fleche gauche pour aller a gauche
REM on met la commande en pause
pause
REM on va lancer le jeux pygame
py -m pygame.examples.aliens
REM n'affiche pas C:\... mais juste la comande
echo off
REM Texte
echo pygame a ‚t‚ mis a jour sur votre ordinateur.
REM instructions
goto n
REM balise
:n
REM texte
echo Au revoir
REM texte
echo cr‚‚ par Henry Letellier
REM texte
echo " ._____. "
REM texte
echo " |.   .| "
REM texte
echo " |  |  | "
REM texte
echo " |\___/| "
REM texte
echo " |_____| "
REM temp de pause
timeout 3
REM met l'invite en pause
pause
REM met l'invite en pause
pause