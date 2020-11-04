import random
import math
import numpy as np
class Selection:
    def selection(self, **kwargs):
        raise NotImplementedError('need to implement crossover')

class TournamentSelection(Selection):

    def selection(self, **kwargs):
        mating_pool = self.population.copy()
        partner1 = sorted(random.sample(mating_pool, self.Tour), key=lambda x: x.fitness, reverse=True)[0]
        partner2 = sorted(random.sample(mating_pool, self.Tour), key=lambda x: x.fitness, reverse=True)[0]
        return (partner1, partner2)

class Roulette(Selection):

    def selection(self, **kwargs):
        
        idx1 = self.turn_roulette()
        idx2 = self.turn_roulette()
        while (idx1 == idx2):
            idx2 = self.turn_roulette()
        partner1 = self.population[idx1]
        partner2 = self.population[idx2]
        return (partner1, partner2)
            
    def build_roulette(self):
        roulette = []
        for idx, sol in enumerate(self.population):
            roulette += ([idx] * int(sol.fitness*1000))
        self.roulette = roulette

    def turn_roulette(self):
        idx = np.random.randint(0,len(self.roulette))
        return self.roulette[idx]
    
    def turn_and_remove_roulette(self):
        idx = self.roulette[np.random.randint(0,len(self.roulette))]
        self.roulette = [value for value in self.roulette if value != idx]
        return idx

class OptimizedRoulette(Roulette):
    def build_roulette(self):
        '''
        Creates the roulette representation based on the individuals fitness, instead of using the raw value we use the probability which would give same results
        but saves memory, hence speeding up the algorithm
        '''
        sum_fitness = sum(map(lambda c: c.fitness, self.population))
        roulette = []
        for idx, sol in enumerate(self.population):
            prob = int((sol.fitness/sum_fitness)*MAX_FITNESS)
            roulette += ([idx] * prob)
        self.roulette = roulette

class NormalizedRoulette(Roulette):
    '''
    Creates the Roulette based on the minimum fitness across individuals, considering the difference + 1 as the number of spaces in the roulette
    '''
    def build_roulette(self):
        min_fitness = min(map(lambda c: c.fitness, self.population))
        roulette = []
        for idx, sol in enumerate(self.population):
            roulette += ([idx] * int((sol.fitness + 1) - min_fitness))
        self.roulette = roulette

class RankedRoulette(Roulette):
    '''
    Make sure it's sorted before running this
    '''
    def build_roulette(self):
        spaces = []
        for idx, _ in enumerate(self.population):
            spaces += ([idx] * (len(self.population)-idx))
        self.roulette = spaces

class StochasticTournamentSelection(Roulette):
    
    def selection(self, **kwargs):
        partners = []
        nbr_parents = 2
        for _ in range(nbr_parents):
            mating_pool = []
            for _ in range(self.Tour):
                mating_pool.append(self.population[self.turn_roulette()].copy())
            partners.append(sorted(mating_pool, key=lambda x: x.fitness, reverse=True)[0])
        
        return tuple(partners)
class OptimizedStochasticTournamentSelection(StochasticTournamentSelection, OptimizedRoulette):
    def selection(self, **kwargs):
         return super(StochasticTournamentSelection, self).selection(**kwargs)
class RankedStochasticTournamentSelection(StochasticTournamentSelection, RankedRoulette):
    def selection(self, **kwargs):
         return super(StochasticTournamentSelection, self).selection(**kwargs)
class NormalizedStochasticTournamentSelection(StochasticTournamentSelection, NormalizedRoulette):
    def selection(self, **kwargs):
        return super(StochasticTournamentSelection, self).selection(**kwargs)