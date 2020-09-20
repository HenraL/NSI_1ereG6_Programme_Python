z="o"
while z=="o":
    for i in [0,1]:
        for j in [0,1]:
            for k in [0,1]:
                print("{} or {} and {}={}".format(i,j,k,i or j and k),end='')
                print("-{} or ({} and {})={}".format(i,j,k,i or (j and k)), end='')
                print("-({} or {} and {}={}".format(i,j,k,(i or j) and k))
    z=input("Continuer? [(o]ui/(n)on]:")

