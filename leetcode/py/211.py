Trie = lambda : collections.defaultdict(Trie)

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        node = self.trie
        for ch in word:
            node = node[ch]
        node['$'] = True

    def search(self, word, node=None):
        if not node:
            node = self.trie
        for i, ch in enumerate(word):
            if ch == '.':
                return any(self.search(word[i + 1:], v) for k, v in node.items() if k != '$')
            elif ch in node:
                node = node[ch]
            else:
                return False
        return '$' in node
