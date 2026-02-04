n, m = map(int, input().split())
t = int(input())
m += t
if m >= 60:
    n += (m // 60)
    m = (m%60)
    if n >= 24:
        n -= 24
print(n, m)