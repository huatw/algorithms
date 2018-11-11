import collections

class Solution:
    def can_form_palindromes(self, ch_cnt_map):
        has_odd = False
        self.single_ch = ''
        for (ch, cnt) in ch_cnt_map.items():
            if cnt % 2 != 0:
                if not has_odd:
                    self.single_ch = ch
                    has_odd = True
                else:
                    return False

        return True

    def generatePalindromes(self, s):
        ch_cnt_map = collections.Counter(s)
        if not self.can_form_palindromes(ch_cnt_map):
            return []

        res = []
        def dfs(ch_cnt_map, acc_str, rest_n):
            if rest_n == 0:
                res.append(acc_str + self.single_ch + acc_str[::-1])
                return

            for (ch, cnt) in ch_cnt_map.items():
                if cnt >= 2:
                    ch_cnt_map[ch] -= 2
                    dfs(ch_cnt_map, acc_str + ch, rest_n - 1)
                    ch_cnt_map[ch] += 2

        dfs(ch_cnt_map, '', len(s) // 2)

        return res
