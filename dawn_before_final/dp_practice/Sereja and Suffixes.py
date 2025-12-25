n, m = map(int, input().split())
arr = list(map(int, input().split()))
distinct_numbers = set()
dp_table = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    number = arr[i]
    if number in distinct_numbers:
        dp_table[i] = dp_table[i + 1]
    else:
        distinct_numbers.add(number)
        dp_table[i] = dp_table[i + 1] + 1

for _ in range(m):
    l = int(input()) - 1
    print(dp_table[l])