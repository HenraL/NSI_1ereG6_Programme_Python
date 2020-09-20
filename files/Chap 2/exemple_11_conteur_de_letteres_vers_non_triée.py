from time import sleep
texte="alioe was begining to get very tired of sitting ..."
lettres={}
for c in texte:
    if c==" ": continue
    elif c in lettres:
        lettres[c]+=1
    else:
        lettres[c]=1
for c in lettres:
    print("Nombre de {} : {}".format(c,lettres[c]))
sleep(3)