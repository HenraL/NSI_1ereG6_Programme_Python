z=1
A=0
i=0
while z==1:
    i+=9999999+A
    A+=9999999+i
    print (i)
    k=str(i)
    f=open("max_number.txt", "a")
    s=f.write(k)
    f.close()
