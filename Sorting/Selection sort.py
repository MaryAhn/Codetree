n = int(input())
nums = input()
num = nums.split()
min = 100
min_idx = 0

for i in range(n):
    num[i] = (int)(num[i])

for i in range(n):
    for j in range(i, n):
        if min > num[j]:
            min = num[j]
            min_idx = j
    num[min_idx], num[i] = num[i], num[min_idx]
    min = 100
    min_idx = 0

for i in range(n):
    print(num[i], end=' ')

