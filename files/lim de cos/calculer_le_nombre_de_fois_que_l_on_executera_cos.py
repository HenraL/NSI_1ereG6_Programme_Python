#Créé par Henry letellier
#le 06/01/2020 à 17h15
from time import sleep
from math import *
cont="o"
while cont=="o":
    i,a=0,int(input("Entrez a:"))
    while a!=0.7390851332151607:
        a=cos(a)
        i+=1
        print("cos(a)={}, nombre de fois que l'on a fait cos={}".format(a,i))
    print ("Créé par Henry Letellier\n\n\n\n")
    sleep(5)
    contt=input("continuer? [(o)ui/(n)on]")
    if contt=="o":
        cont="o"
    elif contt=="n":
        cont="n"
        print("Au revoir")
        sleep(2)
    else:print("assurez-vous d'avoir entré soit o pour oui ou n pour non")
