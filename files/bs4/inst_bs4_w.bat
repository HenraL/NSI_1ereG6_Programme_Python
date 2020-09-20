REM met a couleur à écriture verte sur fond noir
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
echo si l'invite des comandes vous affiche "Could not install packages due to an EnvironmentError: [WinError 5] Acces refus‚: 'c:\\\\program files (x86)\\\\python37-32\\\\Lib\\\\site-packages\\\\soupsieve'"
echo ou
echo "Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: 'C:\\\\Program Files (x86)\\\\Python37-32\\\\Lib\\\\site-packages\\\\pip\\\\__init__.py'"
echo Essayez d'‚x‚cuter l'invite des comandes en mode administrateur
REM question
echo Voulez-vous installer beautifulsoup4? [(o)ui/(n)on/(m)ettre a jour]:
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
pip3 install beautifulsoup4
REM seconde tentative d'installation si première rate
py -3 -m pip install beautifulsoup4
REM troisième tentative d'installation si seconde rate
--user pip install beautifulsoup4
REM n'affiche pas C:\... mais juste la comande
echo off
REM texte
echo beautifulsoup4 a ‚t‚ install‚ sur votre ordinateur.
REM balise
:q
REM question
echo Voulez-vous mettre a jour pip/beautifulsoupe [(o)ui/(n)on]:
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
python -m pip install --upgrade pip
REM seconde tentative
--user python -m pip install --upgrade pip
REM n'affiche pas C:\... mais juste la comande
echo off
REM Texte
echo pip/beautifulsoup a ‚t‚ mis a jour sur votre ordinateur.
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