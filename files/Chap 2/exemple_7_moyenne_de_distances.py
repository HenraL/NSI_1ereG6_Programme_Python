from random import random
from math import sqrt
N,Total=1000,0
for I in range(N):
    distance=0
    for J in range(2):
        P=random()
        Q=random()
        distance+=(P-Q)**2
    distance=sqrt(distance)
    Total+=distance
print("Moyenne des distances={}".format(Total/N))