commande = "files\Interrogation_2_NSI_Cours_HATTEMER_1ère6_JEUDI_10_OCTOBRE_2019.py"
Set fso = CreateObject("Scripting.FileSystemObject" )
set shl = createobject("wscript.shell" )
shl.run """"+commande+"""",1,false