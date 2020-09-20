color 0A
echo off
cls
:choice
echo Do you want to install Thorpy? [(y)es/(n)o]:
set /p choice=
if %choice%==y goto y
if %choice%==Y goto y
if %choice%==n goto n
if %choice%==N goto n
echo please enter 'y' for yes or 'n' for no.
pause
goto choice
:y
title installing...
echo installing...
echo on
pip install thorpy
echo off
pause
goto n
:n
echo created by Henry Letellier
echo " ._____. "
echo " |.   .| "
echo " |  |  | "
echo " |\___/| "
echo " |_____| "
timeout 3
pause
pause