li = []
max = 0
result1 = 0
result2 = 0
for i in range(1, 10):
    li.append(list(map(int, input().split())))

for i in range(1, 10):
    for j in range(1, 10):
        if li[i-1][j-1] >= max: 
            max = li[i-1][j-1]
            result1 = i
            result2 = j

print(max)
print(result1, result2)