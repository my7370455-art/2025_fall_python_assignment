# play snakes and ladders game, give you a board, find the minimum number of moves to reach the end
# the board is n x n, with some cells having snakes or ladders
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        n = len(board)
        def get_coordinates(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col
        
        visited = set()
        queue = deque([(1, 0)])  # (square number, moves)
        visited.add(1)
        while queue:
            position, moves = queue.popleft()
            if position == n * n:
                return moves
            for i in range(1, 7):
                next_pos = position + i
                if next_pos > n * n:
                    continue
                r, c = get_coordinates(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        return -1