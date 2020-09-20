import os, platform
from time import sleep
if platform.system()=="Windows":
    h="o"
    def pause():
        os.system("pause")
    def clear():
        os.system("cls")
    def Start():
        os.system("echo off")
        os.system("color 0A")
        clear()
    Start()
    print("Exécuter\nenter\nshell:startup\ncopie et colle ça dans l'explorateur pour accéder au fichier {}\nPour stopper faire ctrl+c".format(os.getcwd()))
    choice=input("Continuer? [(o)ui/(n)on]:")
    while h=="o":
        if choice=="o" or choice=="O" or choice=="0":
            print("  ___   ___  \n /   \_/   \ \n \         / \n  \ Irina /  \n   \     /   \n    \   /    \n     \_/     ")
            sleep(0.05)
            clear()
        elif choice=="n" or choice=="N":
            print("Au revoir")
            sleep(1)
            print("Créé par Henry Letellier")
            sleep(1)
            pause()
            pause()
            h="n"
        else:print("assurez-vous de ne rentrer que 'o' pour oui ou 'n' pour non")
else:
    print("merci d'éxécuter ce programe sous windows")
    sleep(5)
