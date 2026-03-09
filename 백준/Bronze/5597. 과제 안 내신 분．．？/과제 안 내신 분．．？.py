li = []
result = []
for i in range(28):
    li.append(int(input()))
for i in range(1, 31):
    if i not in li:
        result.append(i)
print(*result)