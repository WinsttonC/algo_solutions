n = int(input())
lst = [int(i) for i in input().split()]
directions = [elem for elem in input()]
v_c = [0] * len(lst)
l_stack = []
r_stack = []
v_c = [0] * n

for i in range(len(lst)-1):
    if not l_stack or l_stack[-1] > lst[i]:
        l_stack.append(lst[i])
    else:
        while l_stack and l_stack[-1] < lst[i]:
            l_stack.pop()
        l_stack.append(lst[i])

    if not r_stack or r_stack[-1] > lst[n-1-i]:
        r_stack.append(lst[n-1-i])
    else:
        while r_stack and r_stack[-1] < lst[n-1-i]:
            r_stack.pop()
        r_stack.append(lst[n-1-i])

    if directions[n-i-2] == 'R':
        v_c[n-i-2] = len(r_stack)

    if directions[i+1] == 'L':
        v_c[i+1] = len(l_stack)


print(' '.join([str(i) for i in v_c]))