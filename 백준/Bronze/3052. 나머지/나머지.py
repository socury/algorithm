li = []
for i in range(10):
    li.append(int(input()))
print(len(set([x%42 for x in li])))