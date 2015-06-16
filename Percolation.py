from pylab import *
from scipy.ndimage import measurements
import matplotlib as plt
import numpy as np

# generate the random matrix with occupation probability x
L = 10 #size of the matrix
r = rand(L,L)
p = 0.8
mat = np.zeros((L,L))
for i in range(L):
	for j in range(L):
		if r[i,j] < p * (r.max()-r.min()):
			mat[i,j] = 1 #possible occupations of p
		else:
			mat[i,j] = 0 
#showing in two colors
#pcolor(mat, cmap="binary")
#show()

success = 0 # keep track of number of successful paths
for i in range(100):
	# choose a random cell in the top roll that is 1
	pos = 0
	while pos == 0:
		x,y = 0,np.random.randint(0,L)
		pos = mat[x,y]
	flag = 1 # when it reaches the bottom
	# create an array of number of cells each run has gone through
	while flag == 1 and x<L-1:
		# choose a random number out of 3 to decide the position of the next step
		nextdir = np.random.randint(0,3)
		nextx,nexty = x+1, y+nextdir-1
		x,y = nextx,nexty
		print x,y%L
		# whenever runs into a cell of 0, then terminates the run
		if mat[x,y%L]==0:
			flag =0
		# if the path reaches to the bottom, the success increases 1
		if x == L-1:
			success += 1
print 'number of successes is', success