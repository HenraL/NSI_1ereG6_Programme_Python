from time import sleep
from turtle import*
#import turtle
while ii<10000000:
    print ("left=90, forward=120, left=90")
    for i in range(2):
        color('black')
        forward(120)
        left(90)
        color('red')
        forward(80)
        left(90)
    sleep(1)
    reset()
    print ("a=10, left=90, left=90")
    a=10
    for i in range(a):
        forward(a)
        left(90)
        forward(a)
        left(90)
        a=a+10
    sleep(1)
    reset()
    print ("a=5, left=60, left=30")
    a=5
    for i in range(25):
        forward(a)
        left(60)
        forward(a)
        left(30)
        a=a+5
    sleep(1)
    reset()
    print ("a=5, left=45, left=30")
    a=5
    for i in range(25):
        forward(a)
        left(45)
        forward(a)
        left(30)
        a=a+5
    sleep(1)
    reset()
    print ("a=5, left=45, left=45")
    a=5
    for i in range(25):
        forward(a)
        left(45)
        forward(a)
        left(45)
        a=a+5
    sleep(1)
    reset()
    print ("a=5, left=30, left=30")
    a=5
    for i in range(25):
        forward(a)
        left(30)
        forward(a)
        left(30)
        a=a+5
    sleep(1)
    reset()
    print ("a=20, circle=a")
    a=20
    x=0
    y=0
    goto(0,0)
    for i in range(5):
        up()
        goto(x,y)
        down()
        circle(a)
        a=a+20
        y=y-20
    sleep(1)
    reset()
    
