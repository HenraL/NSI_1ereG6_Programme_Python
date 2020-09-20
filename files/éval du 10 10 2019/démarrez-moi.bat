echo off
color 0A
cls
echo ceci n'est pas un programme malveillant.
timeout/T 2
cls
cmd/c "files\watermark.bat"
echo Bonjour et Bienvenue dans le fichier évaluation du 10 10 2019
:start
echo voir le Document word (vdw), voir le code python (vcp), quitter (q)
set /p mol=
if %mol%==vdw goto vdw
if %mol%==vcp goto vcp
if %mol%==q goto q
goto start
:vdw
echo Sorry file not avaidable, please check in the folder files to see if you can find Interrogation_2_NSI_Cours_HATTEMER_1ère6_JEUDI_10_OCTOBRE_2019.docx
goto start
:vcp
cmd/c "files\py.vbs"
goto start
:q
echo au revoir
timeout/T 2