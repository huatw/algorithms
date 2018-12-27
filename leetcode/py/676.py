# use a lot of spaces
class MagicDictionary:
    def __init__(self):
        self.word_cnt = collections.Counter()
        self.original = None

    def buildDict(self, words):
        self.original = set(words)
        for word in words:
            for i in range(len(word)):
                self.word_cnt[word[:i] + '_' + word[i + 1:]] += 1

    def search(self, word):
        for i in range(len(word)):
            modified = word[:i] + '_' + word[i + 1:]
            if word in self.original:
                if self.word_cnt[modified] > 1:
                    return True
            elif modified in self.word_cnt:
                return True
        return False


# trie
Trie = lambda: collections.defaultdict(Trie)
class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, words):
        for word in words:
            node = self.trie
            for ch in word:
                node = node[ch]
            node['$'] = True

    def search(self, word):
        def dfs(idx, node, cnt):
            if cnt > 1:
                return False
            if idx == len(word):
                return '$' in node and cnt == 1
            return any(dfs(idx + 1, next_node, cnt if ch == word[idx] else cnt + 1) \
                        for ch, next_node in node.items() if ch != '$')

        return dfs(0, self.trie, 0)



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
        def dfs(node, idx, cnt):
            if cnt > 1:
                return False
            if idx == len(word):
                return '$' in node and cnt == 1
            return any(dfs(next_node, idx + 1, cnt if word[idx] == ch else cnt + 1) \
                        for ch, next_node in node.items() if ch != '$')

        return dfs(self.trie, 0, 0)

