expression = list(input().split())
# give you a normal expression, you need to convert it to reversed polish note
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
def infix_to_postfix(expression):
    stack = []
    output = []
    for token in expression:
        if token.isalnum():  # If the token is an operand (number/variable)
            output.append(token)
        elif token == '(':  # If the token is '(', push it to the stack
            stack.append(token)
        elif token == ')':  # If the token is ')', pop and output from the stack until an '(' is encountered
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:  # The token is an operator
            while (stack and precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())
            stack.append(token)
    # Pop all the operators from the stack
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

print(infix_to_postfix(expression))