from jmetal.core.operator import Crossover
from multiobjective.jmetal_solution import MulticastMultiObjectiveSolution
from typing import List
import numpy as np
from components.graph import Graph, MulticastRoute
from components.edge import Edge
from components.crossover import BuenoOliveiraCrossover
import networkx as nx
import random

class MulticastCrossover(BuenoOliveiraCrossover, Crossover[MulticastMultiObjectiveSolution, MulticastMultiObjectiveSolution]):
    
    def __init__(self, probability: float, root_node: int, destination_nodes: List[int], graph: Graph):
        super(MulticastCrossover, self).__init__(probability=probability)

        self.root_node = root_node
        self.destination_nodes = destination_nodes
        self.graph = graph

    def get_number_of_parents(self) -> int:
        return 2
    
    def get_number_of_children(self) -> int:
        return 1

    def execute(self, parents: List[MulticastMultiObjectiveSolution]) -> List[MulticastMultiObjectiveSolution]:
        child_tree = self.crossover(parents[0], parents[1])
    
        child = MulticastMultiObjectiveSolution(graph = child_tree, 
                                                number_of_variables = parents[0].number_of_variables, 
                                                number_of_objectives = parents[0].number_of_objectives,
                                                root_node = parents[0].root_node,
                                                destination_nodes = parents[0].destination_nodes,
                                                number_of_constraints = parents[0].number_of_constraints,
                                                max_delay = parents[0].max_delay,
                                                alpha = parents[0].alpha,
                                                phi = parents[0].phi,
                                                build_tree=False
                                                )
        return [child]
    def get_name(self) -> str:
        return 'Crossover by Similarity'