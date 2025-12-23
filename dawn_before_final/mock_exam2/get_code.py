from collections import deque
def cal_power(n):
    power = 0
    current = 1
    while current <= n:
        power += 1
        current *= 2
    return power - 1

string = list(input())
n = len(string)
buffer_code = deque()
for i in range(cal_power(n) + 1):
    buffer_code.append(string[2**i - 1])
output = ''
while len(buffer_code) > 1:
    first = buffer_code.popleft()
    second = buffer_code.pop()
    output += first + second

if buffer_code:
    output += buffer_code.popleft()

print(output)