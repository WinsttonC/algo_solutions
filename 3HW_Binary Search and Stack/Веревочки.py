n, k = map(int, input().split())
ropes = [int(input()) for i in range(n)]

def max_rope_length(n, k, ropes):
    def is_possible(length):
        count = 0
        for rope in ropes:
            count += rope // length
        return count >= k
    left, right = 1, max(ropes)
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right if right > 0 else 0



print(max_rope_length(n, k, ropes))
