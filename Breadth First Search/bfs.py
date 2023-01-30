from collections import deque

class BFS:
	def __init__(self) :
		self.__graph={}
		self.__source_node=0
		self.__target_node=0
		self.__path=[]

	def __str__(self):
		return "Source node: {}\n Destination node: {}.format(self.__source_node,self__target_node) "

	def bfs(self,graph,src_node,dest_node):
		self.__target_node=dest_node
		self.__source_node=src_node
		self.__graph=graph
		queue = deque()
		que =deque()
		found=False
		queue.append(self.__source_node)
		keys=list(self.__graph)
		if queue[0]==self.__target_node:
			self.path.append(queue.popleft())
		else:
			while(found==False):
				que=queue.copy()

				for j in range(len(que)):
					if que[j]==self.__target_node:
						found=True
						self.__path.append(queue.popleft())
						break
					elif que[j] not in keys:
						self.__path.append(queue.popleft())
					elif que[j] in keys:
						for l  in range(len(self.__graph[que[j]])):
							if self.__graph[que[j]][l] not in queue and self.__graph[que[j]][l] not in self.__path:
								queue.append(self.__graph[que[j]][l])
						self.__path.append(queue.popleft())
				if len(queue)==0:
					break
		if found==True:
			print("BFS:Optimal path from {} to {} is {} after traversing: {} nodes".format(self.__source_node,self.__target_node,self.__path,len(self.__path)))
			print('-'*50)
		elif found==False:
			print("BFS:Target {} is NOT reachable from source {} using BFS".format(self.__target_node,self.__source_node)) 
		del queue
		del que
