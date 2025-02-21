import sys
from collections import deque

left = deque(sys.stdin.readline().rstrip())
right = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    if "P" == s[0]:
        left.append(s[-1])
    elif "L" == s[0]:
        if len(left) != 0:
            right.appendleft(left.pop())
    elif "D" == s[0]:
        if len(right) != 0:
            left.append(right.popleft())
    elif "B" == s[0]:
        if len(left) != 0:
            left.pop()

print("".join(left) + "".join(right))