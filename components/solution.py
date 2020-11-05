import numpy as np
from components.graph import MulticastRoute, Graph
import random
import networkx as nx
from components.edge import Edge
from components.objective import Objective
import random
class Solution:

    '''
    The solution is represented by a adjancency matrix, which represents a tree, that is a valid solution for the multicast problem
    The number of objectives can vary, the algorithm to solve can also change
    '''

    def __init__(self, graph, root_node, destination_nodes, max_delay = 25, alpha=0.5, omega=1, build_tree=True):
        assert isinstance(graph,Graph), 'Invalid Type for graph'
        if build_tree:
            self.multicast_tree = MulticastRoute(graph, root_node, destination_nodes)
        else:
            self.multicast_tree = MulticastRoute(graph, root_node, destination_nodes, build_tree=False)
        self.max_delay = max_delay
        self.alpha = alpha
        self.omega = omega
        
    def w(self, delay):
        return 1.0 if delay <= self.max_delay else self.alpha

    def mutation(self, number_of_disconnections, G):
        # 1. Select Edges to be removed
        edges_to_remove = int(len(list(self.multicast_tree.edges()))*number_of_disconnections)
        edges_removed = 0
        while edges_removed < edges_to_remove:
            edges = list(self.multicast_tree.edges())
            random_edge_to_remove = random.choice(edges)
            self.multicast_tree.remove_edge(random_edge_to_remove)
            edges_removed += 1
        self.multicast_tree.reconnect(G)
        # print(f'Has Cycle? {self.multicast_tree.has_cycle()}')
        # self.multicast_tree.draw()
class MonoObjectiveSolution(Solution, Objective):
    pass

            


    

