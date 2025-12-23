import sys
from functools import cmp_to_key

# Custom comparator: returns -1 if x should come before y
def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

# Read inputs
# Using sys.stdin.read().split() is often safer for competitive programming 
# to handle all whitespace/newlines automatically
input_data = sys.stdin.read().split()
if not input_data:
    exit()

iterator = iter(input_data)
m = int(next(iterator))
n = int(next(iterator))

number_list = []
for _ in range(n):
    number_list.append(next(iterator))

# Sort using the custom comparator
# This ensures that for any subset we pick, the relative order is optimal
number_list.sort(key=cmp_to_key(compare))

# DP Initialization
# dp[i] = max value with exactly i digits
dp = [-1] * (m + 1)
dp[0] = 0

for num_str in number_list:
    length = len(num_str)
    num_val = int(num_str)
    # Iterate backwards to avoid using the same number multiple times for one state
    for j in range(m, length - 1, -1):
        if dp[j - length] != -1:
            # Append current number to the end of the best previous number
            new_val = dp[j - length] * (10 ** length) + num_val
            if new_val > dp[j]:
                dp[j] = new_val

# Find the largest value among all valid lengths
# Since they are integers, a longer number is always larger.
# So we just look from m down to 0.
for j in range(m, -1, -1):
    if dp[j] != -1:
        print(dp[j])
        break

