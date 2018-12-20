class ValidWordAbbr:
    def __init__(self, dictionary):
        self.abbr_words_map = collections.defaultdict(set)
        for word in dictionary:
            if word:
                abbr = word[0] + str(len(word)) + word[-1]
                self.abbr_words_map[abbr].add(word)

    def isUnique(self, word):
        if not word:
            return True
        abbr = word[0] + str(len(word)) + word[-1]
        return abbr not in self.abbr_words_map or self.abbr_words_map[abbr] == set([word])
