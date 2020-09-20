from time import sleep
a=int(input("Entrer a:"))
b=int(input("Entrer b:"))
texte="PGCD({};{})=".format(a,b)
while (a!=b):
    if a>b: a=a-b
    else: b=b-a
print(texte+str(a))
sleep(3)