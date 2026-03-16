n, m = map(int, input().split())
li1 = []
li2 = []
for i in range(n):
    li1.append(list(map(int, input().split())))

for i in range(n):
    li2.append(list(map(int, input().split())))

for i in range(n):
    temp = []
    for j in range(m):
        temp.append(li1[i][j] + li2[i][j])
    print(*temp)
