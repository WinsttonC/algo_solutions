len_a = int(input())
a = [int(i) for i in input().split()]

#сортировка пузырьком
# for i in range(len_a):
#     for j in range(i+1, len_a):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]



# #быстрая сортировка
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)

# print(' '.join([str(num) for num in quick_sort(a)]))

#mergesort
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

print(' '.join([str(num) for num in merge_sort(a)]))