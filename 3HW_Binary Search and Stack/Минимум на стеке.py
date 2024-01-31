import sys

stack = []
n = int(sys.stdin.readline())
stack_min = []

for _ in range(n):
    inp = sys.stdin.readline().split()
    operation = inp[0]

    if operation == '1':
        elem = int(inp[1])
        stack.append(elem)
        if not stack_min or elem < stack_min[-1]:
            stack_min.append(elem)
    elif operation == '2':
        if stack[-1] == stack_min[-1]:
            stack_min.pop()
        stack.pop()
    else:
        sys.stdout.write(str(stack_min[-1]) + "\n")






