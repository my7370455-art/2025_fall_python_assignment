def find_the_max_weight(maze, n, m):
    max_weight = float('-inf')
    visited = [[False for _ in range(m)] for _ in range(n)]
    def dfs(x, y, current_weight, step_list=[]):
        nonlocal max_weight
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if x == n - 1 and y == m - 1:
            if current_weight > max_weight:
                max_weight = current_weight
                
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, current_weight + maze[nx][ny])
                visited[nx][ny] = False
    visited[0][0] = True
    dfs(0, 0, maze[0][0])
    return max_weight

m, n = map(int, input().strip().split())
maze = [list(map(int, input().strip().split())) for _ in range(m)]
print(find_the_max_weight(maze, m, n))