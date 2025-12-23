import sys
lines = sys.stdin.read().strip().split('\n')
stack = []
min_stack = []
for line in lines:
    if len(line) != 3:
        a, b = map(str, line.strip().split())
        b = int(b)
        stack.append(b)
        if not min_stack or b <= min_stack[-1]:
            min_stack.append(b)

    elif line == 'pop':
        if stack:
            top = stack.pop()
            if top == min_stack[-1]:
                min_stack.pop()
    elif line == 'min':
        if stack:
            print(min_stack[-1])