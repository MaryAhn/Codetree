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
res = []

for i in range(n):
    tmp = input()
    cmd = tmp.split()

    if cmd[0] == 'push_front':
        dq.push_front(int(cmd[1]))

    elif cmd[0] == 'push_back':
        dq.push_back(int(cmd[1]))

    elif cmd[0] == 'pop_front':
        tmp = dq.pop_front()
        res.append(tmp)

    elif cmd[0] == 'pop_back':
        tmp = dq.pop_back()
        res.append(tmp)

    elif cmd[0] == 'size':
        res.append(dq.size())

    elif cmd[0] == 'empty':
        res.append(dq.empty())

    elif cmd[0] == 'front':
        res.append(dq.front())

    elif cmd[0] == 'back':
        res.append(dq.back())

for i in range(len(res)):
    print(res[i])




