from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, element):
        self.dq.append(element)

    def empty(self):
        if self.dq:
            return 0
        else:
            return 1

    def pop(self):
        res = self.dq.popleft()
        return res

    def front(self):
        return self.dq[0]

    def size(self):
        return len(self.dq)

n = int(input())
res = []
queue = Queue()

for i in range(n):
    tmp = input()
    cmd = tmp.split()

    if cmd[0] == 'push':
        queue.push(int(cmd[1]))

    elif cmd[0] == 'pop':
        tmp = queue.pop()
        res.append(tmp)

    elif cmd[0] == 'size':
        res.append(queue.size())

    elif cmd[0] == 'empty':
        res.append(queue.empty())

    elif cmd[0] == 'front':
        res.append(queue.front())

for i in range(len(res)):
    print(res[i])


