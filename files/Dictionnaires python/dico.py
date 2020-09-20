print("tableau sans numpy")
t=[[1,2,3,4,5],
   [6,7,8,9,0],
   [0,0,0,0,0]]
for y in range(3):
    for x in range(5):
        print(t[y][x], end=" ")
    print()

print("dictionnaire avec python")
data={} # initialiser dictionnaire
data={'Jean Pierre':25, 'Bertrand':49, 'Jérome':50, 'David':12}
#Ajouter des valeurs à un dictionnaire
data['Isabelle']=35
#Affichage correspondant à la clef
print('Age de Bertrand', end=" : ")
print(data.get('Bertrand'))
#Affichage de toutes les clefs:
for clef in data.keys():
    print(clef)
#affihcage des valeurs:
for valeur in data.values(): #l'ordre d'écriture en sortie varie
    print(valeur)
#affichage des couples clef,valeur
for clef,valeur in data.items():
    print(clef,valeur)
#recherche d'une clef dans un dictionnaire
if 'Bertrand' in data:
    print('La clef Bertrand est bien présente')
#Je veux chercher toutes les personnes de plus de 30 ans:
print()
print('voici les personnes de plus de 30 ans')
for clef,valeur in data.items():
    if valeur>30:
        print(clef)
print()

#supprimer une clef (et la valeur associée) à un dictionnaire
del data['Isabelle']
if 'Isabelle' in data:
    print("la clef isabelle est bien présente")
else:
    print("la clef isabelle n'existe plus")

#On veut afficher un tableau de 8 lignes (y) et 10 colonnes (x)
from numpy import *
# Procédure d'affichage du tableau
def affiche_tableau(x1,y1):
    for y in range(y1):
        for x in range(x1):
            print(t[x,y], end=" ")
        print()

nb_ligne=8
nb_colonne=10
#création du tableau
t=zeros([nb_ligne,nb_colonne], int) #t[y,x] y=8 lignes x=10 colonnes
#Ci dessous possibilité d'initialiser le tableau
t[0,]=[1,1,1,1,1,1,1,1,1,1]
t[1,]=[1,2,0,0,0,0,0,0,0,1]
t[2,]=[1,0,1,1,1,1,1,0,0,1]
t[3,]=[1,0,0,0,0,0,1,0,0,1]
t[4,]=[1,0,1,1,1,0,1,1,1,1]
t[5,]=[1,0,1,1,1,0,1,0,0,1]
t[6,]=[1,1,1,1,1,0,0,0,3,1]
t[7,]=[1,1,1,1,1,1,1,1,1,1]

affiche_tableau(nb_colonne,nb_ligne) #appel de la procédure d'affichage

def affiche_tableau2(x1,y1):
    for y in range(y1):
        for x in range(x1):
            if t[y,x]==0:
                print(".", end=" ")
            else:
                print(t[x,y], end=" ")
        print()
affiche_tableau2(nb_colonne,nb_ligne)
