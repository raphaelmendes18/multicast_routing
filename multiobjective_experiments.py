from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.algorithm.multiobjective.spea2 import SPEA2
from jmetal.algorithm.multiobjective.moead import MOEAD
from multiobjective.jmetal_problem import MulticastProblem, MulticastProblemExp1, MulticastProblemExp2, MulticastProblemExp3, MulticastProblemExp4, MulticastProblemExp5, MulticastProblemExp6
from multiobjective.jmetal_mutation import MulticastMutation
from multiobjective.jmetal_crossover import MulticastCrossover
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from components.graph import Graph
from utils.utils import build_pre_defined_network
from jmetal.lab.visualization import Plot
import argparse
from jmetal.util.aggregative_function import Tschebycheff
default_parameters = {
    'network':0,
    'Tel':0.5,
    'Pmut':0.5,
    'Pnmut':0.2,
    'alpha':0.5,
    'phi':1,
    'nbr_runs':20,
    'nbr_generations':20,
    'pop_size':15,
    'max_delay':25,
    'Cr':0.5
}

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Mono-objective Experiment.')
    parser.add_argument('--pop_size', type=int, help='Population Size of GA')
    parser.add_argument('--nbr_generations', type=int, help='Number of Generations of GA.')
    parser.add_argument('--network', type=int, help='Network Number')
    parser.add_argument('--algorithm', type=str, help='Algorithm')
    parser.add_argument('--experiment', type=int, help='Number of Experiment')
    args = parser.parse_args()
    params = vars(args)
    print(params)
    G, root_node, destination_nodes = build_pre_defined_network(network=params['network'])
    gr = Graph(G)
    
    Pnmut: float = params
    Tel: float = default_parameters['Tel']
    Pmut: float = default_parameters['Pmut']
    Pnmut: float = default_parameters['Pnmut']
    generations: int = params['nbr_generations']
    pop_size: int = params['pop_size']
    Cr: float = default_parameters['Cr']
    max_evaluations: float = generations*pop_size
    problem: MulticastProblem = globals()[f'MulticastProblemExp{params["experiment"]}'](Graph = gr, root_node = root_node, destination_nodes = destination_nodes)
    
    for i in range(default_parameters['nbr_runs']):
        if params['algorithm'] == 'MOEAD':
            algorithm = MOEAD(
                problem=problem,
                population_size=pop_size,
                mutation=MulticastMutation(probability=Pmut, Pnmut=Pnmut, G=gr),
                crossover=MulticastCrossover(probability=0.5, root_node = root_node, destination_nodes = destination_nodes, graph=gr),
                aggregative_function=Tschebycheff(dimension=problem.number_of_objectives),
                neighbor_size=20,
                neighbourhood_selection_probability=0.9,
                max_number_of_replaced_solutions=1,
                weight_files_path='resources/MOEAD_weights',
                termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
            )
        elif params['algorithm'] == 'SPEAII':
            algorithm = SPEA2(
            problem=problem,
            population_size=pop_size,
            offspring_population_size=int(pop_size*Cr),
            mutation=MulticastMutation(probability=Pmut, Pnmut=Pnmut, G=gr),
            crossover=MulticastCrossover(probability=1.0, root_node = root_node, destination_nodes = destination_nodes, graph=gr),
            termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
            )
        elif params['algorithm'] == 'NSGAII':
            algorithm = NSGAII(
                problem=problem,
                population_size=pop_size,
                offspring_population_size=int(pop_size*Cr),
                mutation=MulticastMutation(probability=Pmut, Pnmut=Pnmut, G=gr),
                crossover=MulticastCrossover(probability=Cr, root_node = root_node, destination_nodes = destination_nodes, graph=gr),
                termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
            )

        algorithm.run()
        front = algorithm.get_result()
    
        # Save results to file
        print_function_values_to_file(front, f"results/multiobjective/{params['algorithm']}/{params['pop_size']}_{params['nbr_generations']}_{params['network']}_{params['experiment']}_{i}")
        plot_front = Plot(title='Pareto front approximation', axis_labels=['cost', 'delay'])
        plot_front.plot(front, label=f'{params["algorithm"]}', filename=f'{params["algorithm"]}', format='png')
        print(f'Algorithm: ${algorithm.get_name()}')
        print(f'Problem: ${problem.get_name()}')
        print(f'Computing time: ${algorithm.total_computing_time}')
