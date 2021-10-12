n = int(input())
graph = list(map(int, input().split()))
stack = [0]
visited = [-1 for _ in range(n)]
res = []

while len(res) != len(graph):
    present = stack.pop()
    left = 2 * present + 1
    right = 2 * present + 2

    if visited[present] == -1:
        res.append(graph[present])
        stack.append(present)
        visited[present] += 1

    if left < n or right < n:
        if visited[left] == -1 and left < n:
            stack.append(left)
        elif visited[right] == -1 and right < n:
            stack.append(right)

print(res)







