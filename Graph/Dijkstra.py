from collections import deque

n = int(input())
graph = []

for i in range(n):
    graph.append(input().split())
for i in range(n):
    for j in range(n):
        graph[i][j] = int(graph[i][j])

dist = [float("inf") for _ in range(n)]
dist[0] = 0

q = deque()

for i in range(n):
    q.appendleft(i)

while len(q) > 0:
    present, mindist = 0, float("inf")
    for item in q:
        if dist[item] < mindist:
            present = item
            mindist = dist[item]
    print(present)
    q.remove(present)

    for i in range(n):
        if graph[present][i] != 0:
            tmp = dist[present] + graph[present][i]
            if tmp < dist[i]:
                dist[i] = tmp
    print(dist)
