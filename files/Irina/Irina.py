import math, random
from time import sleep
print ("""
def hypothenus(a,b):
    c=sqrt(a**2+b**2)
    return c

print (hypothenus(3,4))

h=int(input("opzerpoezrzperezproezjrpzer: "))
b=int(input("dhaoiahreozaheozaheza:"))
def airetrianglerectangle(b,h):
    a=b*h/2
    return a
print ("aire du triangle rectangle {}".format(airetrianglerectangle(b, h)))


#y=7x**2-3x+2

#I="O"
#while I=="o" or I=="O":
#x=int(input("Donnez une valeur à x:"))
#    def f1(x):
#        y=7*x**2-3*x+2
#    return y
#    I=input("{}\ncontinuer : [(o)ui/(n)on]".format(f1(x)))

n=int(input("affectez une valeure à n:"))
def compter(n,L1):
    compteur = L1[n]
    LongueurListe=len(L1)
    for i in range(n):
        if L1[]==n:
            compteur=n
    return compteur
L1=[1,27,27,19,18,113,22,1,14,189,7,2,23,21,22,23,100,1,100,22,14,100,1]
print (compter(1,L1))

def maximum(liste):
    max1=
    LongueurListe=
    for 
for i in range(10):
    print("x", end=" ")""")

ligne=10
colonne=20
for i in range(ligne):
    for j in range(colonne):
        print ("x", end=" ")
    print()

#ligne=10000000000000000000
#print
ligne=5
#colonne=200
for i in range(ligne):
    for j in range(i):
        print("x", end=" ")
    print()

for i in range(ligne,0,-1):
    for j in range(i):
         print("x", end=" ")
    print()

ligne=17
for i in range(ligne):
    for j in range(ligne+i):
         print(" ", end=" ")
    for j in range (2*j+1):
        print ("x", end=" ")
    print()
ligne=17
for i in range(ligne):
    for j in range(ligne-i):
         print(" ", end=" ")
    for j in range (2*j+1):
        print ("x", end=" ")
    print()
ligne=5
for i in range(ligne):
    for j in range(ligne-i):
         print(" ", end=" ")
    for j in range (2*i+1):
        print ("x", end=" ")
    print()
ligne=5
for i in range(ligne,0,-1):
    for j in range(ligne-i):
         print(" ", end=" ")
    for j in range (2*i+1):
        print ("x", end=" ")
    print()
print ("          x")
ligne=100
colonne=200

print ("""#ligne=10
#colonne=200
#for i in range(ligne,0,-1):
#    for j in range(i):
#        print("U", end=" ")
#    print()""")
#print
t=[[0,1,2,3,4],
   [5,6,7,8,9],
   [10,11,12,13,14],
   [15,16,17,18,19]]

print(t[0][0])
print(t[2][1])
print(t[1][3])
z=0
while z<=100:
    x=random.randint(0, 3)
    y=random.randint(0, 4)
    print("nb de tour{}".format(z))
    print ("x,y={}, {}".format(x, y))
    print (t[x][y])
    z+=1

for ligne in range(4):
    for colonne in range(5):
        valeur=t[ligne][colonne]
        print(valeur, end=" ")
    print()
print()
for ligne in range(4):
    for colonne in range(5):
        valeur=t[ligne][colonne]
        if valeur<10:
            print(valeur, end=" ")
        else:
            print(valeur, end=" ")
    print()

ligne=10
colonne=20
for i in range(ligne):
    for j in range(colonne):
        print ("x", end=" ")
    print()

b=0
#ligne=1000000000 #long
ligne=100 #court
colonne=52
for i in range(ligne):
    for j in range(colonne):
        b=random.randint(0, 1)
        print (b, end="  ")
    print()
print()
ligne=100 #court
colonne=52
for i in range(ligne):
    for j in range(colonne):
        b=random.randint(0, 9)
        print (b, end="  ")
    print()
