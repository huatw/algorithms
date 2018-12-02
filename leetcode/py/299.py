class Solution:
    def getHint(self, secret, guess):
        chs_cnt_map = collections.defaultdict(int)
        chg_cnt_map = collections.defaultdict(int)
        bulls, cows = 0, 0
        for chs, chg in zip(secret, guess):
            if chs == chg:
                bulls += 1
            else:
                chs_cnt_map[chs] += 1
                chg_cnt_map[chg] += 1
        for chs, cnt in chs_cnt_map.items():
            cows += min(cnt, chg_cnt_map[chs])
        return str(bulls) + 'A' + str(cows) + 'B'




class Solution:
    def getHint(self, secret, guess):
        bulls, cows = 0, 0
        d = collections.defaultdict(int)
        for chs, chg in zip(secret, guess):
            if chs == chg:
                bulls += 1
            else:
                if d[chs] < 0:
                    cows += 1
                d[chs] += 1
                if d[chg] > 0:
                    cows += 1
                d[chg] -= 1
        return '{}A{}B'.format(bulls, cows)
