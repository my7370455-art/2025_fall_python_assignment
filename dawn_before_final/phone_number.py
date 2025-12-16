# give you a bunch of phone numbers, decide if they are consistent
# consistent means no number is prefix of another number
# use trie to solve this problem
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number: str) -> bool:
        current = self.root
        for digit in number:
            if digit not in current.children:
                current.children[digit] = TrieNode()
            current = current.children[digit]
            if current.is_end_of_number:
                return False  # Found a prefix
        if current.children:
            return False  # Current number is a prefix of another number
        current.is_end_of_number = True
        return True
    
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    trie = Trie()
    consistent = True
    for _ in range(n):
        number = input().strip()
        if not trie.insert(number):
            consistent = False
    print("YES" if consistent else "NO")