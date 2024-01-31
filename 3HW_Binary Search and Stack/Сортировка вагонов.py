n = int(input())
wagons = [int(i) for i in input().split()]
def reorder_trains(n, wagons):
    stack = []
    actions = []
    next_wagon = 1

    for wagon in wagons:
        stack.append(wagon)
        actions.append(f"1 1")
        while stack and stack[-1] == next_wagon:
            stack.pop()
            actions.append(f"2 1")
            next_wagon += 1

    if next_wagon - 1 == n:
        return actions
    else:
        return ["0"]



for i in reorder_trains(n, wagons):
    print(i)

