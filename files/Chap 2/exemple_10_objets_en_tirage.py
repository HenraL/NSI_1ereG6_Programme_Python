from time import sleep
from random import randint
z,result=1,0
while z<300:
    n=6
    t=0
    L0,L1,L2,L3=[],n*[0],n*[0],n*[0]
    while L1.count(0)>0:
        t+=1
        r=randint(0,n-1)
        L0.append(r)
        if L1[r]==0: L1[r]=t
        L2[r]=t
        L3[r]+=1
    y="{} objets obtenus en {} tirages\n|objets|premier|dernier|nombre|".format(n,t)
    print(y)
    # result+=int(n)
    # result+=" objets obtenus en "
    # result+=int(t)
    # result+=" tirages\n|objets|premier|dernier|nombre|"
    for i in range(n):
        print("|{:6}|{:7}|{:7}|{:6}|".format(i+1,L1[i],L2[i],L3[i]))
        # result+="|{:6}|{:7}|{:7}|{:6}|".format(i+1,L1[i],L2[i],L3[i])
    print("Liste des tirages:",[i+1 for i in L0])
    # result+="Liste des tirages:",[i+1 for i in L0]
    sleep(0.05)
    z+=1
    print("nombre de tours {}".format(z))
    # result+="nombre de tours {}".format(z)
# f=open("cache_de_exemple_10_objets_en_tirage.py.txt", "a")
# s=f.write(result)
# f.close()