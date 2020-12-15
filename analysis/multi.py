import os
import numpy as np
algorithm = 'NSGAII'
pop_size = 30
nbr_generations = 50
network = 2
problem_group = 1
def parse_file_multi(path, problem_group):
    with open(path,'r') as ga_file:
        res = ga_file.readlines()
        return_values = []
        for r in res: 
            str_ = r.split(' ')
            cost = float(str_[0])
            delay = float(str_[1])
            if problem_group > 3:
                delay_2 = float(str_[2])
                return_values.append(
                    (
                        cost,
                        delay,
                        delay_2
                    )
                )
            else:
                return_values.append(
                    (
                        cost,
                        delay
                        
                    )
                )
    return return_values


for algorithm in ['SPEAII', 'NSGAII']:
    for problem_group in range(1,7):
        all_results = []        
        for i in range(20):
            path_template = f'results/multiobjective/{algorithm}/{pop_size}_{nbr_generations}_{network}_{problem_group}_{i}'
            all_results.append(parse_file_multi(path_template,problem_group))

        print(f'Setup: pop_size = {pop_size}, nbr_generations = {nbr_generations}, network={network}, problem = {problem_group}, algorithm = {algorithm}')
        delays = []
        costs = []
        cardinality = []

        for frontier in all_results:
            cardinality_n = 0
            print(set(frontier))
            for val in list(set(frontier)):
                delays.append(val[0])
                costs.append(val[1])
                cardinality_n += 1
            cardinality.append(cardinality_n)
        # print(f'Convergence: {len(list(filter(lambda res: res[-1]["fitness"]==0.010869565217391304, all_results)))/20}')

        # print(f'STD Delay: {np.std(list(map(lambda res: res[-1]["delay"], all_results)))}')
        # print(f'Average Cost: {np.average(costs)}')
        # print(f'Average Delay: {np.average(delays)}')
        print('Algorithm')
        print(f'Average Cardinality: {np.average(cardinality)}')
        # print(f'STD Cost: {np.std(list(map(lambda res: res[-1]["cost"], all_results)))}')
    
