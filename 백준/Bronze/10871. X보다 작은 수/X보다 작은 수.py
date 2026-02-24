n, x = map(int, input().split())
li = list(map(int, input().split()))
result = []
for i in li:
    if i < x:
        result.append(i)
print(*result)