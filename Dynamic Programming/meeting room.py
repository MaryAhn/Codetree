n = int(input())
time = [[0, 0] for _ in range(n)]

for i in range(n):
    tmp = input().split()
    start, end = int(tmp[0]), (int)(tmp[1])
    time[i][0] = start
    time[i][1] = end

time.sort(key=lambda x:x[1])

res = [time[0]]
idx = 0

for i in range(n):
    if res[idx][1] <= time[i][0]:
        res.append(time[i])
        idx += 1

print(len(res))