from utils import *

ss = 0
P = {}
with open('a6.in') as f:
    for line in f.readlines():        
        a,b = line.strip().split(")")
        P[b] = a
        
s1 = 0
for b in P:    
    while (b in P):            
        b = P[b]        
        s1+=1

def find_dist(f,d):
    Y = {}
    ss = 0
    for b in P:
        if (b == f):
            while (b in P):
                b = P[b]
                Y[b] = ss
                ss+=1
    ss = 0
    for b in P:
        if (b == d):
            while (b in P):            
                b = P[b]
                if (b in Y):
                    return ss + Y[b]                    
                ss+=1
                          
print (s1,find_dist("YOU", "SAN"))
#6   00:20:27  1089      0   00:27:13   686      0