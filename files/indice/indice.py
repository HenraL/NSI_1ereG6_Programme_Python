from math import sqrt
from time import sleep
U=int(input("Entrez votre nombre:"))
while U!=0:
    print("Pour le nombre {}, sa racine est égale à {}".format(U,sqrt(U)))
    U-=1
sleep(20)
print("créé par henry Letellier")
sleep(5)
