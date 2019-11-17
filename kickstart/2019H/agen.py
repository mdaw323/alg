import random
print("10")
n = 100
a = [0]*n
for i in range(n):
    a[i] = i
print(n)
print(' '.join([str(x) for x in a]))    

a = [0]*n
for i in range(n):
    a[i] = max(i//2,1)
print(n)
print(' '.join([str(x) for x in a]))

a = [0]*n
for i in range(n):
    a[i] = 1
print(n)
print(' '.join([str(x) for x in a]))    

a = [0]*n
for i in range(n):
    a[i] = max(i//5,1)
print(n)
print(' '.join([str(x) for x in a]))

a = [0]*n
for i in range(n):
    a[i] = max(i//5,1)
random.shuffle(a)
print(n)
print(' '.join([str(x) for x in a]))

n = 100000
a = [0]*n
for i in range(n):
    a[i] = i
print(n)
print(' '.join([str(x) for x in a]))    

a = [0]*n
for i in range(n):
    a[i] = max(i//2,1)
print(n)
print(' '.join([str(x) for x in a]))

a = [0]*n
for i in range(n):
    a[i] = 1
print(n)
print(' '.join([str(x) for x in a]))    

a = [0]*n
for i in range(n):
    a[i] = max(i//5,1)
print(n)
print(' '.join([str(x) for x in a]))

a = [0]*n
for i in range(n):
    a[i] = max(i//5,1)
random.shuffle(a)
print(n)
print(' '.join([str(x) for x in a]))
