def min_removals_for_balanced_parentheses(s):
    stack = []
    unbalanced_count = 0

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                unbalanced_count += 1

    return unbalanced_count + len(stack)

data = input()
output = min_removals_for_balanced_parentheses(data)
print(output)
