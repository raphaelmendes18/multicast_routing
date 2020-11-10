from jmetal.core.solution import Solution
from typing import List
from components.graph import Graph, MulticastRoute
from components.solution import MulticastSolution

class MulticastMultiObjectiveSolution(Solution, MulticastSolution):
    
    def __init__(self, 
                number_of_variables: int, 
                number_of_objectives: int, 
                graph: Graph, 
                root_node: int, 
                destination_nodes: List[int], 
                number_of_constraints: int = 0,
                max_delay: int = 25, 
                alpha:float = 0.5, 
                omega:int = 1,
                build_tree:bool = True
                ):
        self.number_of_variables = number_of_variables
        self.number_of_objectives = number_of_objectives
        self.number_of_constraints = number_of_constraints
        self.variables = [[] for _ in range(self.number_of_variables)]
        self.objectives = [0.0 for _ in range(self.number_of_objectives)]
        self.constraints = [0.0 for _ in range(self.number_of_constraints)]
        self.attributes = {}

        assert isinstance(graph, Graph), 'Invalid Type for graph'
        
        if build_tree:
            self.multicast_tree = MulticastRoute(graph, root_node, destination_nodes)
        else:
            self.multicast_tree = MulticastRoute(graph, root_node, destination_nodes, build_tree=False)
        self.max_delay = max_delay
        self.alpha = alpha
        self.omega = omega
        self.root_node = root_node
        self.destination_nodes = destination_nodes

    def __eq__(self, solution) -> bool:
        if isinstance(solution, self.__class__):
            return self.variables == solution.variables
        return False

    def __str__(self) -> str:
        return 'Solution(variables={},objectives={},constraints={})'.format(self.variables, self.objectives,
                                                                            self.constraints)