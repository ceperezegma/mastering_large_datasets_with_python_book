#!/usr/bin/env python

import sys

if __name__ == "__main__":
	for line in sys.stdin:
		for word in line.split():
			sys.stdout.write("{}\t1\n".format(word))


# if __name__ == "__main__":
#     for line in sys.stdin:
#         for word in line.split():
#             if len(word) > 10:
#                 print(word)
