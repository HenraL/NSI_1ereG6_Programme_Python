from random import*
from time import sleep
def nb_succes(n,p):
	#n est le nombre de simulations
	#p est le probabilité de réussite
	c=0
	for k in range(1,n+1):
		t=random()
		if t<p:
			c=c+1
	return c

print(nb_succes(1000,0.3))
sleep(5)
