from time import sleep
from tkinter import *
import os, platform
#from tkinter import ttk
time=input("voulez-vous que le minuteur fasse : décomp d'heures (dh), de minutes (mn), décomp d'heures en affichant les minutes (hm), afficher les secodes? (as), afficher heures minutes et secondes (t)")
i=60

if time=="T" or time=="t":
    i=input("Veuillez entrer votre temps en heures (temps par défaut 1 heure):")
    if i=="" or i==" ":
        i=1
    else:
        i=float(str(i))
elif time=="DH" or time=="Dh" or time=="dH" or time=="dh":
    i=input("Veuillez entrer votre temps (temps par défaut 1 heure):")
    if i=="" or i==" ":
        i=1
    else:
        i=float(str(i))
elif time=="MN" or time=="Mn" or time=="mn" or time=="mN":
    i=input("Veuillez entrer votre temps (temps par défaut 1 minute):")
    if i=="" or i==" ":
        i=1
    else:
        i=float(str(i))
elif time=="HM" or time=="Hm" or time=="hm" or time=="hM":
    i=input("Veuillez entrer votre temps (temps par défaut 1 heure):")
    if i=="" or i==" ":
        i=1
    else:
        i=float(str(i))
elif time=="AS" or time=="As" or time=="as" or time=="aS":
    i=input("Veuillez entrer votre temps (temps par défaut 1 minute):")
    if i=="" or i==" ":
        i=1
    else:
        i=float(str(i))

print ("Votre temps: {}".format(i))
if time=="DH" or time=="Dh" or time=="dH" or time=="dh":
    while i>0:
        print ("Il reste {} heure(s)".format(i))
        sleep(3600)
        i+=-1
elif time=="MN" or time=="Mn" or time=="mn" or time=="mN":
    while i>0:
        print ("Il reste {} minute(s)".format(i))
        sleep(60)
        i+=-1
elif time=="HM" or time=="Hm" or time=="hm" or time=="hM":
    while i>0:
        m=60
        while m>0:
            print ("Il reste {} heure(s) {} minute(s)".format(i, m))
            sleep(60)
            m+=-1
        i+=-1
elif time=="AS" or time=="As" or time=="as" or time=="aS":
    while i>0:
        s=60
        while s>0:
            print ("Il reste {} minute(s) {} seconde(s)".format(i, s))
            sleep(1)
            s+=-1
        i+=-1
elif time=="AS" or time=="As" or time=="as" or time=="aS":
    while i>0:
        s=60
        while s>0:
            print ("Il reste {} minute(s) {} seconde(s)".format(i, s))
            sleep(1)
            s+=-1
        i+=-1
elif time=="T" or time=="t":
    while i>-1:
        m=60
        while m>0:
            s=60
            while s>0:
                print ("Il reste {} heure(s) {} minute(s) {} seconde(s)".format(i, m, s))
                sleep(1)
                s+=-1
            m+=-1
        i+=-1
while i>0:
    print ("Il reste {} minutes".format(i))
    sleep(60)
    i+=-1
print("\nLe temps est écoulé")
print ( "                    *==============================================================================================================*                    \n                      |                              @@         @@                                                                  |                    \n                      |                             @@         @@                                                                   |                    \n                      |                            @@         @@                                                                    |                    \n                      |                                                                                                             |                    \n                      |      @@@@@@@@   @@@@@@   @@@@@@@@  @@@@@@@@              @@@@@@@@      @@        @@@@@@@@@                  |                    \n                      |      @@        @      @  @@        @@                   @@       @    @  @       @@       @                 |                    \n                      |      @@        @      @  @@        @@                   @@       @   @    @      @@       @                 |                    \n                      |      @@        @@@@@@@   @@@@@@@@  @@@@@@@@             @@@@@@@@@   @@@@@@@@     @@@@@@@@@                  |                    \n                      |      @@        @  @      @@        @@                   @@         @        @    @@    @                    |                    \n                      |      @@        @   @     @@        @@                   @@        @          @   @@     @                   |                    \n                      |      @@@@@@@@  @    @    @@@@@@@@  @@@@@@@@             @@       @            @  @@      @                  |                    \n                      |                                                                                                             |                    \n                      |              @@       @@  @@@@@@@@@  @@      @@  @@@@@@@@   @@       @@                                     |                    \n                      |              @@       @@  @@         @@@     @@  @@       @  @@     @@                                      |                    \n                      |              @@       @@  @@         @@ @    @@  @@       @   @@   @@                                       |                    \n                      |              @@@@@@@@@@@  @@@@@@@@@  @@  @   @@  @@@@@@@@@     @@ @@                                        |                    \n                      |              @@       @@  @@         @@   @  @@  @@    @        @@@                                         |                    \n                      |              @@       @@  @@         @@    @ @@  @@     @       @@                                          |                    \n                      |              @@       @@  @@@@@@@@@  @@     @@@  @@      @     @@                                           |                    \n                      |                                                                                                             |                    \n                      |      @@         @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@         @@         @@@@@@@@   @@@@@@@  @@@@@@@@      |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@       @    |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@       @    |                    \n                      |      @@         @@@@@@@@      @@       @@@@@@@@@@@  @@         @@            @@      @@@@@@@  @@@@@@@@@     |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@   @        |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@    @       |                    \n                      |      @@@@@@@@@  @@@@@@@@      @@       @@@@@@@@@@@  @@@@@@@@@  @@@@@@@@@@ @@@@@@@@   @@@@@@@  @@     @      |                    \n                     .=============================================================================================================.                     ")
sleep(1)
print("\n*Créé par Henry Letellier")
try:
    Temps=Tk()
    Temps.title("Temps écoulé")
    Temps.geometry("300x100")
    Button(Temps, text="Ok", command=Temps.destroy).pack(padx=10, pady=10)
except:
    if platform=="windows":
        try:    
            os.system("""cmd/c "message.vbs" """)
        except:
            message="""x=MSgbos("Le temps est écoulé",0+64+4096,"Timer.py")"""
            f=open("message.vbs", "w")
            s=f.write(message)
            f.close()
            os.system("""cmd/c "message.vbs" """)
    elif platform=="mac":
        os.system("say Times UP!")
        os.system("""alert "Temps écoulé" """)
    elif platform=="Linux":
        os.system("alert 'Temps écoulé'")
sleep(5)
#macos mojave
