import multiprocessing
import numpy as np 
import parmap

num_cores = multiprocessing.cpu_count()


def square(input_list):
    return [x*x for x in input_list]

data = list(range(1,25))


splited_data = np.array_split(data, num_cores)

splited_data = [x.tolist() for x in splited_data]

result = parmap.map(square, splited_data, pm_pbar=False, pm_processes=num_cores)

