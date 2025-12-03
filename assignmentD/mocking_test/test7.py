# give you a matrix with some islands represented as 1s and water as 0s
# your task is to find the perimeter of the islands
def island_perimeter(grid) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell contributes 4 to the perimeter
                perimeter += 4
                # Check for adjacent land cells to subtract shared edges
                if r > 0 and grid[r - 1][c] == 1:  # Up
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Left
                    perimeter -= 2

    return perimeter

row, col = map(int, input().strip().split())
grid = []
for _ in range(row):
    grid.append(list(map(int, input().strip().split())))
print(island_perimeter(grid))