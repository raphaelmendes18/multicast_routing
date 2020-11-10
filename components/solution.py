import numpy as np
from components.graph import MulticastRoute, Graph
import random
import networkx as nx
from components.edge import Edge
from components.objective import Objective
from components.mutation import Mutation
import random
class MulticastSolution:

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

class MonoObjectiveSolution(MulticastSolution, Objective, Mutation):
    pass

            


    

