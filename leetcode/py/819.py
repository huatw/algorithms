class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = re.split(r'\W+', paragraph.lower())
        banned_set = set(banned)
        word_dict = collections.defaultdict(int)
        max_count = 0
        res = ''

        for word in words:
            if word in banned_set:
                continue
            word_dict[word] += 1
            if word_dict[word] > max_count:
                max_count = word_dict[word]
                res = word

        return res
