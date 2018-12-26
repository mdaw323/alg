#!/bin/python3

import sys

def fib(n):
    a,b = 1,1
    sum = 0
    while b <= n:        
        if b % 2 == 0:
            sum+=b
        a,b = b, a+b
    return sum


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (fib(n))
