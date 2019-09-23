import random
import sys
import time

sys.setrecursionlimit(2**32//2-1)

scale = 1000000

data = [0] * scale

for i in range(scale):
    data[i] = random.randint(1, 1000000)


def quickSort(arr, min, max):
    if min < max:
        part = partition(arr, min, max)
        quickSort(arr, min, part - 1)
        quickSort(arr, part + 1, max)


def partition(arr, min, max):
    i = min - 1
    pivot = arr[max]
    for j in range(min, max):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[max] = arr[max], arr[i + 1]
    return i + 1;


n = len(data)
start = time.time_ns()
quickSort(data, 0, n - 1)
end = time.time_ns()
# print("The sorted array is:")
# for i in range(n):
#     print("%d" % data[i])
print((end-start) / (10**9))