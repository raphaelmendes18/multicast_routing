import numpy as np
import random

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

        self.graph = np.random.randint(low=min_weight, high=max_weight, size=(num_nodes, num_nodes), dtype=int).tolist()
        connections = self.get_number_of_connections()

        while (connections != num_connections):
            if connections > num_connections:
                a = random.randint(0,self.num_nodes)
                b = a
                while((a == b) | (self.is_connected(a, b) == True)):
                    b = random.randint(0,self.num_nodes)
                temp_value = self.graph[a,b]
                self.remove_connection(a,b)
                if self.is_fully_connected():
                    connections -= 1
                else:


    def add_connection(self, a, b, **kwargs):
        self.graph[a,b] = Edge(kwargs)
        self.graph[b,a] = Edge(kwargs)

    def DepthFirstSearch(self, v, visited): 
        # Mark the current node as visited
        visited[v] = True
        for vertix, weight in enumerate(self.graph[v,:]):
            if weight != 0:
                if visited[vertix]==False: 
                    self.DepthFirstSearch(vertix, visited)

    def is_fully_connected(self):
        visited = [False]*self.num_nodes
        self.DepthFirstSearch(0,visited)
        if any(i == False for i in visited): 
            return False
        return True

    def is_connected(self, a, b):
        return self.graph[a,b] != 0

    def remove_connection(self, a, b):
        self.graph[a,b] = 0
        self.graph[b,a] = 0
        

    def get_number_of_connections(self):
        connections = 0
        for i in graph.shape[0]:
            for j in graph.shape[1]:
                if graph[i,j] != 0:
                    connections += 1
        return int(connections/2)

    def get_path(self, a, b):
        '''
        returns the shortest path between two vertices, using dijkstra algorithm
        '''
        pass

