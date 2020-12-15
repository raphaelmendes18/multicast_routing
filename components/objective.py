import numpy as np
class Objective:

    def __init__(self, num_objectives=1):
        self.fitness = -np.inf

    def calculate_fitness(self, root_node, destination_nodes):
        
        delays_to_destination = []
        for destination in destination_nodes:
            shortest_path = self.multicast_tree.shortest_path(source=root_node, target=destination, weight='delay')
            delay = self.multicast_tree.path_weight(shortest_path, 'delay')
            delays_to_destination.append(self.w(delay))
        
        total_cost = 0
        for edge in self.multicast_tree.edges():
            total_cost += self.multicast_tree.get_edge(edge=edge, attribute='cost')

        delay_penalty = np.prod(delays_to_destination)

        self.fitness = self.phi*(delay_penalty/total_cost)