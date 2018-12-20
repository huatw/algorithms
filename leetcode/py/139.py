# DP IMPORTANT
class Solution:
    def wordBreak(self, s, words):
        word_set = set(words)
        res = [False] * (len(s) + 1)
        res[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in word_set and res[j]:
                    res[i] = True
                    break

        return res[-1]


# Tire tree with cache
class Solution:
    def wordBreak(self, s, words):
        def with_cache(fn):
            cache = {}
            def wrapper(start, end, trie):
                if (start, end) not in cache:
                    cache[(start, end)] = fn(start, end, trie)
                return cache[(start, end)]
            return wrapper

        def build_trie(words):
            trie = {}
            for word in words:
                node = trie
                for ch in word:
                    if ch not in node:
                        node[ch] = {}
                    node = node[ch]
                node['$'] = True
            return trie

        @with_cache
        def search(start, end, trie):
            node = trie
            for i in range(start, end):
                if '$' in node and search(i, end, trie):
                    return True
                if s[i] not in node:
                    return False
                node = node[s[i]]
            return '$' in node

        return search(0, len(s), build_trie(words))




class Solution:
    def wordBreak(self, s, words):
        def with_cache(fn):
            cache = {}
            def wrapper(start):
                if start not in cache:
                    cache[start] = fn(start)
                return cache[start]
            return wrapper

        @with_cache
        def search(idx):
            if idx == len(s):
                return True
            return any(search(i) for i in range(idx + 1, len(s) + 1) if s[idx:i] in word_set)
        word_set = set(words)
        return search(0)


