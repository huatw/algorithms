class Solution:
    def compress(self, chars):
        if not chars:
            return 0

        lo, hi = 0, 0
        while hi < len(chars):
            cur_ch = chars[hi]
            cnt = 0
            while hi < len(chars) and chars[hi] == cur_ch:
                hi += 1
                cnt += 1
            chars[lo] = chars[hi - 1]
            lo += 1
            if cnt > 1:
                for ch in str(cnt):
                    chars[lo] = ch
                    lo += 1
        return lo



class Solution:
    def compress(self, chars):
        if not chars:
            return 0

        lo = 0
        cur_ch = chars[0]
        cnt = 0

        for hi, ch in enumerate(chars):
            if ch == cur_ch:
                cnt += 1
                continue
            chars[lo] = cur_ch
            lo += 1
            if cnt > 1:
                for digit in str(cnt):
                    chars[lo] = digit
                    lo += 1
            cnt = 1
            cur_ch = ch

        chars[lo] = cur_ch
        lo += 1
        if cnt > 1:
            for digit in str(cnt):
                chars[lo] = digit
                lo += 1

        return lo


'''
aaabbbccc
'''


class Solution:
    def compress(self, chars):
        idx = 0
        prev_ch, cnt = None, 0

        def update():
            nonlocal idx
            if prev_ch:
                chars[idx] = prev_ch
                idx += 1
                if cnt > 1:
                    for c in str(cnt):
                        chars[idx] = c
                        idx += 1

        for ch in chars:
            if ch != prev_ch:
                update()
                prev_ch, cnt = ch, 1
            else:
                cnt += 1

        update()
        return idx