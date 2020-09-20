from random import*
from turtle import*
from statistics import mean
gerard=[1,55,67,67,7876654567,69,68,69,46654,'5654']
gerard.append("j'aime les bannanes")
print (gerard)
shuffle(gerard)
print (gerard)
gerard.reverse()
print (gerard)
ginette=gerard
print("vive ginette:", ginette)
print(gerard.index(69))
print(len(gerard))
print(gerard[4])
print("turtle")
goto(100,0)
goto(50,100)
goto(0,0)
goto(100,0)
goto(200,0)
goto(150,0)
notes=[0,12,17,20]
moyenne=mean(notes)
print(moyenne)

#======================== Turtle ===================================
#-------------------- ligne 120, angle 90, rouge, haut 80 ----------
forward(120)
left(90)
color('red')
forward(80)
#n=input(" ")

#------------------- fonc principale -------------------------------
#reset() on efface tout et on recommence
#goto(x,y) Aller à l'endroit de coordonnées x,y
#forward(distance) avancer d'une distance donnée
#backward(distance) reculer
#up() relever le crayon (pour pouvoir avancer sans dessiner)
#down() abaisser le crayon (pour pouvoir recommencer à dessiner)
#color(couleur) couleur peut être une chaine prédéfinie ('red', 'blue', 'green', etc)
#left(angle) tourner à gauche d'un angle donné (exprimmé en degré)
#right(angle) tourner à droite d'un angle donné
#width(épaisseur) choisir l'épaisseur du tracé
#fill(1) remplir un contour fermé à l'aide de la couleur sélectionnée
#write(texte) texte doit être une chaine de caractères délimité par des " ou des '
#circle(100) Trace un cercle de rayon 100

#----------------- rectangle bord rouge et bords noires --------------
reset()
for i in range(2):
    color('black')
    forward(120)
    left(90)
    color('red')
    forward(80)
    left(90)
#n=input(" ")

#----------------- triangle équilatéral --------------------------------
reset()
color('black')
forward(200)
left(120)
color('red')
forward(200)
left(120)
color('green')
forward(200)
right(120)

#n=input(" ")

#-------------------------- house ---------------------------------------
reset()
#main
forward(100)
left(90)
forward(80)
left(90)
forward(100)
left(90)
forward(80)
left(90)
#door
forward(20)
left(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
up()
#window
left(90)
forward(40)
left(90)
forward(60)
down()
circle(10)
up()
#roof
forward(20)
right(90)
forward(20)
left(135)
down()
forward(70)
left(90)
forward(70)
left(55)
up()
forward(200)
#n=input(" ")

#-------------- square spiral ------------------
reset()
a=10
for i in range(16):
    forward(a)
    left(90)
    forward(a)
    left(90)
    a+=10

#n=input(" ")

#-------------- criqued spiral -----------------
reset()
a=5
for i in range(25):
    forward(a)
    left(45)
    forward(a)
    left(45)
    a+=5

#n=input(" ")

#------------------ pipe ----------------------
reset()
a,x,y=20,0,0
for i in range(5):
    up()
    goto(x,y)
    down()
    circle(a)
    a+=20
    y-=2
    x+=20
#n=input(" ")
#------------------ eye ----------------------
reset()
a,x,y=20,0,0
for i in range(5):
    up()
    goto(x,y)
    down()
    circle(a)
    a+=20
    y-=2
#n=input(" ")
#------------------ target ----------------------
reset()
a,x,y=20,0,0
for i in range(5):
    up()
    goto(x,y)
    down()
    circle(a)
    a+=20
    y-=20
#n=input(" ")

#--------- module star wars ---------------
reset()
a=100
for i in range(6):
    for i in range(3):
        
        forward(a)
        left(30)
    left(30)
n=input(" ")
