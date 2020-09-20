from random import randint
from time import sleep
ask,jeu,Max,total_etapes,nbr_jeux, etape="o","o",1000,0,0,0
while jeu=="o":
    nbr_jeux+=1
    secret,essai,etape=randint(1,Max),-1,0
    print("Un nombre entre 1 et {} a été choisi\n(entrer 0 arrête le jeu)".format(Max))
    while essai!=secret:
        essai=int(input("Entrez un nombre:"))
        if essai==0: break
        if essai<secret: print("C'est plus, recommencez!")
        elif essai>secret: print("C'est moins, recommencez!")
        etape+=1
    if essai==0: break
    else:
        print("Bravo! Vous avez trouvé après {} étapes".format(etape))
        total_etapes+=etape
    while ask=="o":
        jeu=input("Voulez-vous rejouer? [(o)ui/(n)on]:")
        if jeu=="o" or jeu=="O" or jeu=="0" or jeu==0:
            jeu,ask="o","n"
        elif jeu=="n" or jeu=="N":
            ask,jeu="n","n"
        else:
            print("Veuillez entrer o pour oui ou n pour non. Vous avez entré: {}".format(jeu))
            ask=="o"
            continue 
if essai==0: print("Partie interrompue. A bientôt.")
else:
    print("Vous avez joué {} fois. Merci!\nScore moyen: {}".format(nbr_jeux,total_etapes/nbr_jeux))
    sleep(3)
