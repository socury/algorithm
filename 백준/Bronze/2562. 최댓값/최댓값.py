li = []
for i in range(9):
    li.append(int(input()))
print(max(li))
for i in range(len(li)):
    if li[i] == max(li):
        print(i+1)
        break