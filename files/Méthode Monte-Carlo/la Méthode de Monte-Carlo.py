from turtle import*
from random import*
from math import*
speed(10)
S,N,i=0,random(),0
pensize(width=4)
#N=int(N)
penup()
def set_pixel(x,y):
    setx(int(200*x))
    sety(int(200-200*y))
def point_red(x,y):
    pencolor("red")
    set_pixel(x,y)
    pendown()
    dot(5)
    penup()
def point_blue(x,y):
    pencolor("blue")
    set_pixel(x,y)
    pendown()
    dot(5)
    penup()

while i<N+1:
    x,y=random(),random()
    if hypot(x, y)<1:
        S+=1
        point_red(x,y)
    else:
        point_blue(x,y)
