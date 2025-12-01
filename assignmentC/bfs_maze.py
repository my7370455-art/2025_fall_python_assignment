#given a n*m maze with walls(1) and paths(0), find the smallest number of steps
#from the top_left corner to every other cell using BFS
#if it is not possible to reach a cell, mark it as -1, return the resulting grid
from collections import deque
def bfs_maze(maze, n, m):
    # Initialize the result grid with -1
    result = [[-1 for _ in range(m)] for _ in range(n)]
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS initialization
    queue = deque()
    
    # Start from the top-left corner if it's a path
    if maze[0][0] == 0:
        queue.append((0, 0))
        result[0][0] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds and is a path
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
                # If the cell has not been visited yet
                if result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))
    
    return result

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
result = bfs_maze(maze, n, m)
for row in result:
    print(' '.join(map(str, row)))