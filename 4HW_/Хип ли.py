def is_heap(arr, n):
    for i in range(n // 2):
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
            return "NO"
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
            return "NO"
    return "YES"

n = int(input())
array = [int(i) for i in input().split()]
print(is_heap(array, n))
