'''
Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
[
    "ball",
    "asee",
    "let",
    "lep"
]
'''
class Solution:
    def validWordSquare(self, words):
        for i, word in enumerate(words):
            for j, ch in enumerate(word):
                if j >= len(words) or i >= len(words[j]) or ch != words[j][i]:
                    return False
        return True
