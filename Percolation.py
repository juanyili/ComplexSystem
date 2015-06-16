from pylab import *
from scipy.ndimage import measurements
import matplotlib as plt
import numpy as np
 
L = 100
r = rand(L,L)
p = 0.4
print r.max()
print r.min()
mat = np.zeros((L,L))
for i in range(L):
	for j in range(L):
		if r[i,j] < p * (r.max()-r.min()):
			mat[i,j] = 1
		else:
			mat[i,j] = 0
#showing in two colors
pcolor(mat)
show()
