class Solution:
    def groupStrings(self, strings):
        def encode(s):
            res = ''
            base = ord(s[0])
            for ch in s:
                val = ord(ch) - base
                if val < 0:
                    val += 26
                res += chr(val)
            return res

        encoded_strs_map = collections.defaultdict(list)

        for s in strings:
            encoded_strs_map[encode(s)].append(s)

        return [*encoded_strs_map.values()]

class Solution:
    def groupStrings(self, strings):
        encoded_str_map = collections.defaultdict(list)

        def encode_str(s):
            base_ord = ord(s[0])
            res = []
            for ch in s:
                v = ord(ch) - base_ord
                if v < 0:
                    v += 26
                res.append(str(v))
            return ' '.join(res)

        for s in strings:
            encoded_str_map[encode_str(s)].append(s)

        return list(encoded_str_map.values())

