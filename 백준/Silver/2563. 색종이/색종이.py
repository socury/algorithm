li = [[0 for _ in range(100)] for _ in range(100)]

for i in range(int(input())):
    n, m = map(int, input().split())
    for j in range(n, n + 10):
        for k in range(m, m + 10):
            li[j][k] = 1

count = 0
for row in li:
    count += row.count(1)

print(count)