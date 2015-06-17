from pylab import *
from scipy.ndimage import measurements
import matplotlib.pyplot as plt
import numpy as np

sucarray=[]
prob=[]
L=30
for p in np.arange(0.4,0.98,0.01):
	prob.append(p)

	success = 0. # keep track of number of successful paths
	for i in range(100):
		#generate a new random matrix
		a = False
		while a == False:
			mat=np.random.choice([0, 1], size=(L,L), p=[1-p,p])
			if np.sum(mat[0])>0:
				a = True

		# choose a random cell in the top roll that is 1
		pos = 0
		while pos == 0:
			x,y = 0, np.random.randint(0,L)
			pos = mat[x,y]
		old = 0
		flag = 0 # while it does not reach the bottom
		# create an array of number of cells each run has gone through
		while flag == 0 and x<L-1:
			if mat[x+1,y] == 1: # go down
				x += 1
				old = 0
			else:
				if old == 0:
					nextdir = np.random.choice([-1,1])#go left or right
					if mat[x,(y+nextdir)%L] == 1: #okay to go
						old = +nextdir
						y = (y+nextdir)%L 
					elif mat[x,(y-nextdir)%L] == 1:
						old = -nextdir
						y = (y-nextdir)%L #change to the other side if not okay
					else: flag = 1 #terminates the run
				else:
					if mat[x,(y+old)%L] == 1: #okay to go
						y = (y+old)%L 
					else: flag = 1 #terminates
			if x == L-1:
				success += 1.
	sucarray.append(success/100)

plot(prob,sucarray,'bo')

show()