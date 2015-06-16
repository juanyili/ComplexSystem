
import numpy as np
import matplotlib as plt
from pylab import *
L=10
p = 0.5
mat=np.random.choice([0, 1], size=(L,L), p=[p,1-p])
pcolor(mat)
show()