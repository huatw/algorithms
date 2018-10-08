class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        for i in range(len(words)):
            for j in range(i, len(words[i])):
                if words[i][j] != words[j][i]:
                    return False

        return True
