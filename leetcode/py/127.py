class Solution:
    def ladderLength(self, begin_word, end_word, word_list):
        templeate_words_map = collections.defaultdict(list)
        def get_templates(word):
            for i in range((len(word))):
                yield word[:i] + '_' + word[i+1:]

        for word in word_list:
            for templeate in get_templates(word):
                templeate_words_map[templeate].append(word)

        level = [begin_word]
        step = 0
        seen = set()

        while level:
            step += 1
            next_level = []
            for word in level:
                if word == end_word:
                    return step
                for template in get_templates(word):
                    if template in seen:
                        continue
                    seen.add(template)
                    for next_word in templeate_words_map[template]:
                        if next_word not in seen:
                            next_level.append(next_word)

            level = next_level

        return 0


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_map = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                word_map[word[:i] + '_' + word[i+1:]].append(word)

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



