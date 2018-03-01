# DP IMPORTANT
class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        res = [False] * (len(s)+1)
        res[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordSet and res[j]:
                    res[i] = True
                    break

        return res[-1]

# Tire tree with cache
class Solution(object):
    def wordBreak(self, s, wordDict):
        tire = {}

        for word in wordDict:
            level = tire

            for ch in word:
                if ch not in level:
                    level[ch] = {}
                level = level[ch]

            level['$'] = True

        cache = {}

        def search(start, end):
            word = s[start:end]
            if word in cache:
                return cache[word]

            level = tire

            for i in range(start, end):
                if '$' in level and search(i, end):
                    cache[word] = True
                    return True
                if s[i] not in level:
                    cache[word] = False
                    return False
                level = level[s[i]]

            cache[word] = '$' in level
            return '$' in level


        return search(0, len(s))


