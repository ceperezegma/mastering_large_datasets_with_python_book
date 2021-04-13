#!/usr/bin/env python

import re
from pyspark import SparkContext


def round5 (x):
    return 5 * int(x / 5)

    
def clean_match (match):
    ms = match.split(',')
    match_data = {'winner': ms[10],
                  'loser': ms[20],
                  'surface': ms[2]}
    return match_data
    

def elo_acc (acc, nxt):
    w_elo = acc.get(nxt['winner'], 1600)
    l_elo = acc.get(nxt['loser'], 1600)
    Qw = 10 ** (w_elo/400)
    Ql = 10 ** (l_elo/400)
    Qt = Qw + Ql
    acc[nxt['winner']] = round5 (w_elo + 25 * (1 - (Qw / Qt)))
    acc[nxt['loser']] = round5 (l_elo - 25 * (1 - (Ql / Qt)))
    return acc


def elo_comb(a, b):
    a.update(b)
    return a 


if __name__ == '__main__':
    sc = SparkContext(appName='TennisElos')
    text_files = sc.textFile('/tennis_data/wta_matches_200*.csv')  # reads the files from HDFS
    xs = text_files.map(clean_match) \
            .aggregate({}, elo_acc, elo_comb)
    
    print('--> RESULT')
    for x in sorted(xs.items(), key=lambda x: x[1], reverse=True) [:10]:
        print('{:<30}{}'.format(*x))
    
    print('--> END')