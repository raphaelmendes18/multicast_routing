from multiobjective.jmetal_solution import MulticastMultiObjectiveSolution
from jmetal.core.problem import Problem
from components.graph import Graph
from typing import Generic, TypeVar, List

S = TypeVar('S')

class MulticastProblem(Problem[MulticastMultiObjectiveSolution]):

    MINIMIZE = -1
    MAXIMIZE = 1

    def __init__(self, Graph: Graph, root_node: int, destination_nodes: List[int]):
        self.number_of_variables: int = 2
        self.number_of_objectives: int = 2
        self.number_of_constraints: int = 0

        self.reference_front: List[S] = []

        self.directions: List[int] = []
        self.labels: List[str] = []

        self.G = Graph
        self.root_node = root_node
        self.destination_nodes = destination_nodes

    def create_solution(self) -> MulticastMultiObjectiveSolution:
        """ Creates a valid solution to the problem.
        :return: MulticastMultiObjectiveSolution. """

        return MulticastMultiObjectiveSolution(number_of_variables=self.number_of_variables, 
                                                number_of_objectives=self.number_of_objectives, 
                                                graph=self.G, 
                                                root_node=self.root_node, 
                                                destination_nodes=self.destination_nodes, 
                                                number_of_constraints=self.number_of_constraints
                                                )

    def evaluate(self, solution: MulticastMultiObjectiveSolution) -> MulticastMultiObjectiveSolution:
        
        solution.objectives[0] = self._f_cost(solution)
        solution.objectives[1] = self._f_delay_1(solution)

        return solution

    def _f_cost(self, solution):
        return solution.multicast_tree.get_total_cost()

    def _f_delay_1(self, solution):
        return solution.multicast_tree.get_total_delay()

    def _f_delay_2(self, solution):
        return solution.multicast_tree.get_average_delay()

    def _f_delay_3(self, solution):
        return solution.multicast_tree.get_max_delay()

    def get_name(self) -> str:
        return 'Multicast Problem'

class MulticastProblemExp1(MulticastProblem):
    pass

class MulticastProblemExp2(MulticastProblem):
    def evaluate(self, solution: MulticastMultiObjectiveSolution) -> MulticastMultiObjectiveSolution:
        
        solution.objectives[0] = self._f_cost(solution)
        solution.objectives[1] = self._f_delay_2(solution)
        return solution

class MulticastProblemExp3(MulticastProblem):
    def evaluate(self, solution: MulticastMultiObjectiveSolution) -> MulticastMultiObjectiveSolution:
        
        solution.objectives[0] = self._f_cost(solution)
        solution.objectives[1] = self._f_delay_3(solution)
        return solution

class MulticastProblemExp4(MulticastProblem):

    MINIMIZE = -1
    MAXIMIZE = 1

    def __init__(self, Graph: Graph, root_node: int, destination_nodes: List[int]):
        
        super().__init__(Graph, root_node, destination_nodes)
        self.number_of_variables: int = 3
        self.number_of_objectives: int = 3

    def evaluate(self, solution: MulticastMultiObjectiveSolution) -> MulticastMultiObjectiveSolution:
        
        solution.objectives[0] = self._f_cost(solution)
        solution.objectives[1] = self._f_delay_1(solution)
        solution.objectives[2] = self._f_delay_2(solution)
        return solution

class MulticastProblemExp5(MulticastProblemExp4):
    def evaluate(self, solution: MulticastMultiObjectiveSolution) -> MulticastMultiObjectiveSolution:
        
        solution.objectives[0] = self._f_cost(solution)
        solution.objectives[1] = self._f_delay_1(solution)
        solution.objectives[2] = self._f_delay_3(solution)
        return solution

class MulticastProblemExp6(MulticastProblemExp4):
    def evaluate(self, solution: MulticastMultiObjectiveSolution) -> MulticastMultiObjectiveSolution:
        
        solution.objectives[0] = self._f_cost(solution)
        solution.objectives[1] = self._f_delay_2(solution)
        solution.objectives[2] = self._f_delay_3(solution)
        return solution

