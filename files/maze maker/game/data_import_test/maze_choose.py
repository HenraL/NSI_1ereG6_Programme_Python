from time import sleep
import codecs, os, tkinter, platform
sad,happy,mini,maxi,st,a="Dis-moi, sur WhatsApp, où tu plante\n","cool au suivant :-)\n",1,9,"o",float(input("Entrez le temps de pause du programe [de 0 à 20]:"))
def Pause():
    if platform=="Winwos":
        os.system("pause")
    else:
        sleep(a)
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
            elif valeur==7:
                print("N", end=" ")
            elif valeur==8:
                print("€", end=" ")
            elif valeur==9:
                print("|", end=" ")
            elif valeur== 10:
                print("-", end=" ")
            elif valeur==11:
                print("A", end=" ")
            elif valeur==12:
                print("B", end=" ")
            elif valeur==13:
                print("C", end=" ")
            elif valeur==14:
                print("D", end=" ")
            elif valeur==15:
                print("E", end=" ")
            elif valeur==16:
                print("F", end=" ")
            elif valeur==17:
                print("G", end=" ")
            elif valeur==18:
                print("H", end=" ")
            elif valeur==19:
                print("I", end=" ")
            elif valeur==20:
                print("J", end=" ")
            elif valeur==21:
                print("K", end=" ")
            elif valeur==22:
                print("L", end=" ")
            elif valeur==23:
                print("O", end=" ")
            elif valeur==24:
                print("P", end=" ")
            elif valeur==25:
                print("Q", end=" ")
            elif valeur==26:
                print("R", end=" ")
            elif valeur==27:
                print("S", end=" ")
            elif valeur==28:
                print("T", end=" ")
            elif valeur==29:
                print("U", end=" ")
            elif valeur==30:
                print("V", end=" ")
            elif valeur==31:
                print("W", end=" ")
            elif valeur==32:
                print("X", end=" ")
            elif valeur==33:
                print("Y", end=" ")
            elif valeur==34:
                print("Z", end=" ")
            elif valeur==35:
                print("a", end=" ")
            elif valeur==36:
                print("b", end=" ")
            elif valeur==37:
                print("c", end=" ")
            elif valeur==38:
                print("d", end=" ")
            elif valeur==39:
                print("e", end=" ")
            elif valeur==40:
                print("f", end=" ")
            elif valeur==41:
                print("g", end=" ")
            elif valeur==42:
                print("h", end=" ")
            elif valeur==43:
                print("i", end=" ")
            elif valeur==44:
                print("j", end=" ")
            elif valeur==45:
                print("k", end=" ")
            elif valeur==46:
                print("l", end=" ")
            elif valeur==47:
                print("m", end=" ")
            elif valeur==48:
                print("n", end=" ")
            elif valeur==49:
                print("o", end=" ")
            elif valeur==50:
                print("p", end=" ")
            elif valeur==51:
                print("q", end=" ")
            elif valeur==52:
                print("r", end=" ")
            elif valeur==53:
                print("s", end=" ")
            elif valeur==54:
                print("t", end=" ")
            elif valeur==55:
                print("u", end=" ")
            elif valeur==56:
                print("v", end=" ")
            elif valeur==57:
                print("w", end=" ")
            elif valeur==58:
                print("x", end=" ")
            elif valeur==59:
                print("y", end=" ")
            elif valeur==60:
                print("z", end=" ")
            elif valeur==61:
                print("~", end=" ")
            elif valeur==62:
                print("(", end=" ")
            elif valeur==63:
                print(")", end=" ")
            elif valeur==64:
                print("_", end=" ")
            elif valeur==65:
                print("&", end=" ")
            elif valeur==66:
                print("²", end=" ")
            elif valeur==67:
                print("*", end=" ")
            elif valeur==68:
                print("µ", end=" ")
            elif valeur==69:
                print("ù", end=" ")
            elif valeur==70:
                print("%", end=" ")
            elif valeur==71:
                print("!", end=" ")
            elif valeur==72:
                print("§", end=" ")
            elif valeur==73:
                print(":", end=" ")
            elif valeur==74:
                print("?", end=" ")
            elif valeur==75:
                print("<", end=" ")
            elif valeur==76:
                print(">", end=" ")
            elif valeur==77:
                print("^", end=" ")
            elif valeur==78:
                print("¨", end=" ")
            elif valeur==79:
                print("¤", end=" ")
            elif valeur==80:
                print("°", end=" ")
            elif valeur==81:
                print("+", end=" ")
            elif valeur==82:
                print("≤", end=" ")
            elif valeur==83:
                print("≥", end=" ")
            elif valeur==84:
                print("∓", end=" ")
            elif valeur==85:
                print("∞", end=" ")
            elif valeur==86:
                print("±", end=" ")
            elif valeur==87:
                print("≠", end=" ")
            elif valeur==88:
                print("∝", end=" ")
            elif valeur==89:
                print("∀", end=" ")
            elif valeur==90:
                print("≡", end=" ")
            elif valeur==91:
                print("≪", end=" ")
            elif valeur==92:
                print("≫", end=" ")
            elif valeur==93:
                print("≅", end=" ")
            elif valeur==94:
                print("≈", end=" ")
            elif valeur==95:
                print("℉", end=" ")
            elif valeur==96:
                print("℃", end=" ")
            elif valeur==97:
                print("∇", end=" ")
            elif valeur==98:
                print("√", end=" ")
            elif valeur==99:
                print("←", end=" ")
            elif valeur==100:
                print("↑", end=" ")
            elif valeur==101:
                print("→", end=" ")
            elif valeur==102:
                print("↓", end=" ")
            elif valeur==103:
                print("⋮", end=" ")
            elif valeur==104:
                print("⋯", end=" ")
            elif valeur==105:
                print("⋰", end=" ")
            elif valeur==106:
                print("⋱", end=" ")
            elif valeur==107:
                print("∎", end=" ")
            elif valeur==108:
                print("∅", end=" ")
            elif valeur==109:
                print("∑", end=" ")
            elif valeur==110:
                print("⋈", end=" ")
            elif valeur==111:
                print("⨀", end=" ")
            elif valeur==112:
                print("⨂", end=" ")
            elif valeur==113:
                print("⨁", end=" ")
            elif valeur==114:
                print("⨄", end=" ")
            elif valeur==115:
                print("⨃", end=" ")
            elif valeur==116:
                print("∔", end=" ")
            elif valeur==117:
                print("∸", end=" ")
            elif valeur==118:
                print("⋒", end=" ")
            elif valeur==119:
                print("⋓", end=" ")
            elif valeur==120:
                print("⊟", end=" ")
            elif valeur==121:
                print("⊠", end=" ")
            elif valeur==122:
                print("⊡", end=" ")
            elif valeur==123:
                print("⊞", end=" ")
            elif valeur==124:
                print("⋉", end=" ")
            elif valeur==125:
                print("⋊", end=" ")
            elif valeur==126:
                print("⋇", end=" ")
            elif valeur==127:
                print("⊝", end=" ")
            elif valeur==128:
                print("⊕", end=" ")
            elif valeur==129:
                print("⊖", end=" ")
            elif valeur==130:
                print("⊗", end=" ")
            elif valeur==131:
                print("⊘", end=" ")
            elif valeur==132:
                print("⊙", end=" ")
            elif valeur==133:
                print("⊛", end=" ")
            elif valeur==134:
                print("⊚", end=" ")
            elif valeur==135:
                print("†", end=" ")
            elif valeur==136:
                print("‡", end=" ")
            elif valeur==137:
                print("⨂", end=" ")
            elif valeur==138:
                print("△", end=" ")
            elif valeur==139:
                print("⋘", end=" ")
            elif valeur==140:
                print("⋙", end=" ")
            elif valeur==141:
                print("≦", end=" ")
            elif valeur==142:
                print("≧", end=" ")
            elif valeur==143:
                print("⋖", end=" ")
            elif valeur==144:
                print("⋗", end=" ")
            elif valeur==145:
                print("≑", end=" ")
            elif valeur==146:
                print("≒", end=" ")
            elif valeur==147:
                print("≓", end=" ")
            elif valeur==148:
                print("⊲", end=" ")
            elif valeur==149:
                print("⊳", end=" ")
            elif valeur==150:
                print("⊴", end=" ")
            elif valeur==151:
                print("⊵", end=" ")
            elif valeur==152:
                print("⋐", end=" ")
            elif valeur==153:
                print("⋑", end=" ")
            elif valeur==154:
                print("❤",end=" ")
        print()
