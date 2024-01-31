def find_x(C):
    left, right = 0, C
    while right - left > 1e-7:
        mid = (left + right) / 2
        if mid ** 2 + mid ** 0.5 > C:
            right = mid
        else:
            left = mid
    return left

C = float(input())
x = find_x(C)
print(x)