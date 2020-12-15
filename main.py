from components.graph import Graph
from components.population import MonoObjectivePopulation
from utils.utils import build_pre_defined_network
import argparse
default_parameters = {
    'network':0,
    'Tel':0.5,
    'Pmut':0.05,
    'Pnmut':0.2,
    'alpha':0.5,
    'phi':1,
    'nbr_runs':20,
    'nbr_generations':20,
    'pop_size':15,
    'max_delay':25,
    'Cr':0.5
}

experiments = [
    {'pop_size':15, 'nbr_generations':20, 'max_delay':25, 'network':0},
    {'pop_size':15, 'nbr_generations':50, 'max_delay':25, 'network':0},
    {'pop_size':30, 'nbr_generations':20, 'max_delay':25, 'network':0},
    {'pop_size':30, 'nbr_generations':50, 'max_delay':25, 'network':0},
    {'pop_size':15, 'nbr_generations':20, 'max_delay':9, 'network':1},
    {'pop_size':15, 'nbr_generations':50, 'max_delay':9, 'network':1},
    {'pop_size':30, 'nbr_generations':20, 'max_delay':9, 'network':1},
    {'pop_size':30, 'nbr_generations':50, 'max_delay':9, 'network':1}
]

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Mono-objective Experiment.')
    parser.add_argument('--pop_size', type=int, help='Population Size of GA')
    parser.add_argument('--nbr_generations', type=int, help='Number of Generations of GA.')
    parser.add_argument('--max_delay', type=int, help='Max Delay Constraint.')
    parser.add_argument('--network', type=int, help='Network Number')

    args = parser.parse_args()
    params = vars(args)
    print(params)
    G, root_node, destination_nodes = build_pre_defined_network(params['network'])
    gr = Graph(G)
    optimals = 0
    nbr_runs = default_parameters['nbr_runs']
    generations = params['nbr_generations']
    pop_size = params['pop_size']
    for i in range(nbr_runs):
        results=''
        pop = MonoObjectivePopulation(Graph=gr, 
        Tp=pop_size, 
        Cr=default_parameters['Cr'], 
        Pnmut =default_parameters['Pnmut'], 
        Tel =default_parameters['Tel'] , 
        Pmut=default_parameters['Pmut'], 
        root_node=root_node, 
        destination_nodes=destination_nodes,
        max_delay=params['max_delay'])
        gen = 0
        while gen < generations:
            gen += 1
            pop.fitness()
            pop.sort()
            pop.natural_selection()
            results += f'Fitness: {pop.population[0].fitness} - Delay: {pop.population[0].multicast_tree.get_max_delay()} - Cost: {pop.population[0].multicast_tree.get_total_cost()}\n'
        with open(f'results/{params["pop_size"]}_{params["nbr_generations"]}_{params["max_delay"]}_{params["network"]}_{i}.txt','w') as exper_run_file:
            exper_run_file.write(results)
            img_path = f'results/{params["pop_size"]}_{params["nbr_generations"]}_{params["max_delay"]}_{params["network"]}_{i}.png'
            pop.population[0].multicast_tree.draw(path=img_path)
    

    