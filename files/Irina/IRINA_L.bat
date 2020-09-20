echo off
color 0A
:ff
cls
echo Executer
echo enter
echo shell:startup
cd ..
start Startup
cd Startup
echo Continuer? [(o)ui/(n)on]:
set /p choice=
if %choice%==o goto o
if %choice%==O goto o
if %choice%==0 goto o
if %choice%==n goto n
if %choice%==N goto n
echo assurez-vous de ne rentrer que 'o' pour oui ou 'n' pour non
goto ff
cls
:o
echo Pour stopper faire ctrl+c
timeout 1
:I
echo "  ___   ___  "
echo " /   \_/   \ "
echo " \         / "
echo "  \ Irina /  "
echo "   \     /   "
echo "    \   /    "
echo "     \_/     "
timeout 1
goto I
:n
echo au revoir
timeout 1
echo Créé par Henry Letellier
timeout 1
pause
pause