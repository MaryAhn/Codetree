n_m = input()
a = n_m.split()
n = (int)(a[0])
m = (int)(a[1])

nums = input()
num = nums.split()

for i in range(n):
    num[i] = (int)(num[i])

targets = []
for i in range(m):
    targets.append(int(input()))

res = []

def binary_search(num, target):
    n = len(num)

    for i in range(m):
        left = 0
        right = n - 1

        while left <= right:
            mid = (int)((left + right) / 2)
            if target is num[mid]:
                return mid + 1
            else:
                if target < num[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

for i in range(m):
    res.append(binary_search(num, targets[i]))

for j in range(m):
    print(res[j])