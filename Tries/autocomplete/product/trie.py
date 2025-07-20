class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.words = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        word_lower = word.lower()
        for char in word_lower:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.words.add(word)

    def starts_with(self, prefix):
        prefix_lower = prefix.lower()
        node = self.root
        for char in prefix_lower:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_words(node, prefix_lower, 15)

    def _collect_words(self, node, prefix, limit):
        results = []
        if node.is_end:
            sorted_words = sorted(node.words, key=lambda s: s.lower())
            for word in sorted_words:
                if len(results) >= limit:
                    return results
                results.append(word)
                
        if len(results) >= limit:
            return results
        
        for char in sorted(node.children.keys()):
            child = node.children[char]
            child_results = self._collect_words(child, prefix + char, limit - len(results))
            results.extend(child_results)
            if len(results) >= limit:
                break
                
        return results