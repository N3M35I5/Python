#!/bin/python3

import math
import os
import random
import re
import sys
#source for memoization with recursion : https://medium.com/@anishaj037/the-coin-change-problem-memoization-and-recursion-d6ea2786c3f3
#source for problem solving reference : https://www.geeksforgeeks.org/tiling-problem/
def position(n,memo={}):#function to find different positions with memoization
    if n in memo.keys():
        return memo[n]
    else:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return 1
        memo[n]=position(n - 1) + position(n - 4)
        return memo[n]

#The function which i wrote which was not fast enough so i used Sieve Method
'''
def lessPrime(n):#function to find count of prime less than or equal to n
    global prime
    primeCount = 0
    for i in range(2, n + 1):
        count = 0
        if i in prime:
            primeCount += 1
        else:
            for j in range(2, i + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                prime.append(i)
                primeCount += 1
    return primeCount
'''
# source for Sieve method : https://www.geeksforgeeks.org/analysis-different-methods-find-prime-number-python/#:~:text=Sieve%20Method&text=If%20n%20is%2020%2C%20the,a%20list%20of%20prime%20numbers.
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for p in range(2, n+1):
        if prime[p]:
            c += 1
    return c

# Complete the redJohn function below.
def redJohn(n):
    pos=position(n)
    #return lessPrime(pos)
    return SieveOfEratosthenes(pos)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = redJohn(n)

        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
