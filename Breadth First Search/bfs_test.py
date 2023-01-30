from random_graph import RandomGraph
from bfs import BFS
import time
import matplotlib.pyplot as plt

g=RandomGraph(100,3)
print(g._RandomGraph__graph)
b=BFS()

time1=time.process_time()
b.bfs(g._RandomGraph__graph,0,100)
time2=time.process_time()
print("Searching time is: {} ".format(time2-time1))
