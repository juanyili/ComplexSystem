import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class City:
	def __init__(self, name, wealth, military, population, unification):
		self.name = name
		self.wealth = wealth
		self.military = military
		self.population = population
		self.unification = unification

	def power(self):
		return (self.wealth*2 + self.population*1 + self.military*3)

	def influence(self,connections):
		self.connections=connections
		x = 0
		for c in self.connections:
			#x+=c.unification*np.absolute(np.exp(complex(0,-c.power()*100000000/self.power())))
			#x+=c.unification*(c.power()/self.power())
			x+=c.unification*c.power()
		return x


#create cities:
cities={}
cities[0]=City('Misu', 9, 12, 9, -1)
cities[1]=City('Tripoli', 12, 9, 12, -1)
cities[2]=City('Naf', 3, 9, 6, 1)
cities[3]=City('Zawi', 6, 3, 3, 1)
cities[4]=City('Zintan', 2, 6, 2, -1)

cities[5]=City('Bengha', 8, 8, 8, -1)
cities[6]=City('Tubr', 6, 4, 6, 1)
cities[7]=City('Bayda', 4, 2, 6, 1)

cities[8]=City('Murzu', 1, 2, 1, -1)
cities[9]=City('Uba', 1, 2, 2, -1)
cities[10]=City('Sab', 2, 1, 3, 1)

#control group
G=nx.Graph()
G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10])
G.add_edges_from([(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])
G.add_edges_from([(5,6),(5,7),(6,7),(4,5),(4,6),(4,7)])
G.add_edges_from([(5,6),(6,8),(7,8),(8,10),(9,10)])


#create cities:
cities1={}
cities1[0]=City('Misu', 9, 12, 9, -1)
cities1[1]=City('Tripoli', 12, 9, 12, -1)
cities1[2]=City('Naf', 3, 9, 6, 1)
cities1[3]=City('Zawi', 6, 3, 3, 1)
cities1[4]=City('Zintan', 2, 6, 2, -1)

cities1[5]=City('Bengha', 8, 8, 8, -1)
cities1[6]=City('Tubr', 6, 4, 6, 1)
cities1[7]=City('Bayda', 4, 2, 6, 1)

cities1[8]=City('Murzu', 1, 2, 1, -1)
cities1[9]=City('Uba', 1, 2, 2, -1)
cities1[10]=City('Sab', 2, 1, 3, 1)

#ISIS
cities1[11]=City('ISIS',16,24,24,1)
#experiment group
H=nx.Graph()
H.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11])
H.add_edges_from([(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])
H.add_edges_from([(5,6),(5,7),(6,7),(4,5),(4,6),(4,7)])
H.add_edges_from([(5,6),(6,8),(7,8),(8,10),(9,10)])
H.add_edges_from([(11,0),(11,2),(11,3),(11,4),(11,5),(11,5),(11,7),(11,8),(11,9),(11,10)])

def run_model(G, group, filename, picturename):
	dynamics=[]
	initial = [group[i].unification for i in range (11)]
	dynamics.append(initial)
	for t in range(10):
		uni=[]
		for i in range(11):
			Idx =  G.neighbors(i)
			connections = {group[i] for i in Idx}
			x = group[i].influence(connections)
			if (np.absolute(x)>= group[i].unification) and (np.sign(x)-group[i].unification != 0):
				group[i].unification = np.sign(x)
			uni.append(group[i].unification)
		dynamics.append(uni)

	ar = np.array(dynamics)
	import csv
	fl = open(filename, 'w')

	writer = csv.writer(fl)
	for values in ar:
	    writer.writerow(values)
	fl.close()

	plt.pcolor(ar)
	plt.savefig(picturename)


#no isis
run_model(G, cities,'noisis1.csv','2dnoisis1.png')

#with isis
run_model(H, cities1,'withisis1.csv','2dwithisis1.png')
