from collections import deque

class Deque:
    def __init__(self):
        self. dq = deque()

    def push_front(self, element):
        self.dq.appendleft(element)

    def push_back(self, element):
        self.dq.append(element)

    def pop_front(self):
        if(len(self.dq) != 0):
            return self.dq.popleft()
        else:
            return False

    def pop_back(self):
        if(len(self.dq) != 0):
            return self.dq.pop()
        else:
            return False

    def size(self):
        return len(self.dq)

    def empty(self):
        if len(self.dq) == 0:
            return True
        else:
            return False

    def front(self):
        return self.dq[0]

    def back(self):
        return self.dq[-1]

dq = Deque()
n = int(input())

for i in range(1, n+1):
    dq.push_back(i)

while dq.size() > 1:
    dq.pop_front()
    dq.push_back(dq.pop_front())

print(dq.pop_front())

