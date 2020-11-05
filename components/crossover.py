import numpy as np
from components.graph import Graph, MulticastRoute
from components.edge import Edge
import networkx as nx
import random
from components.solution import Solution
class Crossover:
    def crossover(self, partner1, partner2):
        raise NotImplementedError('CrossoverNotImplemented')

class BuenoOliveiraCrossover(Crossover):
    def crossover(self, partner1, partner2):
        
        # find edges in common
        p1_edges = partner1.multicast_tree.edges()
        edges_in_common = []

        aux_tree = nx.Graph()

        for p1_edge in p1_edges:
            if partner2.multicast_tree.is_connected(p1_edge):
                edges_in_common.append(p1_edge)
        
        aux_tree.add_edges_from(edges_in_common)

        for dest_node in self.destination_nodes:
            if dest_node not in aux_tree.nodes:
                aux_tree.add_node(dest_node)
        
        if self.root_node not in aux_tree.nodes:
            aux_tree.add_node(self.root_node)

        while nx.is_connected(aux_tree) == False: # 0. Repeat process until graph is connected
            available_edges = []
            for node in aux_tree.nodes:
                # 1. Get all neighbor edges not yet in aux_tree
                # 2. Add them to a list
                available_edges += list(self.graph.graph.edges(node))                

            for available_edge in available_edges:
                # remove edges already available in aux_tree
                try:
                    edge = aux_tree.edges[available_edge]
                    available_edges.remove(available_edge)
                except KeyError:
                    pass
            # 3. Randomly pick one edge
            new_edge = random.choice(available_edges)
            # 4. Check if new edge adds a cycle
            try:
                test_cycle = aux_tree.copy()
                test_cycle.add_edge(new_edge[0],new_edge[1])
                cycles = nx.find_cycle(test_cycle)
            except: # will raise if no cycles are found
                aux_tree.add_edge(new_edge[0],new_edge[1])
        # 5. Rebuild aux_tree 
        child = nx.Graph()
        for edge in aux_tree.edges():
            edge_obj = Edge(edge[0],edge[1], **self.graph.graph.edges[(edge[0],edge[1])])
            child.add_edge(edge_obj.start, edge_obj.end, **edge_obj.as_dict())   
        
        # 6. Prune Tree
        child_tree = MulticastRoute(Graph(child), self.root_node, self.destination_nodes, build_tree=False)
        # print(f'Child has Cycle: {child_tree.has_cycle()}')
        return child_tree
        
        








        

