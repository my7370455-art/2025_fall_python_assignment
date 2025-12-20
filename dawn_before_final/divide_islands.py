# give you an n*m grid representing a map where . means water and X means land.
# An island is a maximal 4-directionally connected group of land cells.
# there are 3 lands, find the minimum number of water cells you must convert to land to connect all lands into one island.
import sys
from collections import deque
def min_water_to_connect_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs_mark_island(r, c, island_id):
        queue = deque([(r, c)])
        grid[r][c] = island_id
        while queue:
            x, y = queue.popleft()
            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 'X':
                    grid[nr][nc] = island_id
                    queue.append((nr, nc))

    island_id = 2
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                bfs_mark_island(r, c, island_id)
                island_id += 1

    # Helper function to calculate distance from a specific island to all other cells
    def bfs_distance_from_island(island_id):
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == island_id:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dist[nr][nc] == float('inf'):
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))
        return dist

    # Calculate distances from each of the 3 islands
    dist_from_island_2 = bfs_distance_from_island(2)
    dist_from_island_3 = bfs_distance_from_island(3)
    dist_from_island_4 = bfs_distance_from_island(4)

    min_water = float('inf')

    # 1. Strategy A: Find optimal meeting point (Y-shape or single center)
    for r in range(rows):
        for c in range(cols):
            d2 = dist_from_island_2[r][c]
            d3 = dist_from_island_3[r][c]
            d4 = dist_from_island_4[r][c]
            
            if d2 != float('inf') and d3 != float('inf') and d4 != float('inf'):
                min_water = min(min_water, d2 + d3 + d4 - 2)

    # 2. Strategy B: Sequential connections (Linear chain)
    # Calculate minimum distance between pairs of islands
    def get_min_dist(dist_grid, target_island_id):
        min_d = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == target_island_id:
                    min_d = min(min_d, dist_grid[r][c])
        return max(0, min_d - 1) # Distance is steps - 1 water cells

    dist_2_3 = get_min_dist(dist_from_island_2, 3)
    dist_2_4 = get_min_dist(dist_from_island_2, 4)
    dist_3_4 = get_min_dist(dist_from_island_3, 4)

    # Check all linear combinations
    min_water = min(min_water, dist_2_3 + dist_3_4) # 2-3-4
    min_water = min(min_water, dist_2_4 + dist_3_4) # 2-4-3
    min_water = min(min_water, dist_2_3 + dist_2_4) # 3-2-4

    return min_water

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
print(min_water_to_connect_islands(grid))