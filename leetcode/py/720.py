import functools

class Solution:
    def longestWord(self, words):
        len_words_map = collections.defaultdict(set)
        for word in words:
            len_words_map[len(word)].add(word)

        max_len = 0
        while len_words_map[max_len + 1]:
            max_len += 1

        @functools.lru_cache(None)
        def dfs(word):
            return not word or (word in len_words_map[len(word)] and dfs(word[:-1]))

        while max_len:
            for word in sorted(len_words_map[max_len]):
                if dfs(word):
                    return word
            max_len -= 1
        return ''





# trie
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

class Solution:
    def longestWord(self, words):
        trie = build_trie(words)
        res = ''
        stack = [(node, ch) for ch, node in trie.items() if '$' in node]
        while stack:
            node, acc = stack.pop()
            if len(acc) > len(res):
                res = acc
            elif len(acc) == len(res):
                res = min(res, acc)
            for next_ch, next_node in node.items():
                if next_ch != '$' and '$' in next_node:
                    stack.append((next_node, acc + next_ch))

        return res

