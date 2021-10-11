a = input()
n_m = a.split()
n = int(n_m[0])
m = int(n_m[1])
nums = input()
num = nums.split()

targets = []
for i in range(n):
    num[i] = (int)(num[i])
for i in range(m):
    targets.append(int(input()))

def lower_bound(num, target):
    left = 0
    right = len(num) - 1
    min_idx = len(num)

    while left <= right:
        mid = (int)((left + right) / 2)
        if num[mid] >= target:
            right = mid - 1
            min_idx = min(mid, min_idx)
        else:
            left = mid + 1

    return min_idx

def upper_bound(num, target):
    left = 0
    right = len(num) - 1
    min_idx = len(num)

    while left <= right:
        mid = (int)((left + right) / 2)
        if num[mid] > target:
            right = mid - 1
            min_idx = min(mid, min_idx)
        else:
            left = mid + 1

    return min_idx

res = []

for i in range(m):
    res_value = upper_bound(num, targets[i]) - lower_bound(num, targets[i])
    print(res_value)