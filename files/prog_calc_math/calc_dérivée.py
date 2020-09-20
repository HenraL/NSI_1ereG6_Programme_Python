import subprocess, math, turtle, fractions
from time import sleep

num=1
# color1=color2=color3=color4=color5=color6=color7=color8=color9=color10=input("red")
# # or num==-num
# # t = turtle.Turtle()
# a=int(input("Entrer a:"))
# b=int(input("Entrer b:"))
# c=int(input("Entrer c:"))
# # fonc=a*(x**2)+(b*x)+c
print ("Pour avoir un exemple de ce que va faire ce programme, tapez 0.")
num=int(input("Combien de courbes voulez-vous déssiner?: (de 1 à 10 -si 0 ou que rien n'est mis, la valeur est automatiquement égale à 1-)"))
if num==1:
    color=input("choississez la couleure de votre courbe en anglais: (blue, green, orange, ...)")

    t = turtle.Turtle()

    for c in [color1]:
        t.color(c)
        t.forward(75)
        t.left(50)
    t.penup()
    t.forward(85)
    t.pendown()

    sleep(5)

# elif num==2:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==3:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==4:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color4=input("choississez la quatrième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3, color4]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==5:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color4=input("choississez la quatrième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color5=input("choississez la cinquième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3, color4, color5]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==6:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color4=input("choississez la quatrième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color5=input("choississez la cinquième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color6=input("choississez la sixième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3, color4, color5, color6]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==7:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color4=input("choississez la quatrième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color5=input("choississez la cinquième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color6=input("choississez la sixième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color7=input("choississez la septième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3, color4, color5, color6, color7]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==8:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color4=input("choississez la quatrième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color5=input("choississez la cinquième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color6=input("choississez la sixième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color7=input("choississez la septième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color8=input("choississez la huitième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3, color4, color5, color6, color7, color8]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==9:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color4=input("choississez la quatrième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color5=input("choississez la cinquième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color6=input("choississez la sixième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color7=input("choississez la septième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color8=input("choississez la huitième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color9=input("choississez la neuvième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3, color4, color5, color6, color7, color8, color9]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
# elif num==10:
#     color1=input("choississez la première couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color2=input("choississez la deuxième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color3=input("choississez la troisième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color4=input("choississez la quatrième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color5=input("choississez la cinquième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color6=input("choississez la sixième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color7=input("choississez la septième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color8=input("choississez la huitième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color9=input("choississez la neuvième couleure de votre courbe en anglais: (blue, green, orange, ...)")
#     color10=input("choississez la dixième couleure de votre courbe en anglais: (blue, green, orange, ...)")
    
#     t = turtle.Turtle()
    
#     for c in [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10]:
#         t.color(c)
#         t.forward(75)
#         t.left(50)
#     t.penup()
#     t.forward(85)
#     t.pendown()
    
#     sleep(5)
elif num==0:
    subprocess.call("start prog2.py")
    # subprocess.call("start python turtle_test.py")