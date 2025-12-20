n, k = map(int, input().strip().split())
def dfs(n, current_step, k, largest):
    if current_step == k:
        if n == 0:
            return 1
        else:
            return 0
    if n <= 0:
        return 0
    total_ways = 0
    for i in range(largest, n+1, 1):
        total_ways += dfs(n - i, current_step + 1, k, i)
    return total_ways

print(dfs(n, 0, k, 1))