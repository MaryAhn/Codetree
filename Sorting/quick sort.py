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

def partition(num, low, high):
    pivot = num[high]
    i = low - 1
    for j in range(low, high):
        if num[j] < pivot:
            i += 1
            swap(num, i, j)
    swap(num, i + 1, high)
    return i + 1

def quick_sort(num, low, high):
    if low < high:
        print(low, high)
        pos = partition(num, low, high)

        quick_sort(num, low, pos-1)
        quick_sort(num, pos+1, high)

    return num

num = quick_sort(num, 0, n-1)

for i in range(n):
    print(num[i], end=' ')