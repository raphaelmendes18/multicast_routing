from jmetal.core.operator import Mutation
from multiobjective.jmetal_solution import MulticastMultiObjectiveSolution
from components.graph import MulticastRoute, Graph
import random

class MulticastMutation(Mutation[MulticastMultiObjectiveSolution]):

    def __init__(self, probability: float, Pnmut: int, G: Graph):
        super(MulticastMutation, self).__init__(probability=probability)
        self.number_of_disconnections = Pnmut
        self.G = G
    
    def execute(self, solution: MulticastMultiObjectiveSolution) -> MulticastMultiObjectiveSolution:
        
        edges_to_remove = int(len(list(solution.multicast_tree.edges()))*self.number_of_disconnections)
        edges_removed = 0
        while edges_removed < edges_to_remove:
            edges = list(solution.multicast_tree.edges())
            random_edge_to_remove = random.choice(edges)
            solution.multicast_tree.remove_edge(random_edge_to_remove)
            edges_removed += 1
        solution.multicast_tree.reconnect(self.G)
        solution.multicast_tree.prune()
        return solution

    def get_name(self):
        return 'Multicast Mutation'