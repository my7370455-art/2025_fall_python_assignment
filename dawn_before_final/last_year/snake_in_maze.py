from collections import deque
def bfs(grid, n):
    steps = [[-1]*n for _ in range(n)]
    queue = deque() # state 1 stands for horizontal, 0 stands for vertical
    steps[0][0] = 0
    steps[0][1] = 0
    queue.append((0, 1, 1))
    while queue:
        x, y, state = queue.popleft()
        if x == n-1 and y == n-1 and state == 1:
            return steps[x][y]
        if state == 1:
            ny = y + 1
            nx = x
            if ny < n and grid[nx][ny] == 0 and steps[nx][ny] == -1:
                steps[nx][ny] = steps[x][y] + 1
                queue.append((nx, ny, 1))
            ny = y
            nx = x + 1
            if nx < n and grid[nx][ny] == 0 and grid[nx][ny-1] == 0 and steps[nx][ny] == -1:
                steps[nx][ny] = steps[x][y] + 1
                queue.append((nx, ny, 1))
            nx = x + 1
            ny = y - 1
            if nx < n and ny >= 0 and grid[nx][ny] == 0 and steps[nx][ny] == -1 and grid[nx][ny+1] == 0:
                steps[nx][ny] = steps[x][y] + 1
                queue.append((nx, ny, 0))
        else:
            nx = x + 1
            ny = y
            if nx < n and grid[nx][ny] == 0 and steps[nx][ny] == -1:
                steps[nx][ny] = steps[x][y] + 1
                queue.append((nx, ny, 0))
            nx = x
            ny = y + 1
            if ny < n and grid[nx][ny] == 0 and grid[nx-1][ny] == 0 and steps[nx][ny] == -1:
                steps[nx][ny] = steps[x][y] + 1
                queue.append((nx, ny, 0))
            nx = x - 1
            ny = y + 1
            if nx >= 0 and ny < n and grid[nx][ny] == 0 and steps[nx][ny] == -1 and grid[nx+1][ny] == 0:
                steps[nx][ny] = steps[x][y] + 1
                queue.append((nx, ny, 1))
    return steps[n-1][n-1]

n = int(input().strip())
grid = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    grid.append(row)
print(bfs(grid, n))