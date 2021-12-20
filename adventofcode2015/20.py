#!/usr/bin/python3

import sys
import math
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
import functools
sys.setrecursionlimit(10000)

dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE
p1 = p2 = 0



n = 34000000


# for j in range (n - 10, n+11):
#     k = j
#     for i in range(1,j//2+1):
#         if j % i == 0:
#             k += i
#     print(j, k)

print()

numbers = []

# prime = [True] * (n//10+1)

# primes = []
# for i in range(2,len(prime)):
#     if prime[i]:
#         for j in range(i+i,len(prime), i):
#             prime[j] = False
#         primes.append(i)


# print(primes[0:5])
def presents(j):
    k = 0
    i = 1

    while i*i <= j:
        if j % i == 0:
            # print(j,d,k)
            k += i
            if (i*i != j):
                k+= j//i
        i+=1
    return k * 10


pr = [0] * 350_000_000

for i in range(5_000_001):
    for j in range(50):
        pr[i + i*j] += 11 * i

print(pr[5_000_000])


def presents2(j):
    k = 0
    i = 1

    while i*i <= j:
        if j % i == 0:
            # print(j,d,k)
            if 50 * i <= j:
                k += i
            if (i*i != j) and (j//i * 50 <=j) :
                k+= j//i
        i+=1
    return k * 11

# for j in range (n - 100000, n+1):
#     k = 0
#     for i in range(1,int(math.sqrt(j))+1):
#         if j % i == 0:
#             k += i
#             if (i*i != j):
#                 k+= j//i
#     numbers.append((k,j))

# m = presents(n)
# n = 120
# minm = n
# for i in range(n//10, n, 2):
#    k = presents2(i)
#    if k >= n:
#        print (minm)
#        minm = min(minm, i)

# print(minm)
for i in range(5_000_000):
    if pr[i] >=n:
        print(i,pr[i])
        break
