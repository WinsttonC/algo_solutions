deques = {}
output = []
for i in range(int(input())):
    command = input()
    parts = command.split()
    action = parts[0]
    deque_number = int(parts[1])

    if deque_number not in deques:
        deques[deque_number] = []

    if action == 'pushfront':
        deques[deque_number].insert(0, int(parts[2]))
    elif action == 'pushback':
        deques[deque_number].append(int(parts[2]))
    elif action == 'popfront':
        if deques[deque_number]:
            output.append(deques[deque_number].pop(0))
    elif action == 'popback':
        if deques[deque_number]:
            output.append(deques[deque_number].pop())

print(' '.join([str(elem) for elem in output]))