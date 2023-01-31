from dfs import DFS
from random_graph import RandomGraph
import time
t=RandomGraph(1000,30)
print(t.graph)
g=DFS()
g.graph=t.graph
#g.graphDisp()
time1=time.time()
g.dfs(250,900)
time2=time.time()
print("executing time is: {} ".format(time2-time1))
