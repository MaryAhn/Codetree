from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, element):
        self.dq.append(element)

    def empty(self):
        if self.dq:
            return False
        else:
            return True

    def pop(self):
        if(len(self.dq) != 0):
            res = self.dq.popleft()
            return res
        else:
            return False

    def front(self):
        if(len(self.dq) != 0):
            return self.dq[0]
        else:
            return False

    def size(self):
        return len(self.dq)

queue = Queue()

n_k = input()
n_k = n_k.split()
n, k = int(n_k[0]), int(n_k[1])
res = []

for i in range(1, n+1):
    queue.push(i)

while queue.empty() is False:
    for _ in range(k-1):
        queue.push(queue.pop())
    res.append(queue.front())
    queue.pop()

for i in range(n):
    print(res[i], end=' ')