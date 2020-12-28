from time import time
from multiprocessing import Pool


def times_two(x):
    return x * 2
    

def lazy_map(xs):
    """
    lazy map execution
    """
    return list(map(times_two, xs))
    

def parallel_map(xs, chunk=8500):
    """
    parallel map execution 
    """
    with Pool(2) as P:
        x = P.map(times_two, xs, chunk)
    return x


for i in range(0, 7):
    N = 10 ** i
    t1 = time()
    lazy_map(range(N))
    lm_time = time() - t1
    
    t1 = time()
    parallel_map(range(N))
    par_time = time() - t1
    print("""
    -- N = {} -- 
    Lazy map time: {} 
    Parallel map time: {}
    """.format(N,lm_time, par_time))
    
    