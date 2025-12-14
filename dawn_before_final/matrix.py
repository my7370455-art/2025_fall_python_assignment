class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]

        # First pass: check for top and left
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                else:
                    if r > 0:
                        dist[r][c] = min(dist[r][c], dist[r - 1][c] + 1)
                    if c > 0:
                        dist[r][c] = min(dist[r][c], dist[r][c - 1] + 1)

        # Second pass: check for bottom and right
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r < rows - 1:
                    dist[r][c] = min(dist[r][c], dist[r + 1][c] + 1)
                if c < cols - 1:
                    dist[r][c] = min(dist[r][c], dist[r][c + 1] + 1)

        return dist