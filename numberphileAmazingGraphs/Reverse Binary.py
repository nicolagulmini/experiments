import matplotlib.pyplot as plt
import numpy as np

def number_rev_sub(number, base):
	vec = list(range(number))
	for i in range(number):
		different_base_num = np.base_repr(i,base=base)
		rev = different_base_num[::-1]
		baseten_rev = int(rev, base)
		vec[i] = i-baseten_rev
	return vec

n = 1000
b = 9
fig = plt.figure()
plt.scatter(list(range(n)), number_rev_sub(n,b), s=1)
fig.savefig("fig.png")