class MagicDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self
            for char in word:
                if char not in node.children:
                    node.children[char] = MagicDictionary()
                node = node.children[char]
            node.is_end = True
        

    def search(self, searchWord: str) -> bool:
        def _dfs(self, node, index: int, modified: bool) -> bool:
            if index == len(searchWord):
                return modified and node.is_end
            char = searchWord[index]
            if char in node.children:
                if _dfs(self, node.children[char], index + 1, modified):
                    return True
            if not modified:
                for child_char, child_node in node.children.items():
                    if child_char != char:
                        if _dfs(self, child_node, index + 1, True):
                            return True
                        
            return False
        return _dfs(self, self, 0, False)

from typing import List
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)