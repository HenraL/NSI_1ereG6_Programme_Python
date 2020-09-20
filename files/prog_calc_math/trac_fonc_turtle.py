import math
from fractions import *
import turtle
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
            print("x0=",x0)
            print (" ")
            sleep (2)
            print ("Créé par Henry Letellier")
        elif delta>0:
            # xone=-b-(rac)
            # xtwo=-b+(rac)
            print ("-b-√∆/2*a\n-b+√∆/2*a\n ||\n ||\n\||/\n \/\n-(",b,")-√",delta,"/","2*",a,"\n-(",b,")+√",delta,"/","2*",a)
            # print (r)
            r=math.sqrt(delta)
            x1_1=-b-r
            x1_2= 2*a
            x2_1=-b+r
            x2_2= 2*a
            print ("x1=",x1_1,"/",x1_2, "et x2=", x2_1,"/",x2_2)
            sleep (2)
            print ("Créé par Henry Letellier")
	    t = turtle.Turtle()
	    t.clear()
            t.reset()
            t.penup()
            t.goto(100, 100)
            print(t.eading())
        delt=int(input("Calculer un autre delta (2) oui, (1) non: "))
        if delt==1:
            break
        elif delt==2:
            continue

turtle.clear()
turtle.reset()
turtle.forward(turtle.window_width()/3)
turtle.backward(turtle.window_width()/2)
turtle.bk(50)
turtle.fd(0)
