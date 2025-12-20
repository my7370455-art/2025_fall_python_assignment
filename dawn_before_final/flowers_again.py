# you can eat white or red flowers for dinner, however you can only eat white flowers in size k(consecutively)
# determine how many ways you can eat from a to b, a, b means the total number of flowers you will eat
# use dp, prefix sum and deque to achieve an rolling window
# the output may be large, so use modulo 10^9 + 7
# n indicates the total number of testcases
from collections import deque
MOD = 10**9 + 7
n, k = map(int, input().strip().split())
largest_end = -1
cases = []

for _ in range(n):
    start, end = map(int, input().strip().split())
    largest_end = max(largest_end, end)
    cases.append((start, end))

prefix_sum = [0] * (largest_end + 1)
dp_window = deque(maxlen = k + 1)
dp_window.append(1)
for i in range(1, largest_end + 1):
    if i < k:
        dp_value = dp_window[-1] % MOD
        prefix_sum[i] = prefix_sum[i-1] + dp_value
        dp_window.append(dp_value)
    elif i == k:
        dp_value = (dp_window[-1] + 1) % MOD
        prefix_sum[i] = prefix_sum[i-1] + dp_value
        dp_window.append(dp_value)
    else:
        dp_value = dp_window[-1] + dp_window[1]
        dp_value %= MOD
        prefix_sum[i] = prefix_sum[i-1] + dp_value
        dp_window.append(dp_value)

for start, end in cases:
    result = (prefix_sum[end] - prefix_sum[start - 1]) % MOD if start > 1 else prefix_sum[end] % MOD
    print(result) 
