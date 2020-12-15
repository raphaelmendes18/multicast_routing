import numpy as np
import networkx as nx
from components.edge import Edge
from typing import List

def generate_random_topology(num_nodes: int, num_connections: int) -> np.array:
    np.zeros(num_nodes,num_nodes)

def build_pre_defined_network(network: int):

    if network == 0:
        G = nx.Graph()

        G.add_edge(1,2,cost=7, delay=6)
        G.add_edge(1,3,cost=11, delay=4)
        G.add_edge(1,4,cost=21, delay=3)

        G.add_edge(2,5,cost=24, delay=3)
        
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

        start_node = 1
        destination_nodes = [2,9,10,13,14]
        return G, start_node, destination_nodes
    
    if network == 1:
        
        G = nx.Graph()

        G.add_edge(1, 2, cost=10, delay=2)
        G.add_edge(1, 3, cost=20, delay=1)
        G.add_edge(1, 11, cost=6, delay=4)

        G.add_edge(2, 4, cost=4, delay=1)
        G.add_edge(2, 5, cost=1, delay=3)
        G.add_edge(2, 10, cost=12, delay=9)

        G.add_edge(3, 6, cost=13, delay=4)
        G.add_edge(3, 7, cost=20, delay=1)

        G.add_edge(4, 8, cost=20, delay=1)

        G.add_edge(5, 8, cost=2, delay=3)
        G.add_edge(5, 9, cost=21, delay=2)

        G.add_edge(6, 8, cost=19, delay=1)
        
        G.add_edge(7, 8, cost=12, delay=4)
        
        G.add_edge(8, 16, cost=14, delay=2)

        G.add_edge(9, 13, cost=10, delay=2)

        G.add_edge(10, 12, cost=30, delay=1)

        G.add_edge(11, 12, cost=23, delay=1)

        G.add_edge(12, 14, cost=6, delay=9)

        G.add_edge(13, 14, cost=4, delay=1)

        G.add_edge(14, 15, cost=34, delay=2)
        G.add_edge(14, 16, cost=21, delay=1)

        G.add_edge(15, 18, cost=5, delay=3)

        G.add_edge(16, 17, cost=1, delay=1)

        G.add_edge(17, 18, cost=4, delay=1)

        start_node = 1
        destination_nodes = [7,11,14,16,18]

        return G, start_node, destination_nodes

    if network == 2:
        
        G = nx.Graph()
        # Network 1
        G.add_edge(1,2,cost=7, delay=6)
        G.add_edge(1,3,cost=11, delay=4)
        G.add_edge(1,4,cost=21, delay=3)

        G.add_edge(2,5,cost=24, delay=3)
        
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
        G.add_edge(12,19,cost=13, delay=4)
        G.add_edge(12,27,cost=20, delay=4)

        G.add_edge(13,15,cost=2, delay=3)

        G.add_edge(14,15,cost=5, delay=3)
        G.add_edge(14,18,cost=10, delay=3)
        G.add_edge(14,19,cost=5, delay=10)

        G.add_edge(15,18,cost=10, delay=2)
        G.add_edge(15,27,cost=15, delay=5)

        # Network 2
        G.add_edge(16, 17, cost=10, delay=2)
        G.add_edge(16, 18, cost=20, delay=1)
        G.add_edge(16, 26, cost=6, delay=4)

        G.add_edge(17, 19, cost=4, delay=1)
        G.add_edge(17, 20, cost=1, delay=3)
        G.add_edge(17, 25, cost=12, delay=9)

        G.add_edge(18, 21, cost=13, delay=4)
        G.add_edge(18, 22, cost=20, delay=1)

        G.add_edge(19, 23, cost=20, delay=1)

        G.add_edge(20, 23, cost=2, delay=3)
        G.add_edge(20, 24, cost=21, delay=2)

        G.add_edge(21, 23, cost=19, delay=1)
        
        G.add_edge(22, 23, cost=12, delay=4)
        
        G.add_edge(23, 31, cost=14, delay=2)

        G.add_edge(24, 28, cost=10, delay=2)

        G.add_edge(25, 27, cost=30, delay=1)

        G.add_edge(26, 27, cost=23, delay=1)

        G.add_edge(27, 29, cost=6, delay=9)

        G.add_edge(28, 29, cost=4, delay=1)

        G.add_edge(29, 30, cost=34, delay=2)
        G.add_edge(29, 31, cost=21, delay=1)

        G.add_edge(30, 33, cost=5, delay=3)

        G.add_edge(31, 32, cost=1, delay=1)

        G.add_edge(32, 33, cost=4, delay=1)

        start_node = 1
        destination_nodes = [2,9,10,13,14,22,26,29,31,33]
        return G, start_node, destination_nodes


