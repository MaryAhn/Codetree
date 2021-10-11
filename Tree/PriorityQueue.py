from Tree import maxheap


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def push(self, element):
        self.pq.append(element)

    def pop(self):
        self.pq = maxheap.build_heap(self.pq)
        res = self.pq[0]
        self.pq = self.pq[1:]

        return res

    def size(self):
        return len(self.pq)

    def empty(self):
        return int(not self.pq)

    def top(self):
        self.pq = maxheap.build_heap(self.pq)
        return self.pq[0]

pq = PriorityQueue()
n = int(input())

for i in range(n):
    tmp = input()
    cmd = tmp.split()

    if cmd[0] == 'push':
        pq.push((int)(cmd[1]))
    elif cmd[0] == 'pop':
        print(pq.pop())
    elif cmd[0] == 'size':
        print(pq.size())
    elif cmd[0] == 'empty':
        print(pq.empty())
    elif cmd[0] == 'top':
        print(pq.top())


