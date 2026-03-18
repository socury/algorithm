s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, input().split())
answer = ""

while n != 0:
    answer = s[n % b] + answer
    n //= b

print(answer)