n = int(input())
nums = input()
num = nums.split()

for i in range(n):
    num[i] = (int)(num[i])

def swap(num, i, j):
    tmp = num[j]
    num[j] = num[i]
    num[i] = tmp

    return num

def partition(num, low, high, pvt):
    pivot = num[pvt]
    i = low - 1
    for j in range(low, high):
        if num[j] < pivot:
            i += 1
            swap(num, i, j)
    swap(num, i + 1, high)
    return i + 1

def quick_median(num, low, high, pvt):
    pos = partition(num, low, high, pvt)
    print(pos)
    if pos == len(num) // 2:
        return pos
    else:
        if low < high:
            pos = partition(num, low, high, pvt)
            if pos < len(num) // 2:
                pos = pos + 1
            else:
                pos = pos - 1
            return quick_median(num, low, high, pos)

mid = quick_median(num, 0, n-1, n-1)
print(num[mid])