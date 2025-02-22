n, k = map(int, input().split())
i = 0
li = [i for i in range(1, n+1)]
answer = []
for _ in range(n):
    i += (k-1)
    if i >= len(li):
        i %= len(li)
    answer.append(li[i])
    li.pop(i)

print("<", end="")
print(*answer, sep=", ", end="")
print(">", end="")