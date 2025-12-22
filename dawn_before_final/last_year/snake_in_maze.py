from collections import deque

def bfs(grid, n):
    # steps[x][y][state] -> state 0: horizontal, 1: vertical
    # We use (x, y) as the HEAD position
    steps = [[[-1, -1] for _ in range(n)] for _ in range(n)]
    queue = deque() 
    
    # Starting state: Head at (0, 1), Horizontal (0)
    steps[0][1][0] = 0
    queue.append((0, 1, 0))
    
    while queue:
        x, y, state = queue.popleft()
        dist = steps[x][y][state]
        
        # Target: Head at (n-1, n-1) and Horizontal (0)
        if x == n-1 and y == n-1 and state == 0:
            return dist
            
        if state == 0: # HORIZONTAL
            # 1. Move Right
            nx, ny = x, y + 1
            if ny < n and grid[nx][ny] == 0 and steps[nx][ny][0] == -1:
                steps[nx][ny][0] = dist + 1
                queue.append((nx, ny, 0))
            # 2. Move Down (Must check both cells occupied by snake)
            nx, ny = x + 1, y
            if nx < n and grid[nx][ny] == 0 and grid[nx][ny-1] == 0 and steps[nx][ny][0] == -1:
                steps[nx][ny][0] = dist + 1
                queue.append((nx, ny, 0))
            # 3. Rotate Clockwise (Check the 2x2 area)
            if x + 1 < n and grid[x+1][y] == 0 and grid[x+1][y-1] == 0 and steps[x+1][y-1][1] == -1:
                steps[x+1][y-1][1] = dist + 1
                queue.append((x+1, y-1, 1))
                
        else: # VERTICAL
            # 1. Move Down
            nx, ny = x + 1, y
            if nx < n and grid[nx][ny] == 0 and steps[nx][ny][1] == -1:
                steps[nx][ny][1] = dist + 1
                queue.append((nx, ny, 1))
            # 2. Move Right (Must check both cells occupied by snake)
            nx, ny = x, y + 1
            if ny < n and grid[nx][ny] == 0 and grid[nx-1][ny] == 0 and steps[nx][ny][1] == -1:
                steps[nx][ny][1] = dist + 1
                queue.append((nx, ny, 1))
            # 3. Rotate Counter-Clockwise (Check the 2x2 area)
            if y + 1 < n and grid[x][y+1] == 0 and grid[x-1][y+1] == 0 and steps[x-1][y+1][0] == -1:
                steps[x-1][y+1][0] = dist + 1
                queue.append((x-1, y+1, 0))
                
    return -1

# Input handling
import sys
input_data = sys.stdin.read().split()
if not input_data:
    exit()
n = int(input_data[0])
grid = []
idx = 1
for r in range(n):
    grid.append([int(x) for x in input_data[idx:idx+n]])
    idx += n

print(bfs(grid, n))