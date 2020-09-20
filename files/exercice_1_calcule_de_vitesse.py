import math
from time import sleep
I="O"
#round(number, ndigits=2)
# w="Créé par Henry Letellier"
# w_e="""\n°   °\n  |  \n\\___/"""
print ("Bienvenue dans le programme de calcul d'années ou de dates")
# sleep (2)
# while I=="o" or I=="O":
#     main=input("Commencer [(O)ui/(Q)uitter]:")
#     # if main=="Q" or main=="q":
    #     print ("Au revoir\n{}{}".format(w, w_e))
    #     sleep(2)
    #     break
    # elif main=="o" or main=="O" or main==0:
speed=e=input("Donnez-moi votre vitesse (en km/h):")
        # print("encore une fois")
        # e=int()
        # print (speed, e)
num=str.isnumeric(speed)
        # print (speed, e)
if num==True:
    speed*=1000
    d=speed*30
    c=30/3600
    b=round(c, ndigits=2)
    print ("True\nPour convertir une vitesse de km/h à m/s, Il faut:\n- multiplier 'votre nombre' par 1000\n- diviser ce résultat par 3600 (ce qui donne un résultat en mètres)\n- arrondire ce résultat à deux chiffres après la virgule\n Vous avez votre résultat en m/s.\n\n\n\nLe programme n'est pas terminé")
    # sleep(2)
    print ("Convertissons-là:\n- {}*1000={}\n- {}/3600={}\n- round({}, ndigits=2)={}\n\n\n\n Votre résultat est {}".format(e, e*1000, e*1000, c, c, b, b))
    # continue
elif num==False:
    print ("False\nMercie de vérifier que vous n'avez pas mis de virgules dans votre réponse car ce programme n'est pas fait pour calculer des nombres à virgule")
    # continue
