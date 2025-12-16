class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x, y, index):
            if index == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index]:
                return False
            char = board[x][y]
            board[x][y] = '#'
            found = (backtrack(x + 1, y, index + 1) or
                     backtrack(x - 1, y, index + 1) or
                     backtrack(x, y + 1, index + 1) or
                     backtrack(x, y - 1, index + 1))
            board[x][y] = char
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
                
        return False