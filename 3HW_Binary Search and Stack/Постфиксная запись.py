def evaluate_postfix(expression):
    stack = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    for token in expression.split():
        if token in operators:     
            y, x = stack.pop(), stack.pop()
            stack.append(operators[token](x, y))
        else:
            stack.append(int(token))

    return stack[0]

expression = input()
output = evaluate_postfix(expression)
print(output)
