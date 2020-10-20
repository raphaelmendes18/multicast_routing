import numpy as np
import random
from components.edge import Edge
class Graph:

    def __init__(self, graph_matrix=None, num_nodes=None, num_connections=None):
        
        if graph_matrix is None:
            assert num_nodes is not None, 'Number of Nodes is Mandatory'
            assert num_connections is not None, 'Number of Connections is Mandatory'
            self.num_nodes = num_nodes
            self.graph = self.__generate_random_graph(num_nodes, num_connections)
        else:
            assert isinstance(graph_matrix, list), 'Invalid type for graph_matrix'
            self.graph = graph_matrix
            self.num_nodes = graph_matrix.shape[0]

    def get_number_of_nodes(self):        
        return self.num_nodes

    def __generate_random_graph(self, num_nodes, num_connections, min_weight=1, max_weight=10):
        assert num_connections >= num_nodes - 1, 'Invalid number of connections, need to be at least num_connections >= num_nodes - 1'
        assert num_connections <= (num_nodes*(num_nodes-1))/2, 'Invalid number of connections, need to be maximum of num_nodes*(num_nodes-1)/2 (bidirectional graph)'

        self.graph = np.empty(shape=(num_nodes,num_nodes), dtype=object)
        connections = self.get_number_of_connections()

    def add_connection(self, a, b, **kwargs):
        self.graph[a,b] = Edge(a, b, **kwargs)
        self.graph[b,a] = Edge(b, a, **kwargs)

    def DepthFirstSearch(self, v, visited): 
        # Mark the current node as visited
        visited[v] = True
        for idx, edge in enumerate(self.graph[v,:]):
            if edge:
                if visited[idx]==False: 
                    self.DepthFirstSearch(idx, visited)

    def is_fully_connected(self):
        visited = [False]*self.num_nodes
        self.DepthFirstSearch(0,visited)
        if any(i == False for i in visited): 
            return False
        return True

    def is_connected(self, a, b):
        return self.graph[a,b] != None

    def remove_connection(self, a, b):
        self.graph[a,b] = None
        self.graph[b,a] = None
        

    def get_number_of_connections(self):
        connections = 0
        for i in self.graph.shape[0]:
            for j in self.graph.shape[1]:
                if self.graph[i,j] != None:
                    connections += 1
        return int(connections/2)

    def get_path(self, a, b):
        '''
        returns the shortest path between two vertices, using dijkstra algorithm
        '''
        pass

