w, h, n = map(int, input().split())
def min_board_side(w, h, n):
    left, right = max(w, h), max(w, h) * n
    while left < right:
        mid = (left + right) // 2
        rows = mid // h
        cols = mid // w
        if rows * cols >= n:
            right = mid
        else:
            left = mid + 1
    return left
 
print(min_board_side(w, h, n))