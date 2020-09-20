import codecs, os, tkinter
def maze(t,nb_ligne, nb_colonne):
    print()
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
        print()


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
t1=[[1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,1],
    [1,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,3,1],
    [1,0,1,1,1,0,0,1],
    [1,0,0,3,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]]
maze(t1,9,8)
maze(t_2,9,8)
maze(t_3,9,8)
#f=open("maze_symbole_legend.txt", "r")
#print (f.read())
#f.close()
print ("worked")
f=open("maze_keper.txt", "r")
aaa=chosemaze1=input("Pour avoir les trois informations, pour pouvoir afficher le labyrinthe désiré, entrez successivement dans les trois questions qui suivent (<le nom> dans la première question, <le nombre de lignes> dans la seconde question, <le nombre de colonnes> dans la troisième question)\nExemple:dans maze(t1,9,8)\nQ1:t1\nQ2:9\nQ3:8\nEntrez le nom du labyrinthe à afficher (ex: t1):")
bbb=chosemaze2=int(input("Entrez le nombre de lignes du labyrinthe (ex: 9):"))
ccc=chosemaze3=int(input("Entrez le nombre de colones de votre labyrinthe (ex: 8):"))
#aaaa="maze("
#aaaa+=chosemaze1+","+chosemaze2+","+chosemaze3+")"
s=f.read(maze(chosemaze1,chosemaze2,chosemaze3))
#s=f.read()
print(s)
print ("** Début d'affichage du labyrinthe {} **\n{}\n{}\n** Fin d'affichage du labyrinthe {}**".format(chosemaze1, aaaa, maze(chosemaze1,chosemaze2,chosemaze3), chosemaze1))
