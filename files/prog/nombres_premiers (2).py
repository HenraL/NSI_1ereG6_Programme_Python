from math import pi
a=float(input("Entrer la valeur a:"))
b=int(a)
print (type(a))
print (type(b))
while a>pi:
    a-=2*pi
print("float a={}".format(a))

while b>pi:
    b-=2*pi
print("int b={}".format(b))

y=1
z=int(input("combien de fois voulez-vous exécuter le program?:"))
x=int(input("De combien voulez-vous incrémenter a?"))
a=float(input("Entrer la valeur a:"))
z+=1
while y<z:
    print("Exécution n°{}.\na={}\nb={}".format(y,a,b))
    b=int(a)
    print (type(a))
    print (type(b))
    while a>pi:
        a-=2*pi
    print("float a={}".format(a))

    while b>pi:
        b-=2*pi
    print("int b={}".format(b))
    y+=1
    a+=x
