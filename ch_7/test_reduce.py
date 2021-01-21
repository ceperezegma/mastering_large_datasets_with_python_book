from functools import reduce

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc
    
def my_frequencies(xs):
    return reduce(make_counts, xs, {})
    
if __name__ == "__main__":
    xs = ["A", "B", "C", "A", "A", "C", "A"]
    ys = [1, 3, 6, 1, 2, 9, 3, 12]
    print(my_frequencies(xs))
    print(my_frequencies(ys))
    print(my_frequencies("mississippi"))