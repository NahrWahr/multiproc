import multiprocessing as mp
from joblib import Parallel, delayed
import numpy as np
import time
import matplotlib.pyplot as plt

def random_square(seed):
    np.random.seed(seed)
    random_num = np.random.randint(1, 10)
    return random_num**2

def plot(result):
    fig = plt.figure()
    ax = plt.axes()
    plt.hist(result)
    plt.show()


def serial(n):
    t0 = time.time()
    results = []
    for i in range(n): 
        results.append(random_square(i))
    t1 = time.time()
    exec_time = t1 - t0
    return exec_time

def parallel(n):
    t0 = time.time()
    n_cpu = mp.cpu_count()

    pool = mp.Pool(processes=12)
    results = [pool.map(random_square, range(n))]
    t1 = time.time()
    exec_time = t1 - t0
    return exec_time





