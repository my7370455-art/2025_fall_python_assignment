# give you a big integer string, and the number of numbers you will delete, find the smallest possible number string after deletion
def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    final_stack = stack[:-k] if k else stack
    result = ''.join(final_stack).lstrip('0')
    return result if result else '0'

num = str(input().strip())
k = int(input().strip())
print(remove_k_digits(num, k))