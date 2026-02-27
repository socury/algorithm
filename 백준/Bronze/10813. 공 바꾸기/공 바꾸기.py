n, m = map(int, input().split())
li = [x for x in range(1, n+1)]
for x in range(m):
    i, j = map(int, input().split())
    li[i-1], li[j-1] = li[j-1], li[i-1]
print(*li)