print()
ligne=100 #court
colonne=52
for i in range(ligne):
    for j in range(colonne):
        b=random.randint(-9, 9)
        print (b, end="  ")
    print()

#print
a=0
i=0
e=1
for e in range(101):
    a+=random.randint (1, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    print(a)
    #print ("i=",i)
    #print ("e=",e)
    i+=1
    e+=1
    if i==100 or i==101 or i==102:
        e+=1

ligne=5
for i in range(ligne):
    for j in range(i):
        print("x", end=" ")
    print()

for i in range(ligne,0,-1):
    for j in range(i):
         print("x", end=" ")
    print()



for i in range(ligne):
    for j in range(i):
         print(" ", end=" ")
    for j in range (2*i+1):
        print ("x", end=" ")
    print()

ligne=5
for i in range(ligne):
    for j in range(ligne+i):
         print(" ", end=" ")
    for j in range (2*j+1):
        print ("x", end=" ")
    print()
ligne=5
for i in range(ligne):
    for j in range(ligne-i):
         print(" ", end=" ")
    for j in range (2*j+1):
        print ("x", end=" ")
    print()


eeleelelelel="f*hi***k y**how***u l*do*e b**you**ch l******do*******c"
for letter in eeleelelelel:
    print (letter, end=" ")
    print()

longeur=len(eeleelelelel)
e=0
for i in range(longeur):
    print ("lettre[{}]:".format(e),eeleelelelel[i], end="\n")
    e+=1

texte_1="sqhfmldsqhfmosqhfmdsqhfmidshfmdshfhdsfmlhdsfmlkhsqmlkfhdsqfmlkhdsflkdsfds*fds*f*dsf*d*f*df*ds*f*dsf*ds*fds*fsd*f*ds*****f*srzruzrozuprmsofhsmqfihsoqhfdsqfhdifmdslfkmdsfhiosqdmlhkezm"
texte_2="******qs*dsq*dqs*dsq*d*sq*d*sqd*sqd*sq*d*qd*qd*sq*d*dsjdiMOZHZAIDNUFjmoDNCMOdnmjsoqlqk,dld,nlsmsq*dsq*dsqd$d$*ùdd*md$d^$m*$d*m$d*$m^$*$à)=ç'fdsqfdsfsqfsqdsà3é(àèà-ç_'èé'àçè_(ç-à(_àéç_'(àç-(_'pezuhgsodlfjsm27309372498630729843070965825737874°875943265023186°5°175°98437°598647"
texte_3=texte_2+texte_1+"ezaeazezaeza"
texte_4=texte_3+2*texte_3
texte_5=2*texte_4
print (texte_1, texte_2, texte_3, texte_4, texte_5)

def affiche(eeleelelelel, n):
    for i in range(n):
        print(eeleelelelel, end=" ")

affiche("Bonjour",3)
print()
texte=eeleelelelel+"Bonjour Bertrand, comment vas tu?"
for lettre in texte:
    code=ord(lettre)
    #print(chr(code), end=" ")
    print(chr(code+1), end=" ")

print ("""#encoder
def encrypte(texte):
    texte_crypte=""
    for i in range(lettre):
        code=ord(lettre)
        texte_crypte=texte_crypte+chr(texte)
    return texte_crypte
texte_cypte=encrypte("Bonjour Bertrand, comment vas tu?")
print ("texte encrypte=", texte_crypte)

#decoder
def decrypte(texte):
    texte_decrypte=""
    for i in range(texte):
        code=ord(lettre)
        texte_decrypte=texte_decrypte+chr(lettre)
    return texte_decrypte
print ("texte decrypte={}".format(decrypte(texte_crypte)))""")

#recherche de chaine
t1="Bonjour Bertrand, comment vas-tu?"
if"Bertrand" in t1:
    print ("'Bertrand' est bien dans la chaine")
else:
    print ("Chaine non trouvée")

def cherche(texte, chaine):
    if texte in t1:
        print ("True")
    else:
        print ("False")
    return texte

#programme principal
t1="sqjfdshfsfsdkfjkdsjfldsjfdsjfkdsjf Bonjour Bertrand, comment vas-tu?"
print (cherche(t1, "comment"))
print (cherche(t1, "toto"))

def maze(t,nb_ligne, nb_colonne):
   for y in range(nb_ligne):
       for x in range(nb_colonne):
           valeur=t[y][x]
           if valeur ==0:
               print(".", end=" ")
           elif valeur==1:
               print(t[y][x], end=" ")
           elif valeur==2:
               print("@", end=" ")
           elif valeur==3:
               print("M", end=" ")
           elif valeur==4:
               print("$", end=" ")
           elif valeur==5:
               print("£", end=" ")
           elif valeur==6:
               print("∆", end=" ")
           elif valeur==7:
               print("N", end=" ")
           elif valeur==8:
               print("❤",end=" ")
       print()

t_1=[[1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,1],
    [1,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,3,1],
    [1,0,107,1,1,0,0,1],
    [1,0,0,3,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]]
t_2=[[1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,1],
    [1,1,1,1,0,0,0,1],
    [1,0,0,1,0,0,0,1],
    [1,0,0,1,0,1,3,1],
    [1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,5,1],
    [1,0,0,0,3,0,4,1],
    [1,1,1,1,1,1,1,1]]
t_3=[[3,0,3,3,3,3,3,3],
    [3,0,0,0,0,0,0,3],
    [3,6,6,6,0,6,6,3],
    [3,6,0,6,0,0,0,3],
    [3,0,0,0,0,6,6,3],
    [3,0,6,6,0,0,0,3],
    [3,0,0,0,6,6,6,3],
    [3,6,6,0,0,0,0,3],
    [3,3,3,3,3,3,0,3]]
t_maze1=[[3,0,3,3,3,3,3,1,3,3,3,1,3,3,3,3,3,3],
         [3,0,3,0,0,0,7,7,3,0,0,0,0,2,0,0,2,3],
         [3,0,0,0,7,0,0,1,0,0,3,1,0,2,2,0,2,3],
         [3,0,7,0,0,7,7,1,0,3,0,1,0,2,0,0,0,3],
         [3,0,0,7,0,0,7,1,0,0,0,1,0,2,0,2,0,3],
         [3,7,0,7,7,0,7,1,3,0,3,1,0,2,0,2,0,3],
         [3,0,0,0,7,0,0,0,0,0,3,1,0,0,0,2,0,3],
         [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,3]]
t_maze1_1=[[3,0,3,3,3,3,3,1,3],
         [3,0,3,0,0,0,7,7,3],
         [3,0,0,0,7,0,0,1,0],
         [3,0,7,0,0,7,7,1,0],
         [3,0,0,7,0,0,7,1,0],
         [3,7,0,7,7,0,7,1,3],
         [3,0,0,0,7,0,0,0,0],
         [3,3,3,3,3,3,3,3,3]]
t_maze1_2=[[3,3,1,3,3,3,3,3,3],
           [0,0,0,0,2,0,0,2,3],
           [0,3,1,0,2,2,0,2,3],
           [3,0,1,0,2,0,0,0,3],
           [0,0,1,0,2,0,2,0,3],
           [0,3,1,0,2,0,2,0,3],
           [0,3,1,0,0,0,2,0,3],
           [3,3,3,3,3,3,3,0,3]]
t_love=[[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]]

maze(t_1,9,8)
maze(t_2,9,8)
maze(t_3,9,8)
maze(t_maze1,8,18)
sleep(5)
maze(t_love,8,373)
sleep(10)
list1=["### Decoding Table\n","'\x00'     #  0x00 -> NULL\n","'\x01'     #  0x01 -> START OF HEADING\n","'\x02'     #  0x02 -> START OF TEXT\n","'\x03'     #  0x03 -> END OF TEXT\n","'\x04'     #  0x04 -> END OF TRANSMISSION\n","'\x05'     #  0x05 -> ENQUIRY\n","'\x06'     #  0x06 -> ACKNOWLEDGE\n","'\x07'     #  0x07 -> BELL\n","'\x08'     #  0x08 -> BACKSPACE\n","'\t'       #  0x09 -> HORIZONTAL TABULATION\n","'\\n'       #  0x0A -> LINE FEED\n","'\x0b'     #  0x0B -> VERTICAL TABULATION\n","'\x0c'     #  0x0C -> FORM FEED\n","'\r'       #  0x0D -> CARRIAGE RETURN\n","'\x0e'     #  0x0E -> SHIFT OUT\n","'\x0f'     #  0x0F -> SHIFT IN\n","'\x10'     #  0x10 -> DATA LINK ESCAPE\n","'\x11'     #  0x11 -> DEVICE CONTROL ONE\n","'\x12'     #  0x12 -> DEVICE CONTROL TWO\n","'\x13'     #  0x13 -> DEVICE CONTROL THREE\n","'\x14'     #  0x14 -> DEVICE CONTROL FOUR\n","'\x15'     #  0x15 -> NEGATIVE ACKNOWLEDGE\n","'\x16'     #  0x16 -> SYNCHRONOUS IDLE\n","'\x17'     #  0x17 -> END OF TRANSMISSION BLOCK\n","'\x18'     #  0x18 -> CANCEL\n","'\x19'     #  0x19 -> END OF MEDIUM\n","'\x1a'     #  0x1A -> SUBSTITUTE\n","'\x1b'     #  0x1B -> ESCAPE\n","'\x1c'     #  0x1C -> FILE SEPARATOR\n","'\x1d'     #  0x1D -> GROUP SEPARATOR\n","'\x1e'     #  0x1E -> RECORD SEPARATOR\n","'\x1f'     #  0x1F -> UNIT SEPARATOR\n","' '        #  0x20 -> SPACE\n","'!'        #  0x21 -> EXCLAMATION MARK\n","""'"'        #  0x22 -> QUOTATION MARK\n""","'#'        #  0x23 -> NUMBER SIGN","\n'$'        #  0x24 -> DOLLAR SIGN\n","'%'        #  0x25 -> PERCENT SIGN\n","'&'        #  0x26 -> AMPERSAND\n",""""'"        #  0x27 -> APOSTROPHE\n""","'('        #  0x28 -> LEFT PARENTHESIS\n","')'        #  0x29 -> RIGHT PARENTHESIS\n","'*'        #  0x2A -> ASTERISK","\n'+'        #  0x2B -> PLUS SIGN\n","','        #  0x2C -> COMMA\n","'-'        #  0x2D -> HYPHEN-MINUS\n","'.'        #  0x2E -> FULL STOP\n","'/'        #  0x2F -> SOLIDUS\n","'0'        #  0x30 -> DIGIT ZERO\n","'1'        #  0x31 -> DIGIT ONE\n","'2'        #  0x32 -> DIGIT TWO\n","'3'        #  0x33 -> DIGIT THREE\n","'4'        #  0x34 -> DIGIT FOUR\n","'5'        #  0x35 -> DIGIT FIVE\n","'6'        #  0x36 -> DIGIT SIX\n","'7'        #  0x37 -> DIGIT SEVEN\n","'8'        #  0x38 -> DIGIT EIGHT\n","'9'        #  0x39 -> DIGIT NINE\n","':'        #  0x3A -> COLON\n","';'        #  0x3B -> SEMICOLON\n","'<'        #  0x3C -> LESS-THAN SIGN\n","'='        #  0x3D -> EQUALS SIGN\n","'>'        #  0x3E -> GREATER-THAN SIGN\n","'?'        #  0x3F -> QUESTION MARK\n","'@'        #  0x40 -> COMMERCIAL AT\n","'A'        #  0x41 -> LATIN CAPITAL LETTER A\n","'B'        #  0x42 -> LATIN CAPITAL LETTER B\n","'C'        #  0x43 -> LATIN CAPITAL LETTER C\n","'D'        #  0x44 -> LATIN CAPITAL LETTER D\n","'E'        #  0x45 -> LATIN CAPITAL LETTER E\n","'F'        #  0x46 -> LATIN CAPITAL LETTER F\n","'G'        #  0x47 -> LATIN CAPITAL LETTER G\n","'H'        #  0x48 -> LATIN CAPITAL LETTER H\n","'I'        #  0x49 -> LATIN CAPITAL LETTER I\n","'J'        #  0x4A -> LATIN CAPITAL LETTER J\n","'K'        #  0x4B -> LATIN CAPITAL LETTER K\n","'L'        #  0x4C -> LATIN CAPITAL LETTER L\n","'M'        #  0x4D -> LATIN CAPITAL LETTER M\n","'N'        #  0x4E -> LATIN CAPITAL LETTER N\n","'O'        #  0x4F -> LATIN CAPITAL LETTER O\n","'P'        #  0x50 -> LATIN CAPITAL LETTER P\n","'Q'        #  0x51 -> LATIN CAPITAL LETTER Q\n","'R'        #  0x52 -> LATIN CAPITAL LETTER R\n","'S'        #  0x53 -> LATIN CAPITAL LETTER S\n","'T'        #  0x54 -> LATIN CAPITAL LETTER T\n","'U'        #  0x55 -> LATIN CAPITAL LETTER U\n","'V'        #  0x56 -> LATIN CAPITAL LETTER V\n","'W'        #  0x57 -> LATIN CAPITAL LETTER W\n","'X'        #  0x58 -> LATIN CAPITAL LETTER X\n","'Y'        #  0x59 -> LATIN CAPITAL LETTER Y\n","'Z'        #  0x5A -> LATIN CAPITAL LETTER Z\n'['        #  0x5B -> LEFT SQUARE BRACKET\n","'\\'       #  0x5C -> REVERSE SOLIDUS\n","']'        #  0x5D -> RIGHT SQUARE BRACKET\n","'^'        #  0x5E -> CIRCUMFLEX ACCENT\n","'_'        #  0x5F -> LOW LINE\n","'`'        #  0x60 -> GRAVE ACCENT\n","'a'        #  0x61 -> LATIN SMALL LETTER A\n","'b'        #  0x62 -> LATIN SMALL LETTER B\n","'c'        #  0x63 -> LATIN SMALL LETTER C\n","'d'        #  0x64 -> LATIN SMALL LETTER D\n","'e'        #  0x65 -> LATIN SMALL LETTER E\n","'f'        #  0x66 -> LATIN SMALL LETTER F\n","'g'        #  0x67 -> LATIN SMALL LETTER G\n","'h'        #  0x68 -> LATIN SMALL LETTER H\n","'i'        #  0x69 -> LATIN SMALL LETTER I\n","'j'        #  0x6A -> LATIN SMALL LETTER J\n","'k'        #  0x6B -> LATIN SMALL LETTER K\n","'l'        #  0x6C -> LATIN SMALL LETTER L\n","'m'        #  0x6D -> LATIN SMALL LETTER M\n","'n'        #  0x6E -> LATIN SMALL LETTER N\n","'o'        #  0x6F -> LATIN SMALL LETTER O\n","'p'        #  0x70 -> LATIN SMALL LETTER P\n","'q'        #  0x71 -> LATIN SMALL LETTER Q\n","'r'        #  0x72 -> LATIN SMALL LETTER R\n","'s'        #  0x73 -> LATIN SMALL LETTER S\n","'t'        #  0x74 -> LATIN SMALL LETTER T\n","'u'        #  0x75 -> LATIN SMALL LETTER U\n","'v'        #  0x76 -> LATIN SMALL LETTER V\n","'w'        #  0x77 -> LATIN SMALL LETTER W\n","'x'        #  0x78 -> LATIN SMALL LETTER X\n","'y'        #  0x79 -> LATIN SMALL LETTER Y\n","'z'        #  0x7A -> LATIN SMALL LETTER Z\n","'{'        #  0x7B -> LEFT CURLY BRACKET\n","'|'        #  0x7C -> VERTICAL LINE\n","'}'        #  0x7D -> RIGHT CURLY BRACKET\n","'~'        #  0x7E -> TILDE\n","'\x7f'     #  0x7F -> DELETE\n","'\u20ac'   #  0x80 -> EURO SIGN\n","'\ufffe'   #  0x81 -> UNDEFINED\n","'\u201a'   #  0x82 -> SINGLE LOW-9 QUOTATION MARK\n","'\u0192'   #  0x83 -> LATIN SMALL LETTER F WITH HOOK\n","'\u201e'   #  0x84 -> DOUBLE LOW-9 QUOTATION MARK\n","'\u2026'   #  0x85 -> HORIZONTAL ELLIPSIS\n","'\u2020'   #  0x86 -> DAGGER\n","'\u2021'   #  0x87 -> DOUBLE DAGGER\n","'\u02c6'   #  0x88 -> MODIFIER LETTER CIRCUMFLEX ACCENT\n","'\u2030'   #  0x89 -> PER MILLE SIGN\n","'\u0160'   #  0x8A -> LATIN CAPITAL LETTER S WITH CARON\n","'\u2039'   #  0x8B -> SINGLE LEFT-POINTING ANGLE QUOTATION MARK\n","'\u0152'   #  0x8C -> LATIN CAPITAL LIGATURE OE\n","'\ufffe'   #  0x8D -> UNDEFINED\n","'\u017d'   #  0x8E -> LATIN CAPITAL LETTER Z WITH CARON\n","'\ufffe'   #  0x8F -> UNDEFINED\n","'\ufffe'   #  0x90 -> UNDEFINED\n","'\u2018'   #  0x91 -> LEFT SINGLE QUOTATION MARK\n","'\u2019'   #  0x92 -> RIGHT SINGLE QUOTATION MARK\n","'\u201c'   #  0x93 -> LEFT DOUBLE QUOTATION MARK\n","'\u201d'   #  0x94 -> RIGHT DOUBLE QUOTATION MARK\n","'\u2022'   #  0x95 -> BULLET\n","'\u2013'   #  0x96 -> EN DASH\n","'\u2014'   #  0x97 -> EM DASH\n","'\u02dc'   #  0x98 -> SMALL TILDE\n","'\u2122'   #  0x99 -> TRADE MARK SIGN\n","'\u0161'   #  0x9A -> LATIN SMALL LETTER S WITH CARON\n","'\u203a'   #  0x9B -> SINGLE RIGHT-POINTING ANGLE QUOTATION MARK\n","'\u0153'   #  0x9C -> LATIN SMALL LIGATURE OE\n","'\ufffe'   #  0x9D -> UNDEFINED\n","'\u017e'   #  0x9E -> LATIN SMALL LETTER Z WITH CARON\n","'\u0178'   #  0x9F -> LATIN CAPITAL LETTER Y WITH DIAERESIS\n","'\xa0'     #  0xA0 -> NO-BREAK SPACE\n","'\xa1'     #  0xA1 -> INVERTED EXCLAMATION MARK\n","'\xa2'     #  0xA2 -> CENT SIGN\n","'\xa3'     #  0xA3 -> POUND SIGN\n","'\xa4'     #  0xA4 -> CURRENCY SIGN\n","'\xa5'     #  0xA5 -> YEN SIGN\n","'\xa6'     #  0xA6 -> BROKEN BAR\n","'\xa7'     #  0xA7 -> SECTION SIGN\n","'\xa8'     #  0xA8 -> DIAERESIS\n","'\xa9'     #  0xA9 -> COPYRIGHT SIGN\n","'\xaa'     #  0xAA -> FEMININE ORDINAL INDICATOR\n","'\xab'     #  0xAB -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK\n","'\xac'     #  0xAC -> NOT SIGN\n","'\xad'     #  0xAD -> SOFT HYPHEN\n","'\xae'     #  0xAE -> REGISTERED SIGN\n","'\xaf'     #  0xAF -> MACRON\n","'\xb0'     #  0xB0 -> DEGREE SIGN\n","'\xb1'     #  0xB1 -> PLUS-MINUS SIGN\n","'\xb2'     #  0xB2 -> SUPERSCRIPT TWO\n","'\xb3'     #  0xB3 -> SUPERSCRIPT THREE\n","'\xb4'     #  0xB4 -> ACUTE ACCENT\n","'\xb5'     #  0xB5 -> MICRO SIGN\n","'\xb6'     #  0xB6 -> PILCROW SIGN\n","'\xb7'     #  0xB7 -> MIDDLE DOT\n","'\xb8'     #  0xB8 -> CEDILLA\n","'\xb9'     #  0xB9 -> SUPERSCRIPT ONE\n","'\xba'     #  0xBA -> MASCULINE ORDINAL INDICATOR\n","'\xbb'     #  0xBB -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK\n","'\xbc'     #  0xBC -> VULGAR FRACTION ONE QUARTER\n","'\xbd'     #  0xBD -> VULGAR FRACTION ONE HALF\n","'\xbe'     #  0xBE -> VULGAR FRACTION THREE QUARTERS\n","'\xbf'     #  0xBF -> INVERTED QUESTION MARK\n","'\xc0'     #  0xC0 -> LATIN CAPITAL LETTER A WITH GRAVE\n","'\xc1'     #  0xC1 -> LATIN CAPITAL LETTER A WITH ACUTE\n","'\xc2'     #  0xC2 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX\n","'\xc3'     #  0xC3 -> LATIN CAPITAL LETTER A WITH TILDE\n","'\xc4'     #  0xC4 -> LATIN CAPITAL LETTER A WITH DIAERESIS\n","'\xc5'     #  0xC5 -> LATIN CAPITAL LETTER A WITH RING ABOVE\n","'\xc6'     #  0xC6 -> LATIN CAPITAL LETTER AE\n","'\xc7'     #  0xC7 -> LATIN CAPITAL LETTER C WITH CEDILLA\n","'\xc8'     #  0xC8 -> LATIN CAPITAL LETTER E WITH GRAVE\n","'\xc9'     #  0xC9 -> LATIN CAPITAL LETTER E WITH ACUTE\n","'\xca'     #  0xCA -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX\n","'\xcb'     #  0xCB -> LATIN CAPITAL LETTER E WITH DIAERESIS\n","'\xcc'     #  0xCC -> LATIN CAPITAL LETTER I WITH GRAVE\n","'\xcd'     #  0xCD -> LATIN CAPITAL LETTER I WITH ACUTE\n","'\xce'     #  0xCE -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX\n","'\xcf'     #  0xCF -> LATIN CAPITAL LETTER I WITH DIAERESIS\n","'\xd0'     #  0xD0 -> LATIN CAPITAL LETTER ETH\n","'\xd1'     #  0xD1 -> LATIN CAPITAL LETTER N WITH TILDE\n","'\xd2'     #  0xD2 -> LATIN CAPITAL LETTER O WITH GRAVE\n","'\xd3'     #  0xD3 -> LATIN CAPITAL LETTER O WITH ACUTE\n","'\xd4'     #  0xD4 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX\n","'\xd5'     #  0xD5 -> LATIN CAPITAL LETTER O WITH TILDE\n","'\xd6'     #  0xD6 -> LATIN CAPITAL LETTER O WITH DIAERESIS\n","'\xd7'     #  0xD7 -> MULTIPLICATION SIGN\n","'\xd8'     #  0xD8 -> LATIN CAPITAL LETTER O WITH STROKE\n","'\xd9'     #  0xD9 -> LATIN CAPITAL LETTER U WITH GRAVE\n","'\xda'     #  0xDA -> LATIN CAPITAL LETTER U WITH ACUTE\n","'\xdb'     #  0xDB -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX\n","'\xdc'     #  0xDC -> LATIN CAPITAL LETTER U WITH DIAERESIS\n","'\xdd'     #  0xDD -> LATIN CAPITAL LETTER Y WITH ACUTE\n","'\xde'     #  0xDE -> LATIN CAPITAL LETTER THORN\n","'\xdf'     #  0xDF -> LATIN SMALL LETTER SHARP S\n","'\xe0'     #  0xE0 -> LATIN SMALL LETTER A WITH GRAVE\n","'\xe1'     #  0xE1 -> LATIN SMALL LETTER A WITH ACUTE\n","'\xe2'     #  0xE2 -> LATIN SMALL LETTER A WITH CIRCUMFLEX\n","'\xe3'     #  0xE3 -> LATIN SMALL LETTER A WITH TILDE\n","'\xe4'     #  0xE4 -> LATIN SMALL LETTER A WITH DIAERESIS\n","'\xe5'     #  0xE5 -> LATIN SMALL LETTER A WITH RING ABOVE\n","'\xe6'     #  0xE6 -> LATIN SMALL LETTER AE\n","'\xe7'     #  0xE7 -> LATIN SMALL LETTER C WITH CEDILLA\n","'\xe8'     #  0xE8 -> LATIN SMALL LETTER E WITH GRAVE\n","'\xe9'     #  0xE9 -> LATIN SMALL LETTER E WITH ACUTE\n","'\xea'     #  0xEA -> LATIN SMALL LETTER E WITH CIRCUMFLEX\n","'\xeb'     #  0xEB -> LATIN SMALL LETTER E WITH DIAERESIS\n","'\xec'     #  0xEC -> LATIN SMALL LETTER I WITH GRAVE\n","'\xed'     #  0xED -> LATIN SMALL LETTER I WITH ACUTE\n","'\xee'     #  0xEE -> LATIN SMALL LETTER I WITH CIRCUMFLEX\n","'\xef'     #  0xEF -> LATIN SMALL LETTER I WITH DIAERESIS\n","'\xf0'     #  0xF0 -> LATIN SMALL LETTER ETH\n","'\xf1'     #  0xF1 -> LATIN SMALL LETTER N WITH TILDE\n","'\xf2'     #  0xF2 -> LATIN SMALL LETTER O WITH GRAVE\n","'\xf3'     #  0xF3 -> LATIN SMALL LETTER O WITH ACUTE\n","'\xf4'     #  0xF4 -> LATIN SMALL LETTER O WITH CIRCUMFLEX\n","'\xf5'     #  0xF5 -> LATIN SMALL LETTER O WITH TILDE\n","'\xf6'     #  0xF6 -> LATIN SMALL LETTER O WITH DIAERESIS\n","'\xf7'     #  0xF7 -> DIVISION SIGN\n","'\xf8'     #  0xF8 -> LATIN SMALL LETTER O WITH STROKE\n","'\xf9'     #  0xF9 -> LATIN SMALL LETTER U WITH GRAVE\n","'\xfa'     #  0xFA -> LATIN SMALL LETTER U WITH ACUTE\n","'\xfb'     #  0xFB -> LATIN SMALL LETTER U WITH CIRCUMFLEX\n","'\xfc'     #  0xFC -> LATIN SMALL LETTER U WITH DIAERESIS\n","'\xfd'     #  0xFD -> LATIN SMALL LETTER Y WITH ACUTE\n","'\xfe'     #  0xFE -> LATIN SMALL LETTER THORN\n","'\xff'     #  0xFF -> LATIN SMALL LETTER Y WITH DIAERESIS"]
for letter in list1:
    print (letter)
