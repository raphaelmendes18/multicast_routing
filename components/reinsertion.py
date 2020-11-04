from components.selection import OptimizedRoulette, NormalizedRoulette
class Reinsertion:
    def reinsertion(self, **kwargs):
        raise NotImplementedError('Reinsertion not implemented')

class SortedReinsertion(Reinsertion):
    def reinsertion(self, **kwargs):
        self.fitness()
        self.sort()
        self.population = self.population[:self.pop_size]

class ElitismReinsertion(Reinsertion):
    def reinsertion(self, **kwargs):
        self.fitness()
        elit_parents_to_keep = sorted(self.population, key=lambda x: x.fitness, reverse=True)[0:int(self.Tel*self.pop_size)].copy()
        children = self.population[self.pop_size:int(self.pop_size*self.cross_rate)].copy()
        self.population = elit_parents_to_keep + children
        self.sort()

class RouletteElitismReinsertion(Reinsertion, NormalizedRoulette):
    def reinsertion(self, **kwargs):
        elit_parents_to_keep_idx = sorted(range(self.pop_size), key=lambda x: self.population[x].fitness, reverse=True)[0:int(self.Tel*self.pop_size)]
        old_population = self.population.copy()
        new_pop = list(map(lambda i: old_population[i], elit_parents_to_keep_idx))
        for idx in elit_parents_to_keep_idx:
            del self.population[idx]
        self.fitness()
        self.build_roulette()
        # Reinsert using Roulette
        individuals_picked = []
        while len(new_pop) < self.pop_size:
            while(True):
                new_idx = self.turn_roulette()
                if new_idx not in individuals_picked:
                    individuals_picked.append(new_idx)
                    break
            new_pop.append(self.population[new_idx])
        self.population = new_pop
        self.sort()