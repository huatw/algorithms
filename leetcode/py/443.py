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