stack = [0]
li = []
answer = True
i = 0
for _ in range(int(input())):
    n = int(input())
    while 1:
        if n > i:
            i += 1
            stack.append(i)
            li.append("+")
        else:
            if n < stack[-1]:
                answer = False
                break
            else:
                stack.pop()
                li.append("-")
                break

if answer:
    for j in li:
        print(j)
else:
    print("NO")