t1=[[1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,0,2,0,1],
    [1,0,1,0,0,0,0,1],
    [1,0,0,0,1,152,3,1],
    [1,0,1,1,1,0,0,1],
    [1,0,0,3,0,0,0,1],
    [1,0,0,0,0,153,0,1],
    [1,1,1,1,1,1,0,1]]
t2=[[1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,0,0,0,1],
    [1,0,0,1,0,2,0,1],
    [1,0,0,1,0,1,3,1],
    [1,0,0,0,0,3,0,1],
    [1,0,1,1,1,1,5,1],
    [1,0,0,0,0,150,4,1],
    [1,1,1,0,1,1,1,1]]
t3=[[3,0,3,3,3,3,3,3],
    [3,0,0,0,0,0,0,3],
    [3,6,6,6,0,6,6,3],
    [3,6,0,6,0,0,0,3],
    [3,0,0,0,0,6,6,3],
    [3,0,6,6,0,0,0,3],
    [3,0,0,0,6,6,6,3],
    [3,6,6,0,0,0,0,3],
    [3,3,3,3,3,3,0,3]]
ee4=[[1,2,1,1,1,1,1,1,1],
     [1,2,1,2,1,2,2,2,2],
     [1,2,2,2,2,2,1,2,1],
     [1,1,1,1,1,1,1,2,1]]
