class Solution:
    def toGoatLatin(self, s):
        words = s.split()
        res = []

        for i, word in enumerate(words):
            if word[0] in 'aeiouAEIOU':
                res.append(word + 'ma' + 'a' * (i + 1))
            else:
                res.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))

        return ' '.join(res)