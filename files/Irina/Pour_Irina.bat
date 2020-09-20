echo off
color 0A
cls
:q
echo Activer le message au demarage? [(o)ui/(n)on]:
set /p Activer=
if %Activer%==o goto o
if %Activer%==O goto o
if %Activer%==0 goto o
if %Activer%==n goto n
if %Activer%==N goto n
echo merci de ne rentrer que 'o' pour oui ou 'n' pour non
goto q
:o
copy IRINA_L.bat ..\..\..\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
:n
REM C:\Users\Henry PC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup