import networkx as nx 
import matplotlib.pyplot as plt 
import pandas as pd

g=nx.read_edgelist('facebook_combined.txt',create_using=nx.Graph(),nodetype=int)
sp=nx.spring_layout(g)
print (nx.info(g))

nx.draw_networkx(g,pos=sp,with_labels=False,node_size=35)
plt.show()