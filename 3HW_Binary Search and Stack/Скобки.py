bracket_sequence = input()
def is_correct_bracket_seq(brackets):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for bracket in brackets:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        elif bracket in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[bracket]:
                return 'NO'
            stack.pop()
    
    return 'YES' if not stack else 'NO'

print(is_correct_bracket_seq(bracket_sequence))