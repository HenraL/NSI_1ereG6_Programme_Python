from time import sleep
from random import randint
ask,jeu,Max="o","o",1000
while jeu=="o":
    secret,essai,etape=randint(0,Max),-1,0
    while essai!=secret:
        essai=int(input("Entrez un nombre inférieur à {}:".format(Max)))
        if essai<secret:
            print("c'est plus, recommencez!")
        elif essai>secret:
            print("c'est moin, recommencez!")
        etape+=1
    print("Bravo! Vous avez trouvé après {} étapes.".format(etape))
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