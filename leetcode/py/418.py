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
        cnt = 0

        for _ in range(rows):
            cnt += cols
            while s[cnt % L] != ' ':
                cnt -= 1
            cnt += 1

        return cnt // L
