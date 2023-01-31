import random as rn
class RandomGraph:
  graph={}
  def __init__(self):
    self.graph = {}
  
    # function to add an edge to graph 
  def add_edge(self,u,v):
        keys=list(self.graph)    
        if u in keys:
           l=self.graph[u]
           l.append(v)
           self.graph[u]=l
        else:
           self.graph[u]=[v]


  def graph_disp(self):
        keys=list(self.graph) 
        n=0
        for k in keys:
          print("{} -> {}\n".format(keys[n],self.graph[k]))
          n+=1
          
  def __init__ (self,vertex_num,edge_num):
      
       for key in range(vertex_num): 
         lst=list(self.graph)
         self.graph[key]=[]
         for k in range(edge_num):
              node=rn.randint(key,vertex_num)
              if node not in self.graph[key]:
                self.graph[key].append(node)
