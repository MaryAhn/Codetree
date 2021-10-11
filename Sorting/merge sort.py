def merge(num, low, mid, high):
    merged_num = []
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if num[i] < num[j]:
            merged_num.append(num[i])
            i += 1
        else:
            merged_num.append(num[j])
            j += 1
    while i <= mid:
        merged_num.append(num[i])
        i += 1
    while j <= high:
        merged_num.append(num[j])
        j += 1

    idx = 0
    for iter in range(low, high+1):
        num[iter] = merged_num[idx]
        idx += 1

    return merged_num

def merge_sort(num, low, high):
    if low < high:
        mid = int((low + high) / 2)
        merge_sort(num, low, mid)
        merge_sort(num, mid + 1, high)
        merge(num, low, mid, high)

n = int(input())
nums = input()
num = nums.split()

for i in range(n):
    num[i] = (int)(num[i])

merge_sort(num, 0, n-1)

for i in range(n):
    print(num[i], end=' ')