class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return True
