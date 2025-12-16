class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end_of_word = False
        
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            
            def insert(self, word: str) -> None:
                node = self.root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end_of_word = True

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(x: int, y: int, node: TrieNode, path: str) -> None:
            if node.is_end_of_word:
                result.add(path)
            node.is_end_of_word = False  # Avoid duplicate entries

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return
            
            char = board[x][y]
            if char not in node.children:
                return
            
            board[x][y] = '#'  # Mark as visited
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, node.children[char], path + char)
            board[x][y] = char  # Restore original character

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root, "")
        return list(result)