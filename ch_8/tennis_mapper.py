#!/usr/bin/env python

import json
from sys import stdin

def clean_match(match):
    """
    extracts the winner, loser and the field surface from the tennis data source files
    """
    
    ms = match.split(",")
    match_data = {"winner": ms[10], "loser": ms[20], "surface": ms[2]}
    
    return match_data

if __name__ == "__main__":
    for line in stdin:
        print(json.dumps(clean_match(line)))