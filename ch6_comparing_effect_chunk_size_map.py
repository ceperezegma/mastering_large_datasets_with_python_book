from time import time
from multiprocessing import Pool


def times_two(x):
    return x * 2 + 7 
    
def parallel_map(xs, chunk=8500):
    """
    parallel map execution 
    """
    with Pool(2) as P:
        x = P.map(times_two, xs, chunk)
    return x

print("""
{:<10} | {}
-------------------------""".format("chunksize","runtime"))


for i in range(0, 9):
    N = 10000000
    chunk_size = 5 * (10**i)
    
    t1 = time()
    parallel_map(range(N), chunk_size)
    par_time = time() - t1
    print("""{:<10} | {:>0.3f}""".format(chunk_size, par_time))
    
    