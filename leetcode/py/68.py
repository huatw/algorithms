'''
[aa, bb, cc]
'aa bb cc ?'
'''
class Solution:
    def fullJustify(self, words, max_width):
        def will_overflow(cur_words, cur_len, word):
            return len(cur_words) + cur_len + len(word) > max_width

        def gen_line(cur_words, cur_len):
            nspaces = len(cur_words) - 1 if len(cur_words) > 1 else 1
            for i in range(max_width - cur_len):
                cur_words[i % nspaces] += ' '
            return ''.join(cur_words)

        res = []
        cur_len, cur_words = 0, []

        for word in words:
            if will_overflow(cur_words, cur_len, word):
                res.append(gen_line(cur_words, cur_len))
                cur_len, cur_words = 0, []
            cur_words.append(word)
            cur_len += len(word)

        return res + [' '.join(cur_words).ljust(max_width)]


比如第一行最后面本来放不下, 现在可以把下一个单词拆分, 要求是至少俩字符, 并要加一个-连接符。
# split word if word
class Solution:
    def fullJustify(self, words, max_width):
        def will_overflow(cur_words, cur_len, word):
            return len(cur_words) + cur_len + len(word) > max_width

        def gen_line(cur_words, cur_len, word):
            if len(word) == 1:
                nspaces = len(cur_words) - 1 if len(cur_words) > 1 else 1
                for i in range(max_width - cur_len):
                    cur_words[i % nspaces] += ' '
                return word, ''.join(cur_words)
            else:
                idx = max_width - cur_len - len(cur_words) - 1
                left, right = word[:idx], word[idx:]
                return right, ' '.join(cur_words + [left + '-'])

        res = []
        cur_len, cur_words = 0, []

        for word in words:
            if will_overflow(cur_words, cur_len, word):
                word, line = gen_line(cur_words, cur_len, word)
                res.append(line)
                cur_len, cur_words = 0, []
            cur_words.append(word)
            cur_len += len(word)

        return res + [' '.join(cur_words).ljust(max_width)]
