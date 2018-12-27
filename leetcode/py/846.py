class Solution:
    def isNStraightHand(self, hand, W):
        num_cnt_map = collections.Counter(hand)

        while num_cnt_map:
            num = min(num_cnt_map.keys())
            cnt = num_cnt_map[num]
            for n in range(num, num + W):
                num_cnt_map[n] -= cnt
                if num_cnt_map[n] < 0:
                    return False
                if num_cnt_map[n] == 0:
                    num_cnt_map.pop(n)

        return True