n = int(input())

cnt = n

for i in range(n):
    s = input()
    li = ["*"]
    for j in s:
        if j in li and j != li[-1]:
            cnt -= 1
            break
        li.append(j)

print(cnt)