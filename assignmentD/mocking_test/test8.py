# give you a string of parentheses, find the longest substring that is valid
def longest_valid_parentheses(s: str) -> int:
    max_length = 0
    stack = [-1]

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length

str = input().strip()
print(longest_valid_parentheses(str))