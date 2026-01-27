n, m = map(int, input().split())
m -= 45
if m < 0:
    m += 60
    n -= 1
    if n < 0:
        n += 24
print(n, m)