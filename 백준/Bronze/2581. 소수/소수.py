import math
m = int(input())
n = int(input())
li = []
def primenum(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if i <= 1:
        continue
    if primenum(i):
        li.append(i)

if li == []:
    print(-1)
else:
    print(sum(li))
    print(min(li))