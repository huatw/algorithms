class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word):
        node = self.trie
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '$' in node

    def startsWith(self, prefix):
        node = self.trie
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

