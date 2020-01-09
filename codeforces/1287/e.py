import sys
from itertools import combinations
import random

def print_query(a,b):
    print("?", a, b)
    sys.stdout.flush()

def print_result(s):
    print("!", s)
    sys.stdout.flush()


def readall(a,b):
    res = []
    if mock:
        return list_string(mock_string[a-1:b])
    else:
        l = sys.stdin.readline().strip()    
        while(len(l) > 0):        
            res.append(l)
            l = sys.stdin.readline().strip()

def list_string(strn):
  return [''.join(random.sample(strn[x:y],len(strn[x:y]))) for x, y in combinations( 
            range(len(strn) + 1), r = 2)] 



# n = int(input())

mock = True
mock_string = 'aabc'

print_query(1,4)

X = readall(4,4))
