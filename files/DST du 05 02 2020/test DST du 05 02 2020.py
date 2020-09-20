#def somme(tab):
#    s=0
#    for i in range(len(tab)):
#        s+=tab[i]
#    return s
#
#print(somme([10,11,12,13,14]))

#5
#print([n*n for n in range(10)])
#Ports={'http':80, 'imap':142, 'smtp':25}
#print(Ports)
#Ports['ftp']=21
#print(Ports)
#print(ports['ftp'])
#print(Ports['ftp'])

Repertoire=[{'nom':'Dupont', 'tel':'5234'},
            {'nom':'Tournesol', 'tel':'5248'},
            {'nom':'Dupond','tel':'3452'}]
#try:
#    print(Repertoire[1]['tel'])
#    print("Repertoire[1]['tel']")
#except:
#    print("pas la a")

#try:
#    print(Repertoire['Tournesol'])
#    print("Repertoire['Tournesol']")
#except:
#    print("pas la b")

#try:
#    print(Repertoire['tel'][1])
#    print("Repertoire['tel'][1]")
#except:
#    print("pas la c")

#try:
#    print(Repertoire['Tournesol']['tel'])
#    print("Repertoire['Tournesol']['tel']")
#except:
#    print("pas la d")

#for i in range(len(Repertoire)):
#    try:
#        if Repertoire[i]['nom']=='Dupond':
#            print(Repertoire[i]['tel'])
#            print("Repertoire[i]['nom']=='Dupond', a")
#    except:
#        print("pas la a")

#    try:
#        if Repertoire['nom']=='Dupond':
#            print(Repertoire[i]['tel'])
#            print("Repertoire['nom']=='Dupond', b")
#    except:
#        print("pas la b")
#
#    try:
#        if Repertoire[i]=='Dupond':
#            print(Repertoire[i]['tel'])
#            print("Repertoire[i]=='Dupond', c")
#    except:
#        print("pas la c")
#
#    try:
#        if nom=='Dupond':
#            print(Repertoire[i]['tel'])
#        print("nom=='Dupond', d")
#    except:
#        print("pas la d")


Image=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
for i in range(4):
    for j in range(4):
        if (i+j)==3:
            Image[i][j]=1
#print(Image)

table=[12,43,6,22,37]
for i in range(len(table)-1):
    if table[i]>table[i+1]:
        table[i],table[i+1]=table[i+1],table[i]
        print(table[i],table[i+1])


from turtle import*
a=0
while a<10:
     a+=1
     forward(10*a)
     left(90)
     
