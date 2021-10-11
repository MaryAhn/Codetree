n = int(input())
nums = input()
num = nums.split()
min = 101
min_idx = 0

for i in range(n):
    num[i] = (int)(num[i])

for i in range(1, n):
    j = i - 1
    key = num[i]
    while j>=0 and num[j]>key:
        num[j+1] = num[j]
        j -= 1
    num[j+1] = key


for i in range(n):
    print(num[i], end=' ')
