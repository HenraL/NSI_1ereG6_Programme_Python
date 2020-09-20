from time import sleep
U=int(input("Entrez la valeur de U0:"))
N=int(input("Entrez le nombre de fois que l'on calculera Un(N>0):"))
if N==0:
    print ("N est maintenant égal à 1")
    N=1
elif N<0:
    print ("N est maintenant égal à 1")
    N=1
k=1
for i in range(N):
    U=1/(1+U)
    print("U{}={}".format(k,U))
    k+=1
sleep(10)
print("Créé par Henry Letellier")
sleep(5)
