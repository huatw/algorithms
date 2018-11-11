class MagicDictionary:
    def __init__(self):
        self.trie = {}

    def buildDict(self, words):
        for word in words:
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = True

    def search(self, word):
        def search_word(node, word, cnt):
            if cnt == 1:
                for ch in word:
                    if ch not in node:
                        return False
                    node = node[ch]
                return '$' in node
            # 1. match and search
            # 2. not match and search
            for ch, next_node in node.items():
                if ch != '$' and word and search_word(node[ch], word[1:], cnt if ch == word[0] else cnt + 1):
                    return True
            return False
        return search_word(self.trie, word, 0)

