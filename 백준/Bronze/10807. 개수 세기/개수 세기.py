x = int(input())
li = list(map(int, input().split()))
n = int(input())
result = 0
for i in li:
    if i == n:
        result += 1

print(result)