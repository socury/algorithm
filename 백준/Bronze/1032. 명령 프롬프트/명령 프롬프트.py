li = []

for i in range(int(input())):
    s = input()
    li.append(s)

answer = []
for i in li[0]:
    answer.append(i)

for i in range(1, len(li)):
    for j in range(len(li[0])):
        if answer[j] != li[i][j]:
            answer[j] = "?"

        else:
            answer[j] = li[i][j]

for i in answer:
    print(i, end="")