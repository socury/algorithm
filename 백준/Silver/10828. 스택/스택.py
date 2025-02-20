class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # 스택이 비었는가
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def push(self, item):
        self.items.append(item)  # 빈칸

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "-1"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "-1"

    def size(self):
        return len(self.items)

stack = Stack()

for i in range(int(input())):
    s = input()
    if "push" in s:
        a, b = s.split(" ")
        stack.push(int(b))
    elif s in "pop":
        print(stack.pop())
    elif s in "size":
        print(stack.size())
    elif s in "empty":
        print(stack.is_empty())
    elif s in "top":
        print(stack.peek())