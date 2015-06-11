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
			x+=c.unification*np.absolute(np.exp(complex(0,-c.power()*100000000/self.power())))
		return x


#create cities:
cities={}
cities[0]=City('Misu', 9, 12, 9, -1)
cities[1]=City('Tripoli', 12, 9, 12, 1)
cities[2]=City('Naf', 3, 9, 6, -1)
cities[3]=City('Zawi', 6, 3, 3, 1)
cities[4]=City('Zintan', 2, 6, 2, -1)

cities[5]=City('Bengha', 8, 8, 8, -1)
cities[6]=City('Tubr', 6, 4, 6, 1)
cities[7]=City('Bayda', 4, 2, 6, -1)

cities[8]=City('Murzu', 1, 2, 1, -1)
cities[9]=City('Uba', 1, 2, 2, 1)
cities[10]=City('Sab', 2, 1, 3, -1)

#ISIS
cities[11]=City('ISIS',16,24,24,1)



#control group
G=nx.Graph()
G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10])
G.add_edges_from([(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])
G.add_edges_from([(5,6),(5,7),(6,7),(4,5),(4,6),(4,7)])
G.add_edges_from([(5,6),(6,8),(7,8),(8,10),(9,10)])

dynamicsnoisis=[]
initial = [cities[i].unification for i in range (11)]
dynamicsnoisis.append(initial)
for t in range(50):
	uni=[]
	for i in range(11):
		Idx =  G.neighbors(i)
		connections = {cities[i] for i in Idx}
		x = np.sign(cities[i].influence(connections))
		cities[i].unification = x
		#print x
		#print np.sign(cities[i].unification)
		#if (x - np.sign(cities[i].unification))!=0:
		#	cities[i].unification= x
		uni.append(cities[i].unification)
	dynamicsnoisis.append(uni)
	#print "Without ISIS, how does Libya look like"
	#print "At time %s, unification dynamics is %s." % (t, uni)

ar = np.array(dynamicsnoisis)
import csv
fl = open('dynamicsnoisis.csv', 'w')

writer = csv.writer(fl)
for values in ar:
    writer.writerow(values)
fl.close()



#experiment group
H=nx.Graph()
H.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11])
H.add_edges_from([(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])
H.add_edges_from([(5,6),(5,7),(6,7),(4,5),(4,6),(4,7)])
H.add_edges_from([(5,6),(6,8),(7,8),(8,10),(9,10)])
H.add_edges_from([(11,0),(11,2),(11,3),(11,4),(11,5),(11,5),(11,7),(11,8),(11,9),(11,10)])

dynamics=[]
initial = [cities[i].unification for i in range (11)]
dynamics.append(initial)
for t in range(50):
	uni=[]
	for i in range(11):
		Idx =  H.neighbors(i)
		connections = {cities[i] for i in Idx}
		x = np.sign(cities[i].influence(connections))
		cities[i].unification = x
		#if cities[i].influence(connections) != np.sign(cities[i].unification):
		#	cities[i].unification= -cities[i].unification
		uni.append(cities[i].unification)
	dynamics.append(uni)

#print "With ISIS how does Libya look like?"
	#print "At time %s, unification dynamics is %s." % (t, uni)
#print dynamics

ar = np.array(dynamics)
import csv
fl = open('dynamics5.csv', 'w')

writer = csv.writer(fl)
for values in ar:
    writer.writerow(values)
fl.close()
