from components.graph import Graph
from components.population import MonoObjectivePopulation
from utils.utils import build_pre_defined_network

G = build_pre_defined_network(network=0)
gr = Graph(G)
generations = 20
optimal = 0.012658227848101266
optimals = 0
for i in range(20):
    pop = MonoObjectivePopulation(Graph=gr, Tp=15, Cr=0.8, Pnmut=0.2, Tel = 0.5, Pmut=0.05, root_node=1, destination_nodes=[2,9,10,13,14])
    gen = 0
    while gen < generations:
        gen += 1
        pop.fitness()
        # print(f"G:{gen} - Best Fitness: {pop.population[0].fitness} - Max Delay: {pop.population[0].multicast_tree.get_max_delay(root_node=1, destination_nodes=[2,9,10,13,14])} - Total Cost: {pop.population[0].multicast_tree.get_total_cost()}")
        pop.sort()
        pop.natural_selection()
    if(pop.population[0].fitness == 0.012658227848101266):
        optimals += 1
print(f'Convergence: {(optimals*100)/20}%')
    

    