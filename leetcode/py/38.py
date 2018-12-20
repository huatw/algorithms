class Solution:
    def countAndSay(self, n):
        res = '1'

        for i in range(1, n):
            cur_cnt, cur_n, cur_res = '', '', ''
            for num in res:
                if num == cur_n:
                    cur_cnt += 1
                else:
                    cur_cnt, cur_n, cur_res = 1, num, cur_res + str(cur_cnt) + cur_n
            res = cur_res + str(cur_cnt) + cur_n

        return res

