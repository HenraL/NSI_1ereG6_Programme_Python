import math
from fractions import *
import turtle
from time import sleep

o=t=tac=delt=b=a=c=f(x1)=0
O=o=quest=delt=delta=sub=can=rest=x1x2=x1=x1_1=x1_2=x2_1=x2_2=b=a=c=xone=xtwo=x=cant=O=o=1
i=0
n=3
oo=OO=00
tac=f(x2)-f(x1)/x1-x2


while t==0:
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
        rae=a((x-(α))*(x-(α)))+β
    elif -(α)<0:
        print ("Le résultat de la forme canonique est",a,"(x",-(α),")²",+β)
        rae=a((x-(α))*(x-(α)))+β
    f(x1)=rae
    tac=f(x2)-f(x1)/x1-x2
    print ("Le Taux d'accroisssement est : ", tac)
    t=int(input("Voulez-vous calculer un nouveau taux d'accroissement?: (O)ui/(n)on "))






#    f(x2)-f(x1)/x1-x2
#    f(x1) dépend de de la forme cannonique.