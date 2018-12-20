class Solution:
    def expressiveWords(self, target, words):
        def parse(word):
            stack = []
            token, cnt = '', 0
            for ch in word:
                if token == ch:
                    cnt += 1
                else:
                    stack.append((token, cnt))
                    token, cnt = ch, 1
            stack.append((token, cnt))
            return stack

        def is_extension(t, word):
            if len(t) != len(word):
                return False
            return all(ch_t == ch_w and (cnt_t == cnt_w or (cnt_t > cnt_w and cnt_t >= 3)) \
                for (ch_t, cnt_t), (ch_w, cnt_w) in zip(t, word))

        target = parse(target)
        return sum(is_extension(target, parse(word)) for word in words)
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

        def is_extension(parsed_word, parsed_s):
            if len(parsed_word) != len(parsed_s):
                return False
            for ((ch1, cnt1), (ch2, cnt2)) in zip(parsed_word, parsed_s):
                if ch1 != ch2 or cnt1 > cnt2 or (cnt1 != cnt2 and cnt2 < 3):
                    return False
            return True

        return sum(is_extension(parse(word), parsed_s) for word in words)
