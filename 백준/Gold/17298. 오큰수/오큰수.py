from collections import deque
import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
stack = deque()
answer = list([-1 for _ in range(n)])

for i in range(n):
    while stack and li[stack[-1]] < li[i]:
        answer[stack.pop()] = li[i]
    stack.append(i)

print(" ".join(map(str, answer)))