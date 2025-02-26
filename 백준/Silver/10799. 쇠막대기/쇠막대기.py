from collections import deque
stack = deque()
cnt = 0
last = ''
for i in input():
    if i == ")":
        stack.pop()
        if last == "(":
            cnt += len(stack)
        else:
            cnt += 1
    else:
        stack.append(i)
    last = i
print(cnt)
