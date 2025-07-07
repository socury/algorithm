n = int(input())
sum = 0
for i in list(map(int, input().split())):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                sum += 1
            break

print(sum)