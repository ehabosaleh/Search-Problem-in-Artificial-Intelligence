import random as rn
class RandomGraph:
	__graph={}
	def __init__(self):
 		self.__graph = {}

    # function to add an edge to graph 
	def add_edge(self,u,v):
		keys=list(self.__graph)
		if u in keys:
			l=self.__graph[u]
			l.append(v)
			self.__graph[u]=l
		else:
			self.__graph[u]=[v]


	def graph_disp(self):
		keys=list(self.__graph)
		n=0
		for k in keys:
			print("{} -> {}\n".format(keys[n],self.__graph[k]))
			n+=1

	def __init__ (self,vertex_num,edge_num):
		for key in range(vertex_num): 
			lst=list(self.__graph)
			self.__graph[key]=[]
			for k in range(edge_num):
				node=rn.randint(key,vertex_num)
				if node not in self.__graph[key]:
					self.__graph[key].append(node)
