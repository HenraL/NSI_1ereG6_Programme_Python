continu="o"
while continu=="o":
    nb=float(input("Entrer un nombre décimal:"))
    n=0
    while 2**(n+1)<=nb:
        n+=1
    for i in range(52):
        if nb>=2**n:
            print("1", end="")
            nb-=2**n
        else:
            print("0", end="")
        if n==0:
            print(",", end="")
        n-=1
    continu=input("\ncontinuer: ? [(o)ui/(n)on]")
    if continu=="n":
        break
    else:
        continue
