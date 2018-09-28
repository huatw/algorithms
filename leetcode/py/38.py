class Solution:
    def countAndSay(self, n):
        res = '1'

        for i in range(1, n):
            cur_res, cur_n, cnt = '', res[0], 0

            for j, num in enumerate(res):
                if num == cur_n:
                    cnt += 1
                else:
                    cur_res += str(cnt) + cur_n
                    cur_n, cnt = num, 1

            res = cur_res + str(cnt) + cur_n

        return res
