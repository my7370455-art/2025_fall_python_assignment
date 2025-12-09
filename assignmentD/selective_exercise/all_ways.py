def find_all_ways(maze, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    num_steps = set()
    def dfs(x, y, steps):
        nonlocal num_steps
        if x == n - 1 and y == m - 1:
            num_steps.add(steps)
            return
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, steps + 1)
                visited[nx][ny] = False
    visited[0][0] = True
    dfs(0, 0, 0)
    return num_steps

n, m, wanted_steps = map(int, input().strip().split())
maze = [list(map(int, input().strip().split())) for _ in range(n)]
out_set = find_all_ways(maze, n, m)
if  wanted_steps in out_set:
    print("Yes")
else:
    print("No")
