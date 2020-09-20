import math, time, turtle, random
i="n"
e=f=0
d=c=g=" "
In=1
# t = turtle.Turtle()
l=l1=l2=l3=a1=50
a2=a3=60
if i=="n" or i=="N":
    print ("(rc) recette de cuisine, (ce) cercle, (t) triangle, (o) octogone, (ca) caré, (r) rectangle, (fa) forme aléatoire, (ex) exemple de forme, (s) sortir")
    a=input("que voulez-vous faire?:")
    if a=="rc":
        print ("rc")
        b=input("Voulez-vous créé une recette de cuisine? [(o)ui/(n)on]:")
        if b=="o":
            d=input("Nomez votre création culinaire?: ")
            e=int(input("Combien d'ingrédients a-t-elle? "))
            print ("Nous allons maintenant vous demander à la file les ingrédients que vous souhiatez mettre.")
            while f<e:
                g+=input ("Quel est votre ingrédient N°{}? ".format(In))
                g+=", "
                f+=1
                In+=1
            print ("Votre Recette de cuisine se nome {} et elle contient {} ingrédient(s), les ingrédients sont {}".format(d,f,g))
        elif b=="n":
            d=input("Quel recette de cuisine allez-vous donc réalisée:")
            e=int(input("Combien d'ingrédients a-t-elle? "))
            while f<e:
                g+=input ("Quel est votre ingrédient N°{}? ".format(In))
                g+=", "
                f+=1
                In+=1
            print ("Votre Recette de cuisine est {} et elle contient {} ingrédient(s), les ingrédients sont {}".format(d,f,g))
    elif a=="ce":
        # t = turtle.Turtle()
        print ("ce")
        turtle.circle
    elif a=="t":
        print ("t")
        T=input("Quel triangle voulez-vous déssiner? [(te) triangle équilatéral, (ti) triangle isocèle, (tq) triangle quelconque, (tr) triangle rectangle] : ")
        if T=="te" or T=="TE" or T=="Te" or T=="tE":
            # t = turtle.Turtle()
            print ("te")
            l=int(input("Quel sera la longuere des cotés de votre triangle équilatéral (longueure exprimée en cm): "))
            # turtle.pendown()
            # t.home
            # t.forward()
            # t.left(50)
            # t.forward()
            # t.left(50)
            # t.forward(75)
            # t.left(50)
            # t.penup()
        elif T=="ti" or T=="TI" or T=="Ti" or T=="tI":
            # t = turtle.Turtle()
            print ("ti")
            l=int(input("Quel sera la longuere des cotés de votre triangle équilatéral (longueure exprimée en cm): "))
            # turtle.pendown()
            # t.home()
            # t.forward(75)
            # t.left(50)
            # t.forward(75)
            # t.left(50)
            # t.forward(75)
            # t.left(50)
            # t.penup()
        elif T=="tq" or T=="TQ" or T=="Tq" or T=="tQ":
            # t = turtle.Turtle()
            print ("tq")
            l1=int(input("Quel sera la longuere du premier coté de votre triangle quelconque (longueure exprimée en cm): "))
            l2=int(input("Quel sera la longuere du deuxième coté de votre triangle quelconque (longueure exprimée en cm): "))
            l3=int(input("Quel sera la longuere du troisième coté de votre triangle quelconque (longueure exprimée en cm): "))
            print (" ")
            a1=int(input("Quel est votre premier angle (en degré -max 90°-) : "))
            a2=int(input("Quel est votre second angle (en degré -max {}°) : ".format(90-a1)))
            a3=int(input("Quel est votre troisième angle (en degré -max {}°) : ".format(90-(a1+a2))))
            # turtle.pendown()
            # t.home()
            # t.forward(75)
            #t.left(50)
            #t.forward(75)
            #t.left(50)
            #t.forward(75)
            #t.left(50)
            #t.penup()
        elif T=="tr" or T=="TR" or T=="Tr" or T=="tR":
            # t = turtle.Turtle()
            print ("tr")
            l1=int(input("Quel sera la longuere du premier coté de votre triangle quelconque (longueure exprimée en cm): "))
            l2=int(input("Quel sera la longuere du deuxième coté de votre triangle quelconque (longueure exprimée en cm): "))
            l3=int(input("Quel sera la longuere du troisième coté de votre triangle quelconque (longueure exprimée en cm): "))
            print (" ")
            a1=int(input("Quel est votre premier angle (en degré -max 90°-) : "))
            a2=int(input("Quel est votre second angle (en degré -max {}°) : ".format(90-a1)))
            a3=int(input("Quel est votre troisième angle (en degré -max {}°) : ".format(90-(a1+a2))))
            turtle.pendown()
            t.home()
            t.forward(l1)
            t.left(a1) 
            t.forward(75)
            t.left(50)
            t.forward(75)
            t.left(50)
            t.penup()
        # else:
        #     continue

    elif a=="o":
        print ("o")
    elif a=="ca":
        print ("ca")
    elif a=="r":
        print ("r")
    elif a=="fa":
        print ("fa")
    elif a=="ex":
        import turtle
        t = turtle.Turtle()
        print ("bienvenue dans l'exemple")
        sleep (1)
        print ("La forme qui va être déssiner est un octogone qui se termine en cercle noir.")
        t.pendown()
        for c in ['red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen','red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen']:
            t.color(c)
            t.forward(75)
            t.left(50)
        sleep (5)
        t.penup()
    elif a=="S" or a=="s":
        i=input ("Terminer le programme? [(o)ui/(n)non] :")
    else:   
        i=input ("Terminer le programme? [(o)ui/(n)non] :")
else:
    print ("au revoir")