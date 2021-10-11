def swap(num, i, j):
    tmp = num[i]
    num[i] = num[j]
    num[j] = tmp

def heapify(num, root, n):
    left = 2 * root + 1
    right = 2 * root + 2
    max_idx = root
    if left < n and num[left] > num[max_idx]:
        max_idx = left
    if right < n and num[right] > num[max_idx]:
        max_idx = right

    if max_idx is not root:
        swap(num, root, max_idx)
        heapify(num, max_idx, n)

def heap_sort(num, n):
    mid = (n // 2) - 1
    for i in range(mid, -1, -1):
        heapify(num, i, n)

    for i in range(n-1, 0, -1):
        swap(num, 0, i)
        heapify(num, 0, i)

n = int(input())
nums = input()
num = nums.split()

for i in range(n):
    num[i] = (int)(num[i])

heap_sort(num, n)

for i in range(n):
    print(num[i], end=' ')











