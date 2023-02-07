from ucs import UCS
from random_graph import RandomGraph
import time
t=RandomGraph(100,3)
print(t.graph)
print(t.cost)
g=UCS()
g.graph=t.graph
g.cost=t.cost
#g.graphDisp()
time1=time.time()
g.ucs(0,90)
time2=time.time()
print("executing time is: {} ".format(time2-time1))
