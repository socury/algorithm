while 1:
    stack = []
    a = input()
    if a == ".":
        break

    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print("no")
                break

        elif j == '[':
            stack.append(j)
        elif j == ']':
            if  stack and stack[-1] == '[':
                stack.pop()
            else:
                print("no")
                break

    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")