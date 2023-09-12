def is_balanced(expression):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}

    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or char != brackets[stack.pop()]:
                return False

    return not stack  # The expression is balanced if the stack is empty

# Testing the function
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
