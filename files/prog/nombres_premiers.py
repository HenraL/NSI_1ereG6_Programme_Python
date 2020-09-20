def conversionbase():
    reste,quotient,num,ecriture=list(),nb,nb,""
    while quotient>0:
        quotient=num//base
        reste.append(num%base)
        num=quotient
    for j in range(len(reste)): ecriture=chiffre[reste[j]}+ecriture
    return ecriture
chiffre=
