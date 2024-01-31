n = int(input())
stack = []
 
for _ in range(n):
    operation = input().split()
    
    if operation[0] == '1': 
        stack.append(int(operation[1]))
    elif operation[0] == '2': 
        print(stack.pop())