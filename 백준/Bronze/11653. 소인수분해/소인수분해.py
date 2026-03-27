n = int(input())
m = 2
result = []
for i in range(2, n+1):
    while n % i == 0:
        n = n / m
        result.append(m)
    m += 1
    
    if n == 0:
        break

for i in result:
    print(i)