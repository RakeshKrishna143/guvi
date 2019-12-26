#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxShared' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH friends as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
from itertools import combinations

def maxShared( n,x, y,w):
    print(n,x,y,w)
    d={}
    j=0
    for i in w:
        if i not in d:
            d[i]=set()
        d[i].add(x[j])
        d[i].add(y[j])
        j+=1
    a=[i for i in range(1,n+1)]
    d1={}
    for i,j in list(combinations(a,2)):
        count=0
        for k in d:
            if i in d[k] and j in d[k]:
                count+=1
        d1[(i*j)]=count
    Keymax = max(d1, key=d1.get)
    val=d1[Keymax]
    print(d1)
    print(Keymax)
    print(val)
    res=0
    for i in d1:
        if d1[i]==val:
            res=max(res,i)
    return(res)


if __name__ == '__main__':
