# use dfs to find the number of islands
from collections import deque
def calc_islands(m, n, matrix):
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count_islands = 0
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                visited[x][y] = True
                continue
            if visited[x][y]:
                continue
            else:
                visited[x][y] = True
                count_islands += 1
                stack = deque()
                stack.append((x, y))
                while stack:
                    cur_x, cur_y = stack.popleft()
                    for dx, dy in directions:
                        new_x, new_y = cur_x + dx, cur_y + dy
                        if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and matrix[new_x][new_y] == 1:
                            visited[new_x][new_y] = True
                            stack.append((new_x, new_y))
    return count_islands

m, n = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
result = calc_islands(m, n, matrix)
print(result)