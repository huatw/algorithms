class Solution:
    def fullJustify(self, words, MAX_WIDTH):
        will_overflow = lambda text_len, space_len: text_len + space_len > MAX_WIDTH
        def calc_line(line_words, line_width):
            nspaces = len(line_words) - 1 if len(line_words) > 1 else 1
            for i in range(MAX_WIDTH - line_width):
                line_words[i % nspaces] += ' '
            return ''.join(line_words)

        res = []
        line_words, line_width = [], 0

        for word in words:
            # check if add word will overflow
            if will_overflow(len(word) + line_width, len(line_words)):
                # calc current line
                res.append(calc_line(line_words, line_width))
                # reset
                line_words, line_width = [], 0
            line_words.append(word)
            line_width += len(word)

        return res + [' '.join(line_words).ljust(MAX_WIDTH)]


class Solution:
    def fullJustify(self, words, MAX_WIDTH):
        will_overflow = lambda text_len, space_len: text_len + space_len > MAX_WIDTH

        def calc_line(word, line_words, line_width):
            if not will_overflow(line_width + 2, len(line_words)):
                idx = MAX_WIDTH - len(line_words) - line_width - 1
                left_word, right_word = word[:idx], word[idx:]
                return right_word, ' '.join(line_words + [left_word + '-'])
            else:
                nspaces = len(line_words) - 1 if len(line_words) > 1 else 1
                for i in range(MAX_WIDTH - line_width):
                    line_words[i % nspaces] += ' '
                return word, ''.join(line_words)

        res = []
        line_words, line_width = [], 0

        for word in words:
            # check if add word will overflow
            while will_overflow(len(word) + line_width, len(line_words)):
                # calc current line
                word, line = calc_line(word, line_words, line_width)
                res.append(line)
                # reset
                line_words, line_width = [], 0
            line_words.append(word)
            line_width += len(word)

        return res + [' '.join(line_words).ljust(MAX_WIDTH)]
