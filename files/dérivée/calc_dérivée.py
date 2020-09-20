from math import*
main=input("eeeee")
x=input("entrez l'exposant, laisser vide si 1, x")
if x==" " or x=="":
    x=1
    print("  n-1\nnx\n={}x{}".format(x,x-1))
else:
    try:
        int(x)
        print("nx**n-1={}x{}".format(x,x-1))
    except:print("veuillez entrer un nombre.\nVous avez entré {}".format(x))


#x.isdigit()
