from time import sleep
import math
# import pygame
TV=" "
print ("Bienvenue dans le cripteur python")
a=input ("entrez votre mot à cripter:")
b=input ("entrez votre moyen de cryptage: -pour voir les options tapez h-")

if b=="m":
    ALPHABET = {'A': "._", 'B': '_...','C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..'}
    SEPARATEUR = "/"
    morse = []
    for car in a:
        if car == " " or car=="    ":
            morse.append("")
        elif car.upper() in ALPHABET:
            morse.append(ALPHABET[car.upper()])
    texteMorse = SEPARATEUR.join(morse)
    print(texteMorse)
# elif b=="lm":
#     a=input ("entrez votre mot à décrypter")
#     ALPHABET = {'._': 'A', '_...': 'B' , '_._.': 'C',  '_..': 'D', '.': 'E', '.._.': 'F', '__.': 'G', '....': 'H', '..': 'I', '.___': 'J', '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O', '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T', '.._': 'U', '..._': 'V', '.__': 'W', '_.._': 'X', '_.__': 'Y', '__..': 'Z'}
#     SEPARATEUR = "/"
#     morse = []
#     for car in a:
#         if car == " ":
#             morse.append("")
#         elif car.upper() in ALPHABET:
#             morse.append(ALPHABET[car.upper()])
#     texteMorse = SEPARATEUR.join(morse)
#     print(texteMorse)
elif b=="TV":
    ALPHABET = {'A': 'C', 'B': 'D','C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'}
    decal = 2
    for car in a:
        if car.upper() in ALPHABET:
            TV+=chr(((ord (a)-ord('a')-decal) %26)+ord('a'))#
        elif car.lower() in ALPHABET:
            TV+=chr((ord (a)-ord('A')-decal)  %26)#
        else:
            TV+=a
    print(TV)
elif b=="h":
    print (" Tapez m pour transformer du morse \n tapez lm pour convertir du  morese en lettre, TV pour convertir votre mot en code TV\n")
# print ("{}{}".format(a,b))