class Solution:
    def longestWord(self, words: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str) -> None:
                node = self.root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end = True

        solution_length = float('-inf')
        solution_bucket = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        words.sort(key = lambda x: len(x), reverse = True)
        for word in words:
            if len(word) < solution_length:
                break
            node = trie.root
            for i, char in enumerate(word):
                if i == len(word) - 1:
                    solution_bucket.append(word)
                    solution_length = len(word)
                if char in node.children:
                    node = node.children[char]
                    if not node.is_end:
                        break
        solution_bucket.sort()
        return solution_bucket[0] if solution_bucket else ""