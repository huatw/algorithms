# Time:  O(n^2 * n!)
# Space: O(n^2)
class TrieNode:
    def __init__(self, words = []):
        self.indices = []
        self.children = {}
        for i in range(len(words)):
            self.insert(words, i)

    def insert(self, words, i):
        cur = self
        for c in words[i]:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.indices.append(i)


class Solution:
    def wordSquares(self, words):
        result = []
        trie = TrieNode(words)
        curr = []
        for word in words:
            curr.append(word)
            self.dfs(words, trie, curr, result)
            curr.pop()

        return result

    def dfs(self, words, trie, curr, result):
        if len(curr) >= len(words[0]):
            result.append(list(curr))
            return

        node = trie
        for s in curr:
            if s[len(curr)] not in node.children:
                return
            node = node.children[s[len(curr)]]

        for i in node.indices:
            curr.append(words[i])
            self.dfs(words, trie, curr, result)
            curr.pop()