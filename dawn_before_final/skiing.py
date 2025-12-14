from functools import lru_cache

r, c = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(r)]
dp = [[1] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
@lru_cache(None)
def dfs(x: int, y: int):
    if visited[x][y]:
        return dp[x][y]
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] < grid[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]
max_path = 0
for i in range(r):
    for j in range(c):
        max_path = max(max_path, dfs(i, j))
print(max_path)
