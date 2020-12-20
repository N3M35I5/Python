#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
# to print array
def printarr(a):
    for r in a:
        print(r)


def getWays(n, c):
    #initialize 2D List
    arr = []
    for i in range(len(c)):
        col = []
        for j in range(n + 1):
            col.append(0)
        arr.append(col)
    #Dynamic programing
    for i in range(len(c)):
        arr[i][0] = 1
    for i in range(len(c)):
        for j in range(n + 1):
            if j < c[i]:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - c[i]]
    # printarr(arr)
    return arr[i][j]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(ways)
    # fptr.write(str(ways) + '\n')
    #
    # fptr.close()
