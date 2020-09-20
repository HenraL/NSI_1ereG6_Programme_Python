import time, math
w="Créé par Henry Letellier"
w_e="""\n°   °\n  |  \n\\___/"""
a=input("Tapez (q) ici pour quitter\nQuel programme voulez-vous calculer? [(ex1), (ex2), (ex3)] :")
if a=="ex1" or "EX1":
    print ("ex1")
    print ("Temp 1")
    j_1=input("voulez-vous entrer un jour (3 max): ")
    h_1=input("Veuillez les heure(s): ")
    m_1=input("Veuillez entrer les minute(s): ")
    s_1=input("veuillez entrer les seconde(s): ")
    print ("\nTemp 2")
    j_2=input("voulez-vous entrer un jour (3 max): ")
    h_2=input("Veuillez les heure(s): ")
    m_2=input("Veuillez entrer les minute(s): ")
    s_2=input("veuillez entrer les seconde(s): ")
    if h_1<25 and h_2<25:
        if m_1<61 and h_2<61:
            if s_1<61 and s_2<61:
                b=j_1+j_2
                c=h_1+h_2
                d=m_1+m_2
                e=s_1+s_2
                print ("Toutes les variables ont été vérifiées, on peut commencer.")
                print ("je vais ajouter les heures avec les heures, les minutes avec les minutes, les secondes avec les secondes")
                print ("j_1+j_2={}; h_1+h_2={}; m_1+m_2={}; s_1+s_2={}".format (b, c, d, e))
                print
            else:
                print ("Êtes-vous sûre d'avoir respecté le format de 24 heures, 60 minutes, 60 secondes?")
        else: 
            print ("Êtes-vous sûre d'avoir respecté le format de 24 heures, 60 minutes, 60 secondes?")
    else:
        print ("Êtes-vous sûre d'avoir respecté le format de 24 heures, 60 minutes, 60 secondes?")

elif a=="ex2" or a=="EX2":
    print ("ex2")
elif a=="ex3" or a=="EX3":
    print ("ex3")
elif a=="q" or a=="Q":
    print (" Au revoir.\n {}{}".format(w, w_e))
    exit()
else:
    print ("Veulliez n'entrer uniquement ex1 ou ex2 ou ex3 ou q")