'''
Input: S = "aab"
Output: "aba"

Input: S = "aaab"
Output: ""
'''
class Solution:
    def reorganizeString(self, S):
        ch_cnt_map = collections.Counter(S)
        hq = [(-cnt, ch) for ch, cnt in ch_cnt_map.items()]
        heapq.heapify(hq)

        lastpop = None
        res = []
        while hq:
            neg_cnt, ch = heapq.heappop(hq)
            res.append(ch)
            if lastpop:
                heapq.heappush(hq, lastpop)
            lastpop = (neg_cnt + 1, ch) if neg_cnt + 1 != 0 else None

        return ''.join(res) if len(res) == len(S) else ''



'''
Input: S = "aab"
Output: "aba"

Input: S = "aaab"
Output: ""
'''
class Solution:
    def reorganizeString(self, S):
        ch_cnt_map = collections.Counter(S)

        hq = [(-cnt, ch) for ch, cnt in ch_cnt_map.items()]
        heapq.heapify(hq)
        res = ''
        lastpop = None

        while hq:
            neg_cnt, ch = heapq.heappop(hq)
            res += ch
            if lastpop and lastpop[0]:
                heapq.heappush(hq, lastpop)

            lastpop = (neg_cnt + 1, ch)

        return res if len(res) == len(S) else ''

