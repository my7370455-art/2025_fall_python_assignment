n = int(input())
arr = list(map(int, input().split()))
ways = 0
if arr[0] != 0:
    ways += 1
for i in range(1, n):
    if arr[i-1] < i and arr[i] > i:
        ways += 1
if arr[-1] != n:
    ways += 1

print(ways)
        