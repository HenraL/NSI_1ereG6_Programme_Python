import subprocess, math, fractions, turtle, sys, os#, pygame
#os.system("pause")
# import pdb
from time import sleep
Ub=m=1
Un=w=2
D=l=3
try:
  #  pygame.display.set_icon(pygame.image.load("math_croped.png"))
  print ("hi")
except:
    print ("Il m'est imossible de trouver l'icône, êtes-vous sûr d'avoir tout téléchargé de ce rojet?")
    print ("Êtes-vous sûre d'avoir téléchargé pygame?")
    os=int(input("Quel Ordinateur avez-vous? (m)ac, (w)indows, (l)inux"))
    if os==1:
        print ("Pour mac rendez-vous sur pygame, release notes")
    elif os==2:
        print ("Pour le télécharger sur pc, dans le menu démaré, tapez 'cmd.exe' puis python3 -m pip install -U pygame, une fois cela fait, vous pouvez fermer la fenêtre et relancer le programme.")
    elif os==3:
        lin=int(input("Quelle plateforme de linux avez-vous? (Ub)untu, (Un)ix, (D)ebian"))
        if lin==1:
            print ("Pour Linux, Ubuntu, ouvrez le terminal, tapez ..., attendez que cela se finisse, vous pouvez éxécuter le programme")
        elif lin==2:
            print ("Pour Linux, Unix, ouvrez le terminal, tapez ... attendez que cela se finisse, vous pouvez éxécuter le programme")
        elif lin==3:
            print ("Pour Linux, Debian, ouvrez le terminal, tapez ... attendez que cela se finisse, vous pouvez éxécuter le programme")
O=o=quest=delt=delta=sub=can=rest=x1x2=x1=x1_1=x1_2=x2_1=x2_2=b=a=c=xone=xtwo=x=cant=O=o=1
i=0
n=3
oo=OO=00
# delta=(b*b)-4*(a*c)
# α=Fraction(-b,2*a)
# β=Fraction(-(delta),4*a)
while i==o or i==O or i==0:
    quest=int(input("Que voulez-vous calculer? delta (2), forme canonique (3), x0 (4), x1, x2 (5): "))
    while delt==2 or quest==2:
        a=int(input("Entrer a:"))
        b=int(input("Entrer b:"))
        c=int(input("Entrer c:"))
        delta=(b*b)-4*(a*c)
        print ("∆=",delta)
        if delta<0:
            print ("Pas de solution possible")
            print ("Merci de tenter une autre fonction")
            sleep (2)
            print ("Créé par Henry Letellier")
        elif delta==0:
            x=Fraction(-b,(2*a))
            print ("x0=",x)
            x0=-b/(2*a)
            print("x0=",x0, "\n")
            print ("Créé par Henry Letellier")
        elif delta>0:
            # xone=-b-(rac)
            # xtwo=-b+(rac)
            print ("-b-√∆/2*a\n-b+√∆/2*a\n ||\n ||\n\||/\n \/\n-({})-√{}/2*{}\n-({})+√{}/2*{}".format(b,delta,a,b,delta,a))
            # print (r)
            r=math.sqrt(delta)
            x1_1=-b-r
            x1_2= 2*a
            x2_1=-b+r
            x2_2= 2*a
            print ("x1={}/{}et x2={}/{}".format(x1_1,x1_2,x2_1,x2_2))
            sleep (2)
            print ("Créé par Henry Letellier")
        delt=int(input("Calculer un autre delta (2) oui, (1) non: "))
        if delt==1:
            break
        elif delt==2:
            continue
        # else:2
        #     continue

    while quest==3 or can==3:
        print ("La forme canonique se sert de la fonction du 2nd degré.\n Pour pouvoir la calculer on prend le a, le b et le c de la fonction de degré 2.\n C'est à dire: f(x)=ax²+bx+c.")
        a=int(input("Entrer a:"))
        b=int(input("Entrer b:"))
        c=int(input("Entrer c:"))
        print ("On calcule delta")
        print ("∆=b²-4(a*c)")
        print ("∆=",b,"²","-4(",a,"*",c,")")
        delta=(b*b)-4*(a*c)
        print ("∆=", delta)
        print ("Forme canonique:\n a(x-α)²+β")
        print ("\n α=-b/2a\n β=-∆/4a \n β=-(b²-4(ac))/4a")
        α=Fraction(-b,2*a)
        β=Fraction(-(delta),4*a)
        if -(α)>=0:
            print ("Le résultat de la forme canonique est",a,"(x+",-(α),")²",+β)
        elif -(α)<0:
            print ("Le résultat de la forme canonique est",a,"(x",-(α),")²",+β)
        quet=int(input("voulez-vous-calculer une nouvelle forme canonique?: (0) oui (1) non "))
        if quet==1:
            break
        elif quet==0:
            continue

    while sub==4 or sub==5 or quest==4 or quest==5:
        needdelt=int(input("Quel est votre delta: "))
        while quest==4 or quest==5 or cant==000:
            if delta==0:
                x0=-b/(2*a)
                print("x0=",x0)
                print (" ")
                sleep (2)
                print ("Créé par Henry Letellier")
                cant=int(input("calculer un nouveau x0?: (000) oui, (22) non."))
            elif needdelt>0:
                print ("Votre delta est supérieur à 0 vous devriez tenter de calculer x1 et x2.")
                x1x2=int(input("Voulez-vous calculer x1 et x2: (0) oui (22) non"))
                if x1x2==4 or x1x2==0 or quest==5:
                    print ("-b-√∆/2*a\n-b+√∆/2*a\n ||\n ||\n\||/\n \/\n-(",b,")-√",delta,"/","2*",a,"\n-(",b,")+√",delta,"/","2*",a)
                    r=math.sqrt(delta)
                    x1_1=-b-r
                    x1_2= 2*a
                    x2_1=-b+r
                    x2_2= 2*a
                    print ("x1=",x1_1,"/",x1_2, "et x2=", x2_1,"/",x2_2)
                    sleep (2)
                    print ("Créé par Henry Letellier")
                    x1x2=int(input("Voulez-vous calculer un autre x1, x2?: (O) oui, (n) non:")
                    # if x1x2==0:
                    #     print ("Et c'est reparti ;-) !")
                    #     continue
                    # elif x1x2==1:
                    #     print ("On retourne au début")
                    #     break
                # elif x1x2==22:
                #     break
           # elif needdelt<0:
           #     print ("Votre delta est inférieur à 0, il est impossible de calculer x0, x1 ou x2.")
           #     rest=int(input("Voulez-vous redémarer?: (o) oui (n) non"))
    #             if rest==o :
    #                 print ("On redémare")
    #             elif rest==n :
    #                 print ("On retourne au début")
    #                 break
    #         elif rest==n:
    #             break
    #     if rest==n:
    #         break
    # if rest==n:
    #     break

        )
        sub=int(input("Voulez-vous calculer un autre x?: (3) oui, (2) non"))
    if delt==1 or x1==22 or sub==22 or can==22 or rest==n or delt==1:
        i=int(input("continuer? (0) oui, (1) non: "))
    if i==0:
        continue
    elif i==1:
        print ("sources:")
        sleep(1)
        print ("library fraction: https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Fractions_en_Python")
        sleep (1)
        print ("au revoir")
        break


# calculer du binaire
# calculer de l'hexadécimal
# calculer de l'octet
# calculer des bases de 10
# calculer des bases de 16
# calculer des puissances
# det Taux d'accroissement
# fact fonc
# det im de ...
# trac courbe
# rep graph de fonc
# calc aires
