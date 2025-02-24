from collections import deque
queue = deque()
for _ in range(int(input())):
    s = input()
    if s[:9] == 'push_back':
        queue.append(s.split()[1])
    elif s[:10] == 'push_front':
        queue.appendleft(s.split()[1])

    elif s[:9] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif s[:8] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif s[:4] == 'size':
        print(len(queue))

    elif s[:5] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif s[:5] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        

    elif s[:4] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
