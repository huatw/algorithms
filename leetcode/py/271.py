class Codec:
    def encode(self, strs):
        res = []
        for s in strs:
            res.append(str(len(s)) + ' ' + s)
        return ''.join(res)

    def decode(self, s):
        res = []
        token = ['', '', True] # acc, cnt, number
        for ch in s:
            if token[2]:
                if ch == ' ':
                    token[2] = False
                    token[1] = int(token[1])
                else:
                    token[1] += ch
            else: # string
                token[0] += ch
                token[1] -= 1
                if token[1] == 0:
                    token[2] = True
                    res.append(token[0])
                    token[0] = ''
                    token[1] = ''
        return res
