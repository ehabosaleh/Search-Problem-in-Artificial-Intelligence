from collections import deque
class UCS:   
   optimal_path=[]
   graph={}
   cost={}
   pos=0
   def ucs(self,src_node,dest_node): 
        queue=[]
        path=[]
        total_cost=[0]
        found=False
        queue.append(src_node)
        self.optimal_path.append([src_node])
        keys=list(self.graph)
        while(len(queue)!=0):                              
                  nominated_node=queue[total_cost.index(min(total_cost))]
                  lower_cost=min(total_cost)
                  if nominated_node==dest_node:
                    found=True
                    pos=total_cost.index(min(total_cost))
                    path.append(queue.pop(queue.index(nominated_node)))  
                    break
                  elif nominated_node not in keys:
                     path.append(queue.pop(queue.index(nominated_node))) 
                     ### attention##
                     self.optimal_path.pop(total_cost.index(min(total_cost)))
                     total_cost.pop(total_cost.index(min(total_cost)))
                  elif  nominated_node in keys:
                     V=nominated_node
                     path.append(queue.pop(queue.index(nominated_node)))
                     p=self.optimal_path[total_cost.index(min(total_cost))]
                     self.optimal_path.pop(total_cost.index(min(total_cost)))                
                     total_cost.pop(total_cost.index(min(total_cost)))
                     
                     for l  in range(len(self.graph[V])):
                        if  self.graph[V][l] not in path:
                         queue.append(self.graph[V][l])
                         total_cost.append(self.cost[V][l]+lower_cost) 

                         self.optimal_path.append(p+[self.graph[V][l]])
        if found==True:
           print("UCS:Optimal path from {} to {} is {}, with totall cost: {}\n Path was found after traversing all of these nodes:\n {}".format(src_node,dest_node,self.optimal_path[pos],min(total_cost),path))
           print('-'*50)
        elif found==False:
           print("Target {} is NOT reachable from source {}  using UCS".format(dest_node,src_node)) 
           print('-'*50) 
        del queue
