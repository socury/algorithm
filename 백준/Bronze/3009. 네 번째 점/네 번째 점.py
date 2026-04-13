a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
result = []

if a == e:
    result.append(c)
elif a == c:
    result.append(e)
elif c == e:
    result.append(a)


if b == d:
    result.append(f)
elif b == f:
    result.append(d)
elif f == d:
    result.append(b)

print(*result)