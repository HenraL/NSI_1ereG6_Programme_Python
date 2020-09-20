from math import sqrt
from time import sleep
def stats(tableau):
    n=len(tableau) #on mesure la taille du tableau
    m=sum(tableau)/n # on calcule la moyenne
    tableau2=[(x-m)**2 for x in tableau] #on crée le tableau des carrés des écarts à la moyenne
    variance=sum(tableau2)/n #calcule de la variance
    s=sqrt(variance) #calcule de l'écartype
    a=m-2*s
    b=m+2*s
    compteur=0
    for i in range(n):
        if tableau[i]<=b and tableau[i]>=a:
            compteur+=1
    proportion=compteur/n
    return[m,s,proportion] #on renvoie un tableau qui contient la moyenne, l'écart type et la proportion d'éléments appartenant à [m-2s, m+2s] m=moyenne statistique et S=écart type
tableau=[i**2 for i in range(100)]
print("tableau=[i**2 for i in range(100)]\n{}".format(stats(tableau)))
sleep(5)
