import matplotlib.pyplot as plt
import math
def FSD(l):
	n = list(range(l))
	plo = list(range(l))
	n[0]=1
	n[1]=1
	i=2
	while i < l:
		gc = int(math.gcd(int(n[i-1]),int(i)))
		if gc==1:
			n[i] = n[i-1]+i+1
		else:
			n[i] = n[i-1]//gc
		i+=1
	plt.scatter(plo, n, s=1)
	plt.ylabel('Fly straight dammit!')
	plt.show()

FSD(850)