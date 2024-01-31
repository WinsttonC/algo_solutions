def sift_down(heap, idx):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < len(heap) and heap[left] > heap[largest]:
        largest = left

    if right < len(heap) and heap[right] > heap[largest]:
        largest = right

    if largest != idx:
        heap[idx], heap[largest] = heap[largest], heap[idx]
        sift_down(heap, largest)

def sift_up(heap, idx):
    while idx > 0 and heap[idx] > heap[(idx - 1) // 2]:
        heap[idx], heap[(idx - 1) // 2] = heap[(idx - 1) // 2], heap[idx]
        idx = (idx - 1) // 2

def insert(heap, item):
    heap.append(item)
    sift_up(heap, len(heap) - 1)

def extract(heap):
    if len(heap) == 1:
        return heap.pop()
    root = heap[0]
    heap[0] = heap.pop()
    sift_down(heap, 0)
    return root

n = int(input())
commands = [input().strip() for _ in range(n)]

heap = []
results = []

for command in commands:
    if command.startswith('0'):
        _, number = command.split()
        insert(heap, int(number))
    elif command == '1':
        results.append(extract(heap))

for result in results:
    print(result)

