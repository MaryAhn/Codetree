from collections import deque

q = deque()
graph = list(map(int, input().split()))
n = len(graph)
visited = [-1 for _ in range(n)]
res = []
q.appendleft(0)

while len(res) != len(graph):
    present = q.popleft()
    print(present)
    if visited[present] == -1:
        visited[present] = 0
        q.appendleft(present)
        res.append(graph[present])

    left = 2 * present + 1
    right = 2 * present + 2

    if left < n:
        q.append(left)
    if right < n:
        q.append(right)

print(res)
