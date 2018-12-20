class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        def normalize(chs):
            ch_idx_map = {}
            res = []
            for i, ch in enumerate(chs):
                if ch not in ch_idx_map:
                    ch_idx_map[ch] = i
                res.append(ch_idx_map[ch])
            return tuple(res)

        return normalize(s) == normalize(t)


# len(s) + len(t)
class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_t_map, t_s_map = {}, {}

        for chs, cht in zip(s, t):
            if chs not in s_t_map and cht not in t_s_map:
                s_t_map[chs] = cht
                t_s_map[cht] = chs
            elif chs in s_t_map and chs in s_t_map:
                if s_t_map[chs] != cht or t_s_map[cht] != chs:
                    return False
            else:
                return False

        return True

class Solution:
    def isIsomorphic(self, s, t):
        return [*map(s.find, s)] == [*map(t.find, t)]
