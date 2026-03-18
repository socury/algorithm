n, b = input().split()
li = []
result = 0
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in n:
    li.append(s.find(i))
a = 0
for i in li[::-1]:
    result += i * (int(b) ** a)
    a += 1
print(result)