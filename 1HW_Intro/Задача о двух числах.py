for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    d = abs(b - a)
    steps_nubmer = 0
    if d % 10 == 0:
        steps_nubmer = d // 10
    else:
        steps_nubmer = d // 10 + 1
    print(steps_nubmer)