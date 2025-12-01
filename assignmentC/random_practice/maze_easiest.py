from collections import deque
def find_smallest_steps(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    steps = [[-1 for _ in range(m)] for _ in range(n)]
    steps[0][0] = 0
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
                if steps[nx][ny] == -1:
                    steps[nx][ny] = steps[x][y] + 1
                    q.append((nx, ny))
    return steps[n-1][m-1]

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
result = find_smallest_steps(maze, n, m)
print(result)