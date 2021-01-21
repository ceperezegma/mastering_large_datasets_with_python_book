#!/usr/bin python3
#/home/ec2-user/anaconda3/bin python3

import sys
from functools import reduce

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc

if __name__ == "__main__":
    for w in reduce(make_counts, sys.stdin, {}):
        print(w)
    