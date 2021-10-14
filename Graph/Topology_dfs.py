n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
stack = []
visited = [-1] * n

def dfs(present, visited, graph, stack):
    if visited[present] == -1: # 노드 방문 처리
        visited[present] = 0

    # 작은 번호부터 연결되어 있다면 dfs를 수행함
    for next in range(n):
        if visited[next] == -1 and graph[present][next] != 0:
            dfs(next, visited, graph, stack)
    # dfs의 종료, 즉 연결된 간선이 없는 노드에 도달했을 경우 stack에 append
    stack.append(present)
    return stack

for i in range(n):
    # 작은 번호부터 dfs 수행
    if visited[i] == -1:
        stack = dfs(i, visited, graph, stack)

for i in range(n):
    print(stack.pop() + 1, end=' ')




