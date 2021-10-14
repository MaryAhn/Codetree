from collections import deque
import heapq

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [-1] * n
in_degree = [0] * n
heap = []
res = []

def arrsum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

for i in range(n):
    in_degree[i] = arrsum(graph[i])
    if in_degree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    print(heap)
    present = heapq.heappop(heap)
    res.append(present + 1)
    for i in range(n):
        if graph[i][present] != 0:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(heap, i)

print(res)