#!/bin/python3

import sys
import math

def prime(n):
    p = n
    
    for i in range (2, int(math.sqrt(n)) +1):
        while p % i == 0 and p > i:
            p //= i
    return p                


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (prime(n))
