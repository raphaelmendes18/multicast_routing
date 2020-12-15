import os
import numpy as np
pop_size = 15
nbr_generations = 50
max_delay = 9
network = 1

def parse_file(path):
    with open(path,'r') as ga_file:
        res = ga_file.readlines()
        return_values = []
        for r in res: 
            str_ = r.split(' ')
            fitness = float(str_[1])
            delay = int(str_[4])
            cost = int(str_[7].replace('\n',''))
            
            return_values.append(
                {
                    'fitness':fitness,
                    'delay':delay,
                    'cost':cost
                }
            )
        
    return return_values
        
def parse_file_multi(path):
    with open(path,'r') as ga_file:
        res = ga_file.readlines()
        return_values = []
        for r in res: 
            str_ = r.split('\t')
            cost = float(str_[0])
            delay = int(str_[1])
            
            return_values.append(
                {
                    'delay':delay,
                    'cost':cost
                }
            )
        
    return return_values

all_results = []
for i in range(20):
    path_template = f'results/{pop_size}_{nbr_generations}_{max_delay}_{network}_{i}.txt'
    all_results.append(parse_file(path_template))

print(f'Setup: pop_size = {pop_size}, nbr_generations = {nbr_generations}, network={network}')
print(f'Convergence: {len(list(filter(lambda res: res[-1]["fitness"]==0.010869565217391304, all_results)))/20}')
print(f'Average Delay: {sum(map(lambda res: res[-1]["delay"], all_results))/20}')
print(f'STD Delay: {np.std(list(map(lambda res: res[-1]["delay"], all_results)))}')
print(f'Average Cost: {sum(map(lambda res: res[-1]["cost"], all_results))/20}')
print(f'STD Cost: {np.std(list(map(lambda res: res[-1]["cost"], all_results)))}')
    
