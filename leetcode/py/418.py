'''
'apple egg phone apple egg phone apple egg phone apple egg phone...
      ^
          ^
                ^
'''
class Solution:
    def wordsTyping(self, words, rows, cols):
        s = ' '.join(words) + ' '
        L = len(s)
        idx = 0

        for _ in range(rows):
            idx += cols
            while idx >= 0 and s[idx % L] != ' ':
                idx -= 1
            idx += 1
        return idx // L
