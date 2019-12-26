#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'chooseFlask' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY requirements
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY markings
#
def close(lst,K):
    return lst[min(range(len(lst)), key = lambda i: (K-lst[i])>0)] 
def chooseFlask(req, m, markings):
    d={}
    d1={}

    for i in range(m):
        d[i]=[]
        d1[i]=0
    for i,j in markings:
        d[i].append(j)
    req=list(set(req))
    for k in req:
        for i in d:
            if k>max(d[i]):
                d1[i]=10000000
            else:
                d1[i]+=close(d[i],k)-k
    Keymax = min(d1, key=d1.get) 
    return(Keymax)


    

if __name__ == '__main__':
