class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_map = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i+1:]
                word_map[key].append(word)

        level = [beginWord]
        step = 0
        visited = set()

        while level:
            step += 1
            nextLevel = []
            for word in level:
                if word == endWord:
                    return step
                if word not in visited:
                    visited.add(word)
                    for i in range(len(word)):
                        key = word[:i] + '_' + word[i+1:]
                        if key not in visited:
                            visited.add(key)
                            if key in word_map:
                                nextLevel.extend(word_map[key])
            level = nextLevel
        return 0



