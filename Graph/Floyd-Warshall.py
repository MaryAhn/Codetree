n = int(input())
graph = []
dist = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph.append(input().split())
for i in range(n):
    for j in range(n):
        graph[i][j] = int(graph[i][j])
        if graph[i][j] != 0:
            dist[i][j] = graph[i][j]
        elif i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = float('inf')

for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


for i in range(n):
    print(dist[i])