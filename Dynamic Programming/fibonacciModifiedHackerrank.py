#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    if n==1:
        return t1
    if n==2:
        return t2
    '''To Test
    l= fibonacciModified(t1,t2,n-2)
    k=(fibonacciModified(t1,t2,n-1)**2)
    print(n,':',l,'+',k)'''
    return fibonacciModified(t1,t2,n-2)+(fibonacciModified(t1,t2,n-1)**2)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
