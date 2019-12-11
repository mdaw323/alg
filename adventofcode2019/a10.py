from utils import *
from collections import defaultdict
import math

M = set()

ss = 0

with open('a10.in') as f:
    y = 0
    for line in f.readlines():
        x = 0
        for d in line.strip():
            if d == '#':
                M.add(Point(x,y))
            x +=1
        y+=1

mx = 40
my = 40

S = []

for s in M:

    visited = set()
    visited.add(s)
    
    ss = 0
    for x in range(-mx,mx+1):
        for y in range(-my,my+1):
            if x == 0 and y ==0:
                continue
            p = Point(s.x, s.y)
            xx = x
            yy = y
            
            while xx != 0 and yy != 0 and math.gcd(abs(xx),abs(yy)) > 1:
                g = math.gcd(abs(xx),abs(yy))
                xx //= g
                yy //= g
            if xx == 0:
                yy //= abs(yy)
            if yy == 0:
                xx //= abs(xx)
            # print (p,xx,yy)                
            while abs(p.x) <= mx and abs(p.y)<= my:
                p = Point(p.x + xx, p.y + yy)
                if p in M:
                    if p not in visited:
                        ss+=1
                        visited.add(p)
                    break

    S.append(ss)
print (max(S))

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

s = Point(31,20)
v1 = [0,-1]

visited = set()
GG = []

for x in range(0,mx+1):
    for y in range(-mx,my+1):
        if x == 0 and y ==0:
            continue
        p = Point(s.x, s.y)
        xx = x
        yy = y        
        if xx == 0:
            yy //= abs(yy)
        if yy == 0:
            xx //= abs(xx)
        
        if math.gcd(abs(xx),abs(yy)) > 1:
            g = math.gcd(abs(xx),abs(yy))
            xx //= g
            yy //= g
        v2 = [xx,yy]
        
        vp = Point(xx,yy)
        if vp in visited:
            continue
        visited.add(vp)
        # print (v1,v2, angle(v1,v2))
        GG.append( (angle(v1,v2), vp) )


GG = sorted(GG)

PP = []
visited = set()
for pp in GG:
    angle, p = pp
    if p not in visited:
        PP.append(p)
    visited.add(p)
for pp in reversed(GG):
    angle, p = pp
    p = Point(-p.x, p.y)
    if p not in visited:
        PP.append(p)
    visited.add(p)    


visited - set()
shotted = 0
while (shotted <200):
    for v in PP:
        xx = v.x
        yy = v.y
        p = Point(s.x,s.y)
        while abs(p.x) <= mx and abs(p.y)<= my:
            p = Point(p.x + xx, p.y + yy)
            if p in M:
                M.remove(p)
                shotted +=1
                if (shotted == 200):
                    print (shotted,p)
                break
                
