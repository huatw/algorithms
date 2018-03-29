class Trie:

    def __init__(self):
        self.trie = {}


    def insert(self, word):
        t = self.trie

        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]

        t['$'] = True


    def search(self, word):
        t = self.trie

        for ch in word:
            if ch not in t:
                return False
            t = t[ch]

        return '$' in t


    def startsWith(self, prefix):
        t = self.trie
        for ch in prefix:
            if ch not in t:
                return False
            t = t[ch]

        return True

