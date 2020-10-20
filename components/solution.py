import numpy as np

class Solution:

    '''
    The solution is represented by a adjancency matrix, which represents a tree, that is a valid solution for the multicast problem
    The number of objectives can vary, the algorithm to solve can also change
    '''

    def __init__(self, graph, root_node, destination_nodes):
        assert isinstance(graph,np.ndarray), 'Invalid Type for graph'
        
