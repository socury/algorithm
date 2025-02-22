import sys
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty() == 0:
            return self.items.pop(0)
        else:
            return -1

    def size(self):
        return len(self.items)

    def front(self):
        if self.is_empty() == 0:
            return self.items[0]
        else:
            return -1

    def back(self):
        if self.is_empty() == 0:
            return self.items[-1]
        else:
            return -1

queue = Queue()
for _ in range(int(input())):
    s = input()
    if s[:4] == 'push':
        queue.enqueue(s.split()[1])
    elif s[:3] == 'pop':
        print(queue.dequeue())
    elif s[:4] == 'size':
        print(queue.size())
    elif s[:5] == 'empty':
        print(queue.is_empty())
    elif s[:5] == 'front':
        print(queue.front())
    elif s[:4] == 'back':
        print(queue.back())
