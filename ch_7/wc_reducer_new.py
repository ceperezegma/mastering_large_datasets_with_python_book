#!/usr/bin/env python

import sys
from functools import reduce

def make_counts(acc, nxt):
	nxt = nxt.strip("\n") # removes de the taining LF from the stdin for each word
	nxt = nxt.strip("\t") # removes de the taining CR from the stdin for each word
	acc[nxt] = acc.get(nxt, 0) + 1
	return acc

if __name__ == '__main__':
	word_count = reduce(make_counts ,sys.stdin, {})
	sys.stdout.write("{}".format(word_count))
