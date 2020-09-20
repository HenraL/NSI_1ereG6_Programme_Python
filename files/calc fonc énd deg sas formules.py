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
    delta=(b*b)-4*(a*c)
    print ("delta =",delta)
    if delta<0:
        print ("Pas de solution possible")
        print ("Merci de tenter une autre fonction")
        sleep (2)
        print ("Créé par Henry Letellier")
    elif delta==0:
        x0=-b/(2*a)
        print("x0=",x0)
        print (" ")
        sleep (2)
        print ("Créé par Henry Letellier")
    elif delta>0:
        rac=math.sqrt(delta)
        x1=(-b-(rac))/(2*a)
        x2=(-b+(rac))/(2*a)
        print ("x1=", x1, "et x2=", x2)
        sleep (2)
        print ("Créé par Henry Letellier")
    i=int(input("continuer? (0) oui, (1) non: "))
