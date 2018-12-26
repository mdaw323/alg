#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    d3 = n // 3
    d5 = n // 5
    d15 = n // 15
    d3 = (d3 * (d3+1)) * 3 // 2
    d5 = (d5 * (d5+1)) * 5 // 2
    d15 = (d15 * (d15+1)) * 15 // 2    
    print(d3+d5 - d15)
