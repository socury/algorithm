n = int(input())
list = list(map(int, input().split()))
stack = []
m = 1

for i in list:
    stack.append(i)
    while stack != [] and stack[-1] == m:
        stack.pop()
        m += 1
    

if stack == []:
    print("Nice")
else:
    print("Sad")