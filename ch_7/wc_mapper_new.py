#!/usr/bin/env python

import sys

if __name__ == "__main__":
	for line in sys.stdin:
		for word in line.rstrip("\r\n").split(): # removes the CR LF and the end of each line in the text 
			if len(word) > 10:
				sys.stdout.write("{}\n".format(word))