import numpy as np
import random
from components.edge import Edge
import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, graph=None, num_nodes=None, num_connections=None):
        
        if graph is None:
            assert num_nodes is not None, 'Number of Nodes is Mandatory'
            assert num_connections is not None, 'Number of Connections is Mandatory'
            self.num_nodes = num_nodes
            self.__generate_random_graph(num_connections)
        else:
            assert isinstance(graph, nx.Graph), 'Invalid type for graph_matrix'
            self.graph = graph
            self.num_nodes = len(list(graph.nodes()))

    def get_number_of_nodes(self):        
        return len(self.graph.nodes())

    def __generate_random_graph(self, num_connections, min_weight=1, max_weight=10):
        assert num_connections >= 2*(self.num_nodes - 1), 'Invalid number of connections, need to be at least num_connections >= num_nodes - 1.'
        assert num_connections <= (self.num_nodes*(self.num_nodes-1))/2, 'Invalid number of connections, need to be maximum of num_nodes*(num_nodes-1)/2 (bidirectional graph).'
        assert num_connections % 2 == 0, 'Number of connections has to be an even number.'

        # self.graph = np.empty(shape=(self.num_nodes,self.num_nodes), dtype=object)
        self.graph = nx.Graph()
        nodes_list = np.arange(self.num_nodes)
        connections_count = 0
        node_count = 0

        # pick one node from node list
        root_node = np.random.choice(nodes_list)
        node_count += 1
        # remove node from list of nodes
        nodes_list = nodes_list[nodes_list != root_node]
        start_node = root_node
        # create basic connected graph with all nodes
        while len(nodes_list) > 0:
            new_node = np.random.choice(nodes_list)
            nodes_list = nodes_list[nodes_list != new_node]
            edge = Edge(start_node, new_node, weight=np.random.randint(min_weight, max_weight + 1))
            self.graph.add_edge(edge.start, edge.end, **edge.as_dict())
            node_count += 1
            connections_count += 2
            start_node = np.random.choice(self.graph.nodes)
        # add the remaining connections until reaches num_connections
        while connections_count < num_connections:
            a = 0
            b = 0
            while(self.is_connected(edge=(a,b)) or a==b):
                a = np.random.randint(0, self.num_nodes)
                b = np.random.randint(0, self.num_nodes)
            
            edge = Edge(a, b, weight=np.random.randint(min_weight, max_weight + 1))
            self.graph.add_edge(edge.start, edge.end, **edge.as_dict())
            connections_count += 2

    def is_connected(self, edge):
        try:
            val = self.graph.edges[edge]
            return True
        except KeyError:
            return False

    def graph_is_connected(self, graph):
        return nx.is_connected(graph)

    def path_weight(self, path, attribute):
        return nx.path_weight(self.graph, path=path, weight=attribute)

    def get_number_of_connections(self):
        return len(self.graph.edges)*2

    def shortest_path(self, source, target, weight):
        return nx.algorithms.shortest_path(G=self.graph, source=source, target=target, weight=weight, method='dijkstra')

    def get_edge(self, edge, attribute):
        return self.graph.edges[edge][attribute]

    def edges(self):
        return self.graph.edges()

    def remove_edge(self, edge):
        self.graph.remove_edge(*edge)

    def __str__(self):
        graph_as_str = ''
        for i in self.graph.nodes:
            graph_as_str += f'Node {i} connections: {",".join([f"{j}" for j in list(self.graph.neighbors(i))])}\n'
        return graph_as_str
    
    def draw(self):
        G = self.graph
        pos = nx.spring_layout(G)  # positions for all nodes
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(G, pos, width=6)
        
        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

        plt.axis("off")
        plt.show()
    
    def has_cycle(self):
        try:
            cycles = nx.find_cycle(self.graph)
            return True
        except:
            return False
    
