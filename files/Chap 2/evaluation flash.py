# I L'instuction print
print("I L'instuction print\nprog 1\nv1=20\nv2=20\nres=v1*v2\nprint(res)")
v1=20
v2=20
res=v1*v2
print(res)

print("prog 2")
print("""prog 1\nv1=20\nv2=20\nres=v1*v2\nprint("resultat=",resultat)""")
v1=20
v2=20
res=v1*v2
print("resultat=",res)

print(" la différence entre ces deux progframmes est que le premier affichera juste le résultat, le second affichera le mot 'resultat =' suivi du résultat\nles guillements dans l'instruction print sert à indiquer à l'ordinateur que l'on souhaite afficher (ce qu'il y a entre elle) du texte défini.")

# II La boucle for
print ("II La boucle for\na=3\nfor i in range(4):\na=a*2\nprint(a)")
a=3
for i in range(4):
    a=a*2
    print(a)
print("la boucle a*2 est éxécuté 4 fois.\nIII-Si/alors/sinon/Et/ou")
# III Si/alors/sinon/et/ou
print("""Entrer une valeur pour n\nEntrrez une valeur pour a\nSi ((a>n) et n<100)) ou (n>100) alors\n    Afficher 'condition vraie'\nSinon\n    Afficher 'condition fausse'\n\n n=input("Entrez n:")\na=input("Entrez a:")\nif ((a>n) and (n<100)):\n    print("condition vraie")\nelse:\n    print("conditon fausse")""")

n=int(input("Entrez n:"))
a=int(input("Entrez a:"))
if ((a>n) and (n<100)):
    print("condition vraie")
else:
    print("conditon fausse")

#IV écrire
print ("""IV écrire\nc,a=0,10\nwhile a<21:\n    c+=c+a\n    a+=1\n    print("a={} tot={}".format(a,c))\nprint("S={}".format(c))""")

c,a=0,10
while a<21:
    c+=c+a
    a+=1
    print("a={} tot={}".format(a,c))
print("S={}".format(c))
#V convertir les nmbres binaires suivants en décimal
print("V convertir les nmbres binaires suivants en décimal\n10001111=1*2**8+1*2**7+1*2**6+1*2**5+1*2**1=256+128+64+32+2=450\n11001100=1*2**6+1*2**5+1*2**2+1*2**1=64+32+4+2=102\n10000001=1*2**8+1*2**1=256+2=258")
