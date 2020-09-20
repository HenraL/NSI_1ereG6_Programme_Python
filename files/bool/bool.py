import random
def nand(a,b):
    if a==0 and b==0:
        ab=0
        print(ab)
    elif a==0 and b==1:
        ab=1
        print(ab)
    elif a==1 and b==0:
        ab=1
        print(ab)
    elif a==1 and b==1:
        ab=1
        print(ab)
def ou(a,b):
    if a==0 and b==0:
        ab=0
        print(ab)
    elif a==1 and b==0:
        ab=1
        print(ab)
    elif a==0 and b==1:
        ab=1
        print(ab)
    elif a==1 and b==1:
        ab=0
        print(ab)
    else:
        print ("assurez-vous d'avoir entré un chiffre entier compris entre 0 et 1")
def et(a,b):
    if a==0 and b==0:
        ab=0
        print(ab)
    elif a==1 and b==0:
        ab=0
        print(ab)
    elif a==0 and b==1:
        ab=0
        print(ab)
    elif a==1 and b==1:
        ab=1
        print(ab)
iiii="O"
while iiii=="o" or iiii=="O" or iiii=="0":
    a=input("Entrez a:")
    if a=="1" or a=="0":
        a=int(a)
        b=input("Entrez b:")
        if b=="1" or b=="0":
            b=int(b)
            ii="O"
            while ii=="o" or ii=="O" or ii=="0":
                boool=input("Entrez nand(a) ou nand(b) ou nand(a,b) ou ou(a,b) ou et(a,b) ou nand(nand(a,b),nand(a,b)) [raccourcit 'nandnandnand']:")
                print(boool)
                if boool=="nand(nandab,nandab)" or boool=="'nand(nandab,nandab)'" or boool=="nand(nand(a,b),nand(a,b))" or boool=="[raccourcit 'nandnandnand']" or boool=="'nandnandnand'" or boool=="nandnandnand":
                    # nandab1=nandab2=nand(a,b)
                    # if nandab1==1 and nandab2==1:
                    #     nandab=0
                    #     print (nandab)
                    #     #print("nand(nand(a,b),nand(a,b))={}".format(nandab))
                    # elif nandab1==0 and nandab2==0:
                    #     nandab=1
                    #     print (nandab)
                    #     #print("nand(nand(a,b),nand(a,b))={}".format(nandab))
                    print ("non disponible actuellement")
                elif boool=="et(a,b)" or boool=="'et(a,b)'":
                    print ("a et b={}".format(et(a,b)))
                    ii="n"
                elif boool=="ou(a,b)" or boool=="'ou(a,b)'":
                    print ("a ou b={}".format(ou(a,b)))
                    ii="n"
                elif boool=="nand(a,b)" or boool=="'nand(a,b)'":
                    print("nand(a,b)={}".format(nand(a,b)))
                    ii="n"
                elif boool=="nand(b)" or boool=="'nand(b)'":
                    if b==0:
                        b=1
                        print("b={}".format(b))
                    elif b==1:
                        b=0
                        print("b={}".format(b))
                    ii="n"
                elif boool=="nand(a)" or boool=="'nand(a)'":
                    print (boool)
                    if a==0:
                        a=1
                        print("a={}".format(a))
                    elif a==1:
                        a=0
                        print("a={}".format(a))
                    ii="n"
                else:
                    print ("Assurez-vous d'avoir entré soit 'nand(a)' ou 'nand(b)' ou 'nand(a,b)' ou 'ou(a,b)' ou 'et(a,b)' ou 'nand(nandab,nandab)' ou 'nand(nand(a,b),nand(a,b))' ou 'nandnandnand']")
                    ii="o"
        else:
            print ("Assurez-vous d'avoir entré un chiffre entier compris entre 0 et 1\nVous avez entré '{}'".format(b))
            continue
    else:
        print ("Assurez-vous d'avoir entré un chiffre entier compris entre 0 et 1\nVous avez entré '{}'".format(a))
        continue

