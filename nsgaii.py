from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from multiobjective.jmetal_problem import MulticastProblem
from multiobjective.jmetal_solution import MulticastMultiObjectiveSolution
from multiobjective.jmetal_mutation import MulticastMutation
from multiobjective.jmetal_crossover import MulticastCrossover
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from components.graph import Graph
from utils.utils import build_pre_defined_network

if __name__ == '__main__':
    G = build_pre_defined_network(network=0)
    gr = Graph(G)
    root_node = 1
    destination_nodes = [2,9,10,13,14]
    Pnmut: float = 0.2
    Tel: float = 0.5 
    Pmut: float = 0.05 
    generations: int = 50
    pop_size: int = 30
    Cr: float = 0.5
    max_evaluations: float = generations*pop_size
    problem: MulticastProblem = MulticastProblem(Graph = gr, root_node = root_node, destination_nodes = destination_nodes)
    algorithm = NSGAII(
        problem=problem,
        population_size=pop_size,
        offspring_population_size=int(pop_size*Cr),
        mutation=MulticastMutation(probability=Pmut, Pnmut=Pnmut, G=gr),
        crossover=MulticastCrossover(probability=1.0, root_node = root_node, destination_nodes = destination_nodes, graph=gr),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
    )

    algorithm.run()
    front = algorithm.get_result()

    # Save results to file
    print_function_values_to_file(front, 'FUN.' + algorithm.label)
    print_variables_to_file(front, 'VAR.'+ algorithm.label)

    print(f'Algorithm: ${algorithm.get_name()}')
    print(f'Problem: ${problem.get_name()}')
    print(f'Computing time: ${algorithm.total_computing_time}')
