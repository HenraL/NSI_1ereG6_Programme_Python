from time import sleep
n,solutions,soolutions=181341,0,"=======solutions de Sam Loyd=======\n"
for a in range(10):
    for b in range(10):
        if b==a: continue
        for c in range(10):
            if c==b or c==a: continue
            for d in range(10):
                if d==c or d==b or d==a: continue
                for e in range(10):
                    if e==d or e==c or e==b or e==a: continue
                    for f in range(10):
                        if f==e or f==d or f==c or f==b or f==a: continue
                        for g in range(10):
                            if g==f or g==e or g==d or g==c or g==b or g==a: continue
                            for h in range(10):
                                if h==g or h==f or h==e or h==d or h==c or h==b or h==a: continue
                                for i in range(10):
                                    if i==h or i==g or i==f or i==e or i==d or i==c or i==b or i==a: continue
                                    j=45-(a+b+c+d+e+f+g+h+i)
                                    num1,num2=a*10**4+b*10**3+c*10**2+d*10**1+e,f*10**4+g*10**3+h*10**2+i*10+j
                                    if num1+num2==n and num1<num2:
                                        solutions+=1
                                        print("solution {}:{}+{}={}".format(solutions,num1,num2,n))
                                        soolutions+="solution {}:{}+{}={}\n".format(solutions,num1,num2,n)
if solutions==0: print("Pas de solution")
soolutions+="Edité par Henry Letellier"
f=open("solutions_de_Sam_Loyd.txt", "a")
s=f.write(soolutions)
f.close()
sleep(10)
