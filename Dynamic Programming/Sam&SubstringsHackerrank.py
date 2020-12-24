#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def mod7(n):
    return n%1000000007

#Time complexity is O(n)
def substrings(n):
    sum = 0  # Initialize result
    # mf is multiplying factor.
    mf = 1
    for i in range(len(n) - 1, -1, -1):
        #print(sum ,'+', (int(n[i])) ,'*', (i + 1) ,'*', mf)
        sum = sum + (int(n[i])) * (i + 1) * mf
        # Making new multiplying factor as
        mf = mf * 10 + 1
    return mod7(sum)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
