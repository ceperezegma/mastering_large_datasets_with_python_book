#!/usr/bin/env python

import sys
# from functools import reduce

# def make_counts(acc, nxt):
#     acc[nxt] = acc.get(nxt, 0) + 1
#     return acc


if __name__ == '__main__':
	curkey = None
	total = 0
	for line in sys.stdin:
		key, val = line.split("\t")
		val = int(val)

		if key == curkey:
			total += val
		else:
			if curkey is not None:
				sys.stdout.write("{}\t{}\n".format(curkey, total))

			curkey = key
			total = val

	sys.stdout.write("{}\t{}\n".format(curkey, total))
  
  
  
  
  
  
  
#  for w in reduce(make_counts, sys.stdin, {}):
#      print(w)
         
    