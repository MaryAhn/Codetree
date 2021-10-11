n = int(input())
nums = input()
num = nums.split()
min = 101
min_idx = 0

for i in range(n):
    num[i] = (int)(num[i])

for i in range(n):
    for j in range(i, n):
        if(num[j]<min):
            min = num[j]
            min_idx = j
    tmp = num[i]
    num[i] = min
    num[min_idx] = tmp
    min = 101

for i in range(n):
    print(num[i], end=' ')
