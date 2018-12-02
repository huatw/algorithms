class Solution:
    def addBoldTag(self, s, words):
        itvs = []
        for i in range(len(s)):
            sub_s = s[i:]
            for word in words:
                if sub_s.startswith(word):
                    itvs.append((i, i + len(word)))

        if not itvs:
            return s

        merged_itvs = []
        for (start, end) in sorted(itvs):
            if not merged_itvs or start > merged_itvs[-1][1]:
                merged_itvs.append([start, end])
            else:
                merged_itvs[-1][1] = max(merged_itvs[-1][1], end)

        res = s[:merged_itvs[0][0]]
        for i, (start, end) in enumerate(merged_itvs):
            res += '<b>' + s[start:end] + '</b>'
            if i == len(merged_itvs) - 1:
                res += s[end:]
            else:
                res += s[end:merged_itvs[i + 1][0]]

        return ''.join(res)




class Solution:
    def addBoldTag(self, s, words):
        N = len(s)
        mask = [False] * N
        for i in range(N):
            prefix_s = s[i:]
            for word in words:
                if prefix_s.startswith(word):
                    for j in range(i, min(i + len(word), N)):
                        mask[j] = True
        res = []
        isbold = False
        for masked, ch in zip(mask, s):
            if isbold and not masked:
                isbold = False
                res.append('</b>')
            if not bold and masked:
                isbold = True
                res.append('<b>')
            res.append(ch)
        if isbold:
            res.append('</b>')
        return ''.join(res)

        # res = []
        # for isbold, sub_s in itertools.groupby(zip(s, mask), key=lambda z: z[1]):
        #     if isbold:
        #         res.append("<b>")
        #     res.append("".join(z[0] for z in sub_s))
        #     if isbold:
        #         res.append("</b>")
        # return "".join(res)