ee5=[[1,2,1,1,1,1,1,1,1],
     [1,2,2,2,2,2,2,2,1],
     [1,2,1,2,1,2,1,2,1],
     [1,1,1,1,1,1,1,2,1]]
ee6=[[1,2,1,3,1,1,3,1,1],
     [1,2,1,1,21,1,2,2,2],
     [1,2,2,2,2,2,2,11,2],
     [1,1,1,1,1,1,1,21,2]]
ee7=[[1,1,1,1,1,1,1,0],
     [1,2,3,4,5,0,0,0],
     [1,56,57,59,0,0,60,154],
     [1,99,0,0,0,154,140,149],
     [1,2,0,34,111,133,122,88],
     [1,0,0,22,145,144,124,134],
     [1,0,11,11,123,134,99,19],
     [1,0,23,151,154,123,129,1]]
ee8=[[1,2,3,4,5,6,7,7,5],
     [1,2,3,2,2,2,1,2,3],
     [1,2,2,2,3,2,2,2,113],
     [1,1,1,4,4,5,3,2,1]]
ea9=[[1,2,3,4,5,6,6,4,3],
     [3,2,3,4,3,2,3,2,3],
     [1,2,2,2,2,2,2,2,1],
     [1,2,3,2,4,4,5,2,6],
     [6,6,7,7,8,8,9,2,1]]
while st=="o":
    maaze=input("Pour quitter tape 'q'\nDans le jeux, tu pourras être amené(e) a suivre des '@' ou des '.' tout les autres symboles vont te bloquer.\nL'entrée se trouve sur la première ligne et le sortie sur la dernière ligne il n'y a pas de sorties ou d'entrée autre part.\nQuel labyrinthe veux-tu afficher: [labyrinthe: 1, 2, 3, 4, 5, 6, 7, 8, 9]?")
    if maaze=="1":
        maze(t1,9,8)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="2":
        maze(t2,9,8)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="3":
        maze(t3,9,8)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print("dis-moi, sur WhatsApp, où tu plante")
    elif maaze=="4":
        maze(ee4,4,9)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="5":
        maze(ee5,4,9)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="6":
        maze(ee6,4,9)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="7":
        maze(ee7,8,8)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="8":
        maze(ee8,4,9)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="9":
        maze(ea9,5,9)
        Pause()
        resolu=input("L'avez-vous résolu? [(o)ui/(n)on]")
        if resolu=="o":print(happy)
        elif resolu=="n":
            print(sad)
    elif maaze=="q":
        print ("Au revoir\nCréé par Henry Letellier\n._______.\n|       |\n| °   ° |\n|   |   |\n|\\_____/|\n|_______|")
        sleep(5)
        st="n"
    else:
        print("Merci de rentrer un chiffre entier compris entre {} et {} ou d'avoir tapé 'q'.\nVous avez entré {}".format(mini,maxi,maaze))
