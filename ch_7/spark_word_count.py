#!/usr/bin/env python

import re
from pyspark import SparkContext


if __name__ == "__main__":
    sc = SparkContext(appName="WordScores")
    PAT = re.compile(r'[-./:\s\xa0]+')
    text_files = sc.textFile("/home/ec2-user/environment/mastering_large_datasets_with_python_book/ch_7/*").collect()
    
    print("test_file = {}".format(text_files))
    
    xs = text_files.flatMap(lambda x: PAT.split(x)).items() #filter(lambda x: len(x) > 6)#.countByValue()
    
    print("xs = {}".format(xs))
    
    # for k, v in xs:
    #     print("{:<30}{}".format(k.encode("ascii","ignore"),v))
    
