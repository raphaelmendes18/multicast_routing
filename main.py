from components.graph import Graph
from components.population import MonoObjectivePopulation
from utils.utils import build_pre_defined_network

G = build_pre_defined_network(network=0)
gr = Graph(G)
optimal = 0.014492753623188406
optimals = 0
nbr_runs = 1
generations = 50
pop_size = 30
for i in range(nbr_runs):
    pop = MonoObjectivePopulation(Graph=gr, Tp=pop_size, Cr=0.5, Pnmut=0.2, Tel = 0.5, Pmut=0.05, root_node=1, destination_nodes=[2,9,10,13,14])
    gen = 0
    while gen < generations:
        gen += 1
        pop.fitness()
        # print(f"G:{gen} - Best Fitness: {pop.population[0].fitness} - Max Delay: {pop.population[0].multicast_tree.get_max_delay(root_node=1, destination_nodes=[2,9,10,13,14])} - Total Cost: {pop.population[0].multicast_tree.get_total_cost()}")
        pop.sort()
        pop.natural_selection()
        
    if(pop.population[0].fitness == optimal):
        optimals += 1
        pop.population[0].multicast_tree.draw()
print(f'Convergence: {(optimals*100)/nbr_runs}%')
    

    