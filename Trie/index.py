
class Trie:
    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        parent = self.root
        for i,char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.endhere = True

    def search(self, word: str) -> bool:
        parent = self.root 
        for char in word:
            if char not in parent.children:
               return False
            parent = parent.children[char]
        return parent.endhere

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True
