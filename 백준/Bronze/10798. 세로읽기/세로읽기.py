li = []
for i in range(5):
    li.append(input())

for i in range(max(len(x) for x in li)):
    for j in range(5):
        if i < len(li[j]):
            print(li[j][i], end="")