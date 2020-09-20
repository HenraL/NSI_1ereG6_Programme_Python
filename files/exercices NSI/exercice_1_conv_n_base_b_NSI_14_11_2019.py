from math import sqrt

print("""exercice 1 NSI 1ere 6 Cours Hattemer\nconvertir n (donné en base i) en base b""")

def convert (n,b,i=10):
    assert 1<b<37, "la base doit être comprise entre 2 et 36"
    result=""
    if i!=10: n=int(str(n),i) #convertion de n en base 10
    while n>0:
        if n%b<10:
            result=str(n%b)+result #concaténation du reste par la gauche
        else:
            result=chr(87+n%b)+result #même chose quand le reste dépasse un chiffre
        n=n//b
    return result

n,b=2020,7
print("{} en base {} s'écrit {}".format(n,b,convert(n,b)))
n,b=2020,16
print("{} en base {} s'écrit {}".format(n,b,convert(n,b)))
n,b,i='7e4',10,16
print("{} en base {} s'écrit {}".format(n,b,convert(n,b,i)))
n,b,i='7e4',36,16
print("{} en base {} s'écrit {}".format(n,b,convert(n,b,i)))

print("""exercice 2: 1ère 6 cours Hattemers\n3 procédures conditionnelles""")

def boite(a,b):
    """nombre de boites nécessaires au rangement de a des objets dans des boites de b\n-> tester avec (49,10) (50,10) """
    if a%b==0:
        print("nombre de boites={}".format(a//b))
    else:
        print ("nombre de boites={}".format(a//b+1))
def trinome(a,b,c):
    """affiche la ou les solutions de ax²+bx+c=0 ou 'pas de solution'\n->tester avec (1,1,1) (1,2,1) (1,3,2)"""
    delta=b**2-4*a*c
    if delta<0:
        print("pas de solution")
    elif delta==0:
        print("deux solutions: {} ou {}".format((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)))
def intersection(a1,b1,a2,b2):
    """affiche le point d'intersection des droites y=a1*x+b1 et y=a2*x+b2 ou 'pas d'intersection' ou 'droites confondues'\n-> tester avec (1,2,1,3) (1,2,1,2) (1,2,2,1)"""
    if a1==a2:
        if b1==b2:
            print("droites confondues")
        else:
            print("Pas d'intersection")
    else:
        x=(b2-b1)/(a1-a2)
        print("une intersection ({};{})".format(x, a1*x+b1))
print ("boite, (49,10)={}\nboite, (50,10)={}".format(boite(49,10), boite(50,10)))
print ("trinome(1,1,1)={}\ntrinome(1,2,1)={}\ntrinome(1,3,2)={}".format(trinome(1,1,1), trinome(1,2,1), trinome(1,3,2)))
print ("intersection(1,2,1,3)={}\nintersection(1,2,1,2)={}\nintersection(1,2,2,1)={}".format(intersection(1,2,1,3), intersection(1,2,1,2), intersection(1,2,2,1)))
