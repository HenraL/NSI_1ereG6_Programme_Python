echo off
color 0A
cls
echo coucou
echo Comment vas-tu Irina? [(tb)tres_bien/(b)bien/(m)moyen/(pbd)pas_bien_dutout]
set/p choice=
if %choice%==tb goto tb
if %choice%==Tb goto tb
if %choice%==tB goto tb
if %choice%==TB goto tb
if %choice%==b goto b
if %choice%==B goto b
if %choice%==m goto m
if %choice%==M goto m
if %choice%==pdb goto pdb
if %choice%==Pdb goto pdb
if %choice%==PDb goto pdb
if %choice%==PDB goto pdb
if %choice%==pDb goto pdb
if %choice%==pdB goto pdb
if %choice%==PdB goto pdb
:tb
echo "cool :-)"
pause
:b
echo "M Clercbonjuant"
pause
:m
echo "Dis moi dans whatsapp ce qui vas moyen :-|"
pause
:pdb
echo "Dis-moi dans Whatsapp ce qui ne vas pas :-("
pause