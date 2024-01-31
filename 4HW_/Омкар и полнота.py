def generate_complete_array(n):
    a = []

    x, y = 1, 2
    for _ in range(n):
        a.append(x)
        x, y = y, x + y + 1

    return a

for _ in range(int(input())):

    n = int(input())
    print(' '.join([str(elem) for elem in generate_complete_array(n)]))