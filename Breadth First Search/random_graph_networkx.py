import networkx as nx
import random as rn
import matplotlib.pyplot as plt


class RandomGraph():
	def convert(self,tup):
		di={}
		for a, b in tup:
			di.setdefault(a, []).append(b) 
		return di
	def graph_disp(self):
		#pos = nx.circular_layout(self.__graph) 
		nx.draw(self.__graph, with_labels=True,arrowsize=10,arrow=True)
		plt.show()
	"""	
	def graph_disp(self,path):
		pos=nx.spring_layout(self.__graph)
		nx.draw(self.__graph,pos,node_color='r',with_labels=True,alpha=0.8)
		nx.draw_networkx_nodes(self.__graph,pos,nodelsit=path,edge_color='b',with_labels=True,alpha=0.8)
		plt.show()
	"""
	def add_edge(self,node_1,node_2):
		self.__graph.add_edge(node_1,node_2)

	def add_node(self,node):
		self.__graph.add_node(node)

	def __init__(self):
		self.__graph=nx.DiGraph()
	def __init__(self,vertex_num,edge_num):
		self.__graph=nx.DiGraph()
		for key in range(vertex_num):
			self.add_node(key)
			for k in range(edge_num):
				node=rn.randint(key,vertex_num)
				self.add_edge(key,node)
g=RandomGraph(25,5)
print(g.convert(list(g._RandomGraph__graph.edges())))
g.graph_disp()
