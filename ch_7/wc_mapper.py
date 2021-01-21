#! /usr/bin python3

import sys

if __name__ == "__main__":
    for line in sys.stdin:
        for word in line.split():
            if len(word) > 6:
                print(word)
