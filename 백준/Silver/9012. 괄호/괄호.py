class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # 스택이 비었는가
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # 빈칸

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

for i in range(int(input())):
    stack = Stack()
    s = input()
    for j in s:
        if j == "(":
            stack.push(j)
        else:
            if stack.peek() == "(":
                stack.pop()
            else:
                stack.push(j)
                break

    if stack.is_empty():
        print("YES")
    else:
        print("NO")
