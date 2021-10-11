n = int(input())
nums = input()
num = nums.split()
max = 0
max_idx = 0

for i in range(n):
    num[i] = (int)(num[i])

sorted = False

while not sorted:
    sorted = True
    for i in range(n-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            sorted = False

for i in range(n):
    print(num[i], end=' ')
