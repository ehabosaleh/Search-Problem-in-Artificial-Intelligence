from collections import deque
class DFS:   
    graph={}
    path=[]
    def __init__(self):
        self.graph = {}
    def dfs(self, src_node,dest_node): 
        queue = []
        self.path=[]
        found=False
        queue.append(src_node)
        keys=list(self.graph)
        while(len(queue)!=0):
                  if queue[-1]==dest_node:
                    found=True
                    self.path.append(queue.pop())  
                    break
                  elif  queue[-1] not in keys:
                     self.path.append(queue.pop()) 
                  elif  queue[-1] in keys:
                     V=queue[-1]
                     self.path.append(queue.pop())
                     for l  in range(len(self.graph[V])):
                        if self.graph[V][l] not in self.path:
                         queue.append(self.graph[V][l])
        if found==True:
           print("Optimal path from {} to {} is {} after traversing: {} nodes".format(src_node,dest_node,self.path,len(self.path)))
        elif found==False:
           print("There is no path between nodes: {} and {} ".format(src_node,dest_node)) 
        del queue
