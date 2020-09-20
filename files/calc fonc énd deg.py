import math
from time import sleep
O=0
o=0
i=0
n=1
while i==o or i==O or i==0:
    a=int(input("Entrer a:"))
    b=int(input("Entrer b:"))
    c=int(input("Entrer c:"))
    print(" ")
    print("f(x)=",a,"x²+",b,"x+",c)
    print("\n(delta)=b²-4(ac)")
    delta=(b*b)-4*(a*c)
    print ("delta =",delta)
    if delta<0:
        print ("Pas de solution possible")
        print ("Merci de tenter une autre fonction")
        sleep (2)
        print ("\n°   °")
        print ("  |  ")
        print (" ___ ")
        print ("""/   \\\'""")
        print ("snif!")
        print ("Créé par Henry Letellier")
    elif delta==0:
        print ("delta = 0 ==> -b/2a")
        x0=-b/(2*a)
        print("x0=",x0)
        print (" ")
        sleep (2)
        print ("\n°   °")
        print ("  |  ")
        print ("\\___/")
        print ("Yes!")
        print ("Créé par Henry Letellier")
    elif delta>0:
        rac=math.sqrt(delta)
        print("x1=-b-racine(delta)/2*a\n")
        x1=(-b-(rac))/(2*a)
        print("x2=-b+racine(delta)/2*a\n\n")
        x2=(-b+(rac))/(2*a)
        print ("x1=", x1, "et x2=", x2)
        sleep (2)
        print ("\n°   °")
        print ("  |  ")
        print ("\\___/")
        print ("Yes!")
        print ("Créé par Henry Letellier")
    i=int(input("continuer? (0) oui, (1) non: "))
    if i==o or i==O or i==0:
        print ("réanitialisation des variables")
        sleep (0.5)
        a=0
        sleep (0.5)
        b=0
        sleep (0.5)
        c=0
        sleep (0.5)
        d=0
        sleep (0.5)
        delta=0
        sleep (0.5)
        x0=0
        sleep (0.5)
        x1=0
        sleep (0.5)
        x2=0
        sleep (0.5)
        print ("Les variables on étées réanitialisées")
        sleep (1)
    elif i==n or i==1:
        print ("Au revoir")
        print ("\n°   °")
        print ("  |  ")
        print ("\\___/")
        print ("Créé par Henry Letellier")
        print ("votre résultat était",delta)


#revue.sesamath.net/spip.php?article1260
