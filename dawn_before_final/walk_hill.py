# m, n, p means number of rows, columns and number of test cases
# then give you a matrix of n*m representing a hilly area, # means unpassable, number means height
# next p lines give you start and end point like x1 y1 x2 y2
# find the minimum effort to walk from start to end
# effort is defined as the absolute height difference between two consecutive cells in the path
# dijkstra solution
import heapq
def min_effort_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    effort = [[float('inf')] * cols for _ in range(rows)]
    effort[start[0]][start[1]] = 0
    min_heap = [(0, start[0], start[1])]
    if grid[start[0]][start[1]] == '#' or grid[end[0]][end[1]] == '#':
        return "NO"

    while min_heap:
        current_effort, x, y = heapq.heappop(min_heap)
        if (x, y) == end:
            return current_effort
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                height_diff = abs(int(grid[nx][ny]) - int(grid[x][y]))
                next_effort = max(current_effort, height_diff)
                if next_effort < effort[nx][ny]:
                    effort[nx][ny] = next_effort
                    heapq.heappush(min_heap, (next_effort, nx, ny))
    return "NO"

m, n, p = map(int, input().strip().split())
grid = [list(input().split()) for _ in range(m)]
for _ in range(p):
    x1, y1, x2, y2 = map(int, input().strip().split())
    start = (x1, y1)
    end = (x2, y2)
    result = min_effort_path(grid, start, end)
    print(result)