n = int(input())
n -= 1
result = 1
for i in range(n):
    if n <= 0:
        break
    n -= 6 * result
    result += 1
print(result)