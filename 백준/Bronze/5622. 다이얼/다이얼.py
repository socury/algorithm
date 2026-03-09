s = input()
li = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0
for i in s:
    for j in range(len(li)):
        if i in li[j]:
            result += (j+3)
print(result)    