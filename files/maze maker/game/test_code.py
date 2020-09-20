import codecs, os#, data.txt
os=os.getcwd()
print (os)
def affiche_tableau(t,nb_ligne, nb_colonne):
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
       print()
fichier = open("data - Copie.py", "r")
print (fichier.read())
# print (fichier.read(affiche_tableau(t1,9,8)))
fichier.close()
# f=open("data.txt", "a")
# wri=input("Entrez ici le nom du labyrinthe (pas plus de deux lettres):")
# ze=wri
# eza=len(ze)
# if eza==2 or eza==1:
#     wri+="=["
#     wri+=input("Entrez la première ligne de votre labyrinthe (commencez par '[' mettez une virgule après chaque nombre, fermez par '],\\n'):")
#     io="o"
#     li=2
#     print("Pour chaque ligne, commencez par '[', mettez une virgule après chaque nombre, fermez par '],\\n'")
#     while io=="o" or io=="O" or io=="0":
#         wri+="  ["
#         wri+=input("Quelle est votre ligne n°{}:".format(li))
#         wri+="],\n"
#         li+=1
#         ioo="o"
#         while ioo=="o":
#             io=input("Rajouter une nouvelle ligne? [(o)ui/(n)on]:")
#             if io=="o" or io=="O" or io=="0":
#                 ioo="d"
#             elif io=="n" or io=="N":
#                 break
#             else:
#                 print("Assurez-vous d'avoir entré la lettre 'n' pour non ou la lettre 'o' pour oui.\nVous avez entré: {}".format(io))
#                 ioo="o"
#                 continue
#     wri+="]"
#     f=open("data.txt", "a")
#     f.write(wri)
#     print (wri)
#     f.close()
#     # io="n"
    
# elif eza==1:
#     print ("attention possibilité de chevauchement")
#     # continue
# else:
#     print ("mercie de n'entrer que deux caractères")
    # continue


wri=input("Entrez ici le nom du labyrinthe (pas plus de deux lettres):")
ze=wri
eza=len(ze)
if eza==2 or eza==1:
    io="o"
    li=1
    wri+="=["
    brac="["
    brac2="],\n"
    i=0
    ligne=int(input("De combien de lignes se compose votre labyrinthe?:"))
    print("Pour chaque ligne, mettez une virgule après chaque nombre sauf au dernier. (exemple: 1,2,1,2,1,2,1,2,1)")
    while i<ligne:
        wri+=brac
        lenline=input("Quelle est votre ligne n°{}:".format(li))
        lene=len(lenline)
        wri+=lenline
        wri+=brac2
        li+=1
        i+=1
        # print ("i={}, ligne={}, li={}".format(i, ligne, li))
        if i==ligne-1:
            brac2="]"
        elif i==1 and eza==2:
            brac="    ["
        elif i==1 and eza==1:
            brac="   ["
        else:
            continue
    wri+="]\n"
    f=open("data.txt", "a")
    f.write(a)
    f.close()
    print ("Voici votre labyrinthe:\n{}\nVotre labyrinthe se nome {}, fait {} ligne et {} colonnes ".format(wri, ze, ligne, lene))
    lle=ligne
    llle=lene
    maaze="maze({},{},{})\n".format(ze, lle, llle)
    f.write(maaze)
    f.close()
else:
    print ("mercie de n'entrer que deux caractères")
    # continue

# f.write(wri)
# f.close()
# f=open("data.txt", "r")
# s=f.read()
# print ("** contenu de s **")
# print (s)
# print ("** fin contenu **")
# print ("type de s:{}".format(type(s)))
# print ("longueur de s: {}".format(len(s)))
# print ("** début d'affichage des labyrintes **\n{}\n** fin d'affichage **".format(s))
# f.close()

#f=open("data.txt", "w")
# #s=f.read()
#s=f.write("list1=[[1,2,1,3,1,4,1,4,1,2,1,3,2],\n[1,2,4,4,3,4,3,5,7],\n[5,5,5,5,5,5,5,5,5,5,5],\n[5,4,3,2,4,3,2,3,4,5,4]]\n")
# f.close()

# f=open("data.txt", "a")
# f.write("list=[[1,2,3,4,5,6,è,8],\n[12345,32444,24,2],\n34234,32,4,324,23,4,324]]")
# f.write("\nt1=[[2,2,2,3,4,5,5,5],\n[2,3,4,5,5,6,6],\n[2,3,4,5,5,6,6,4,4]]")
# print ("** contenu de s **")
# print (s)
# print ("** fin contenu **")
# f.close()
# i=0
# f=open("data.txt", "a")
# while i<1:
#     z="1&é&é&21212121212121212\n"
#     f.write(z)
#     print ("** contenu de s **")
#     print (s)
#     print ("** fin contenu **")
# f.close()