#Créé par Henry Letellier 
import codecs, os, tkinter, sys
from msvcrt import getch, kbhit
from time import sleep
a="ereefedre\n"
f=open("lettre.txt", "a")
s=f.write(a)
f.close()
f=open("lettre.txt", "r")
s=f.read()
print ("** Début d'affichage  du cache de 'lettre.txt'**\n{}** Fin d'affichage du cache de 'lettre.txt' **".format(s))
f.close()

while True:
    if kbhit():
        final="======================== Début de la touche ========================\n"
        z=getch()
        # print(final,z)
        code=ord(z)
        if ord(z)==27:
            final+="Echap = {} = ".format(z)
        elif ord(z)==8:
            final+="Effacer = {} = ".format(z)
        elif ord(z)==9:
            final+="'Tab', 'Tabulation', '  ' ou ctrl+i= {} = ".format(z)
        elif ord(z)==13:
            final+="Retour à la ligne 'Entrer' = {} = ".format(z)
        elif ord(z)==72:
            final+="Précédé de '224 ou \\xe0' donne flèche du haut = {} = ".format(z)
        elif ord(z)==77:
            final+="Précédé de '224 ou \\xe0' donne flèche de droite --> = {} = ".format(z)
        elif ord(z)==75:
            final+="Précédé de '224 ou \\xe0' donne flèche de gauche <-- = {} = ".format(z)
        elif ord(z)==80:
            final+="Précédé de '224 ou \\xe0' donne flèche du bas = {} = ".format(z)
        elif ord(z)==81:
            final+="Précédé de '224 ou \\xe0' donne flèche saut vers le bas = {} = ".format(z)
        elif ord(z)==73:
            final+="Précédé de '224 ou \\xe0' donne flèche saut vers le haut = {} = ".format(z)
        elif ord(z)==59:
            final+="Précédé de '0 ou \\x00' donne F1 = {} = ".format(z)
        elif ord(z)==60:
            final+="Précédé de '0 ou \\x00' donne F2 non nécessaire pour '<' = {} = ".format(z)
        elif ord(z)==61:
            final+="Précédé de '0 ou \\x00' donne '=' ou F3 = {} = ".format(z)
        elif ord(z)==62:
            final+="Précédé de '0 ou \\x00' donne F4 non nécessaire pour '>' = {} = ".format(z)
        elif ord(z)==63:
            final+="Précédé de '0 ou \\x00' donne ? ou F5 ou '€<=>(chr(8364))' = {} = ".format(z)
        elif ord(z)==64:
            final+="Précédé de '0 ou \\x00' donne @ ou F6 = {} = ".format(z)
        elif ord(z)==65:
            final+="Précédé de '0 ou \\x00' donne F7 = {} = ".format(z)
        elif ord(z)==66:
            final+="Précédé de '0 ou \\x00' donne F8 = {} = ".format(z)
        elif ord(z)==67:
            final+="Précédé de '0 ou \\x00' donne F9 = {} = ".format(z)
        elif ord(z)==68:
            final+="Précédé de '0 ou \\x00' donne F10 = {} = ".format(z)
        elif ord(z)==69:
            final+="Précédé de '0 ou \\x00' donne F11 = {} = ".format(z)
        elif ord(z)==224 or ord(z)==134:
            final+="En entran 224 ou '\\xe0' ou 134 ou '\\x86' donne F12 = {} = ".format(z)
        elif ord(z)==71:
            final+="Petite flèche pointant vers le nord-ouest = {} = ".format(z)
        elif ord(z)==79:
            final+="Précédé de '224 ou \\xe0' donne bouton 'Fin' = {} = ".format(z)
        elif ord(z)==82:
            final+="Précédé de '224 ou \\xe0' donne bouton 'Inser' = {} = ".format(z)
        elif ord(z)==83:
            final+="Précédé de '224 ou \\xe0' donne bouton 'suppr' = {} = ".format(z)
        elif ord(z)==126:
            final+="Précédé de '0 ou \\x00' donne ~ = {} = ".format(z)
        elif ord(z)==231:
            final+="ç = {} = ".format(z)
        elif ord(z)==248:
            final+="° = {} = ".format(z)
        elif ord(z)==253:
            final+="² = {} = ".format(z)
        elif ord(z)==130:
            final+="é = {} = ".format(z)
        elif ord(z)==138:
            final+="è = {} = ".format(z)
        elif ord(z)==136:
            final+="ê = {} = ".format(z)
        elif ord(z)==131:
            final+="â = {} = ".format(z)
        elif ord(z)==132:
            final+="ä = {} = ".format(z)
        elif ord(z)==133:
            final+="à = {} = ".format(z)
        elif ord(z)==156:
            final+="£ = {} = ".format(z)
        elif ord(z)==207:
            final+="¤ = {} = ".format(z)
        elif ord(z)==151:
            final+="ù = {} = ".format(z)
        elif ord(z)==230:
            final+="µ = {} = ".format(z)
        elif ord(z)==245:
            final+="§ = {} = ".format(z)
        elif ord(z)==8364 or ord(z)==:
            final+="€ = {} = ".format(z)
        
        else:
            final+="{} =".format(z)
        final+="{}\n".format(code)
        final+="========================  Fin de la touche  ========================\n"
        print(final)
        final+="\nCréé par Henry Letellier\n"
        f=open("lettre.txt", "a")
        s=f.write(final)
        f.close()
