class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = {}

        class binary_Trie:
            