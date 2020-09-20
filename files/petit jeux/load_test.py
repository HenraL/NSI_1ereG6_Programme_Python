e="[___________________________________________________________________________________________________]"
j=0
i="["
le=1
for letter in e:
    f="[{}%]".format(j)
    print("{}{}".format(i, f))
    j+=1
    if le<100:
        i+="_"
    elif le==100:
        i+="_]"
    le+=1

testline="                                                                                                    "
testeight="[___________________________________________________________________________________________________]"
j=0
i="[                                                                                                    "
le=1
for letter in testeight:
    f="[{}%]".format(j)
    print("{}{}".format(i, f))
    j+=1
    if le<100:
        i=testline.replace(' ','_')
    elif le==100:
        i+="_]"
    le+=1
