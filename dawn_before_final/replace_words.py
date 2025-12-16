class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
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

        ans_bucket = []
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        for word in sentence.split():
            node = trie.root
            prefix = ""
            notfind = False
            for i, char in enumerate(word):
                if char in node.children:
                    prefix += char
                    node = node.children[char]
                    if node.is_end_of_word:
                        break
                else:
                    notfind = True
                    break

            if not notfind:
                ans_bucket.append(prefix)
            else:
                ans_bucket.append(word)

        return " ".join(ans_bucket)