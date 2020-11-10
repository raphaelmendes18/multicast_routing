import numpy as np
import math
import random 
import concurrent.futures
from components.solution import MonoObjectiveSolution
from components.selection import Roulette
from components.reinsertion import SortedReinsertion, ElitismReinsertion
from components.crossover import BuenoOliveiraCrossover

class Population(object):

    def __init__(self, Graph, Tp, Cr, Pnmut, Pmut, Tel, root_node, destination_nodes):
               
        self.graph = Graph
        self.pop_size = Tp 
        self.number_of_disconnections = Pnmut
        self.mutation_rate = Pmut
        self.cross_rate = Cr
        self.Tel = Tel
        self.root_node = root_node
        self.destination_nodes = destination_nodes
        self.population = self.create_population()

    def create_population(self):
        population = []
        pop_count = 0
        while pop_count < self.pop_size:  
            population.append(MonoObjectiveSolution(graph=self.graph, root_node=self.root_node, destination_nodes=self.destination_nodes))
            pop_count += 1
        return population

    def fitness(self):
        for p in self.population:
            p.calculate_fitness(self.root_node, self.destination_nodes)
    
    def natural_selection(self):
        
        offspring = []
        try:
            self.build_roulette()
        except AttributeError:
           pass
        while len(offspring) < int(self.cross_rate*self.pop_size):
            partner1, partner2 = self.selection()
            child = self.crossover(partner1, partner2)
            child = MulticastSolution(child, self.root_node, self.destination_nodes, build_tree=False)
            if np.random.uniform(0,1) <= self.mutation_rate:
                child.mutation()
            offspring.append(child)

        self.population = self.population + offspring
        self.reinsertion()

    def sort(self):
        self.population = sorted(self.population, key=lambda x: x.fitness, reverse=True)

class MonoObjectivePopulation(Population, Roulette, ElitismReinsertion, BuenoOliveiraCrossover):
    def natural_selection(self):
        
        offspring = []
        try:
            self.build_roulette()
        except AttributeError:
           pass
        while len(offspring) < int(self.cross_rate*self.pop_size):
            partner1, partner2 = self.selection()
            child = self.crossover(partner1, partner2)
            child = MonoObjectiveSolution(child, self.root_node, self.destination_nodes, build_tree=False)
            if np.random.uniform(0,1) <= self.mutation_rate:
                child.mutation(self.number_of_disconnections, self.graph)
            offspring.append(child)

        self.population = self.population + offspring
        self.reinsertion()