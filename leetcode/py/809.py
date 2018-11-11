'''
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
'''

class Solution:
    def expressiveWords(self, s, words):
        def parse(s): # str -> [(ch, cnt)
            stack = [('', 0)]
            for ch in s:
                prev_ch, cnt = stack.pop()
                if prev_ch == ch:
                    stack.append((ch, cnt + 1))
                else:
                    stack.append((prev_ch, cnt))
                    stack.append((ch, 1))
            return stack

        parsed_s = parse(s)

        def is_extension(parsed_word):
            if len(parsed_word) != len(parsed_s):
                return False
            for ((ch1, cnt1), (ch2, cnt2)) in zip(parsed_word, parsed_s):
                if ch1 != ch2 or cnt1 > cnt2 or (cnt1 != cnt2 and cnt2 < 3):
                    return False
            return True

        return sum(is_extension(parse(word)) for word in words)
