from collections import deque
s = input()
answer = ""
stack = deque()
check = False
for i in s:
    if "<" == i:
        check = True
        for _ in range(len(stack)):
            answer += stack.pop()

    stack.append(i)

    if ">" == i:
        check = False
        for _ in range(len(stack)):
            answer += stack.popleft()

    if i == " " and not check:
        for j in range(len(stack)):
            if j == 0:
                stack.pop()
                continue
            answer += stack.pop()
        answer += ' '

if len(stack) != 0:
    for _ in range(len(stack)):
        answer += stack.pop()

print(answer)