class MulticastRoute(Graph):
    
    def __init__(self, G, root_node, destination_nodes, build_tree=True):
        assert isinstance(G,Graph), 'Invalid Type'
        if build_tree:
            tree = self.build_multicast_route(G.graph, root_node, destination_nodes)
        else:
            tree = self.prune_multicast_tree(G.graph, root_node, destination_nodes)
        self.root_node = root_node
        self.destination_nodes = destination_nodes
        super().__init__(graph=tree)
    
    def build_multicast_route(self, G, root_node, destination_nodes):

        # Initialize Multicast Tree
        multicast_tree = nx.Graph()
        # Add root node
        multicast_tree.add_node(root_node)
        
        # Initialize Visited Destination Nodes
        visited_destination_nodes = []
    
        while len(destination_nodes) != len(visited_destination_nodes):
            available_edges = []
            for node in multicast_tree.nodes:
                available_edges += list(G.edges(node))
            
            duplicated_edge = True
            while duplicated_edge:
                # Checks for Cycles
                edge_to_add = random.choice(available_edges)
                if edge_to_add[1] in list(multicast_tree.nodes()):
                    duplicated_edge = True
                else:
                    start = edge_to_add[0]
                    end = edge_to_add[1]
                    multicast_tree.add_edge(start, end, **Edge(start=start, end=end, **G.edges[start,end]).as_dict())
                    duplicated_edge = False
                    
                    # Update list of visited destination nodes
                    if end in destination_nodes:
                        visited_destination_nodes.append(end)
        multicast_tree = self.prune_multicast_tree(multicast_tree, root_node, destination_nodes)
        
        return multicast_tree
     
    def prune_multicast_tree(self, multicast_tree, root_node, destination_nodes):
        
        nodes_to_remove = [0] # initialize as not empty, will be overwritten later on
        while len(nodes_to_remove) != 0:
            nodes_to_remove = []
            for node in multicast_tree.nodes:
                if len(list(multicast_tree.neighbors(node))) == 1:
                    if node != root_node and node not in destination_nodes:
                        nodes_to_remove.append(node)
            for node_to_remove in nodes_to_remove:
                multicast_tree.remove_node(node_to_remove)

        return multicast_tree    
    
    def get_max_delay(self, **kwargs):
        delays_to_destination = []
        for destination in self.destination_nodes:
            shortest_path = self.shortest_path(source=self.root_node, target=destination, weight='delay')
            delay = self.path_weight(shortest_path, 'delay')
            delays_to_destination.append(delay)
        return max(delays_to_destination)

    def get_total_cost(self):
        total_cost = 0
        for edge in self.graph.edges():
            total_cost += self.get_edge(edge=edge, attribute='cost')

        return total_cost
    
    def reconnect(self, G):
        aux_tree = self.graph.copy()
        while nx.is_connected(aux_tree) == False: # 4. Repeat process until graph is connected
            available_edges = []
            for node in aux_tree.nodes:
                # 1. Get all neighbor edges not yet in aux_tree
                # 2. Add them to a list
                available_edges += list(G.graph.edges(node))                

            for available_edge in available_edges:
                # remove edges already available in aux_tree
                try:
                    edge = aux_tree.edges[available_edge]
                    available_edges.remove(available_edge)
                except KeyError:
                    pass
            # 3. Randomly pick one edge
            new_edge = random.choice(available_edges)
            try:
                test_cycle = aux_tree.copy()
                test_cycle.add_edge(new_edge[0],new_edge[1])
                cycles = nx.find_cycle(test_cycle)
            except:
                aux_tree.add_edge(new_edge[0],new_edge[1])
            
            # 5. Rebuild aux_tree 
            full_tree = nx.Graph()
            for edge in aux_tree.edges():
                edge_obj = Edge(edge[0],edge[1], **G.graph.edges[(edge[0],edge[1])])
                full_tree.add_edge(edge_obj.start, edge_obj.end, **edge_obj.as_dict())   
            
            self.graph = full_tree

    def draw(self):
        G = self.graph
        pos = nx.spring_layout(G)  # positions for all nodes
        # nodes
        nx.draw_networkx_nodes(G, pos, nodelist= [node for node in G.nodes() if node not in self.destination_nodes and node != self.root_node],node_size=700)
        nx.draw_networkx_nodes(G, pos, nodelist= [node for node in G.nodes() if node in self.destination_nodes and node != self.root_node],node_size=700, node_color='red')
        nx.draw_networkx_nodes(G, pos, nodelist= [self.root_node],node_size=700, node_color='green')
        # edges
        nx.draw_networkx_edges(G, pos, width=6)
        
        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

        plt.axis("off")
        plt.title(f'Max Delay: {self.get_max_delay()} - Cost: {self.get_total_cost()}')
        plt.show()