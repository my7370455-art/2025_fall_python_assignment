operator = list(input().split(' '))
operator.reverse()
stack = []
for op in operator:
    if op == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif op == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a - b)
    elif op == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif op == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(a / b)
    else:
        stack.append(float(op))
print(f'{stack[0]:.6f}')