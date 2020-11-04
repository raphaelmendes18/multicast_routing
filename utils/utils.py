import numpy as np
import networkx as nx
from components.edge import Edge

def generate_random_topology(num_nodes, num_connections):
    np.zeros(num_nodes,num_nodes)

def build_pre_defined_network(network):

    if network == 0:
        G = nx.Graph()

        G.add_edge(1,2,cost=7, delay=6)
        G.add_edge(1,3,cost=11, delay=4)
        G.add_edge(1,4,cost=21, delay=3)

        G.add_edge(2,5,cost=14, delay=3)
        
        G.add_edge(3,5,cost=4, delay=4)
        G.add_edge(3,6,cost=2, delay=5)
        G.add_edge(3,7,cost=5, delay=3)
        
        G.add_edge(4,8,cost=14, delay=6)
        G.add_edge(4,9,cost=21, delay=3)

        G.add_edge(5,10,cost=7, delay=11)

        G.add_edge(6,10,cost=38, delay=1)
        G.add_edge(6,11,cost=3, delay=5)

        G.add_edge(7,11,cost=21, delay=3)

        G.add_edge(8,9,cost=10, delay=2)
        G.add_edge(8,11,cost=20, delay=3)

        G.add_edge(9,11,cost=13, delay=1)

        G.add_edge(10,12,cost=35, delay=4)
        G.add_edge(10,13,cost=22, delay=3)

        G.add_edge(11,13,cost=15, delay=4)

        G.add_edge(12,14,cost=6, delay=4)

        G.add_edge(13,15,cost=2, delay=3)

        G.add_edge(14,15,cost=5, delay=3)

        return G
    