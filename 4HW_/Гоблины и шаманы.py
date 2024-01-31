deq = []
results = []

for i in range(int(input())):
    command = input()
    if command[0] == '+': 
        deq.append(command[2:])
    elif command[0] == '*':
        k = len(deq) // 2
        deq.insert(len(deq) % k + k, command[2:])
    elif command[0] == '-':
        print(deq.pop(0))



