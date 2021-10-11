def max_heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)



def build_heap(arr):
    n = len(arr)
    for i in range((int)(n/2), -1, -1):
        max_heapify(arr, n, i)

    return arr

def insertion(arr, x):
    n = len(arr)
    arr.append(x)

    i = n
    while i > 0 and arr[i/2] < arr[i]:
        arr[i/2], arr[i] = arr[i], arr[i/2]
        i = i / 2

    return arr

def delete(arr):
    n = len(arr)
    arr[0] = arr[n-1]
    max_heapify(arr, n-1, 1)
