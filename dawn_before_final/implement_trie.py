class Trie:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        for char in word:
            if char not in self.children:
                self.children[char] = Trie()
            self = self.children[char]
        self.is_end_of_word = True

    def search(self, word: str) -> bool:
        for char in word:
            if char not in self.children:
                return False
            self = self.children[char]
        return self.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        for char in prefix:
            if char not in self.children:
                return False
            self = self.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)