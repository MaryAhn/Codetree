n = int(input())
graph = []
edges = []

for i in range(n):
    graph.append(input().split())
for i in range(n):
    for j in range(n):
        graph[i][j] = int(graph[i][j])
        if(graph[i][j] != 0):
            edges.append([i, j, graph[i][j]])

mst = []
uf = [-1 for _ in range(n)]
def find(uf, x):
    if uf[x] == -1:
        return x
    tmp = find(uf, uf[x])
    uf[x] = tmp
    return uf[x]

def union(uf, x, y):
    X, Y = find(uf, x), find(uf, y)
    uf[X] = Y
    return uf

edges.sort(key=lambda x:x[2])
res = 0
max_cost = 0

for edge in edges:
    start, end, cost = edge[0], edge[1], edge[2]
    print(edge)
    if find(uf, start) != find(uf, end):
        uf = union(uf, start, end)
        mst.append((start, end))
        res += cost
        max_cost = max(cost, max_cost)
print(mst, res-(max_cost - 1))


