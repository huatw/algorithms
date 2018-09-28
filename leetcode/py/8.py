class Solution:
    def myAtoi(self, str):
        str = str.strip()
        if not str:
            return 0

        res = 0
        start = 0
        flag = 1
        if str[0] == '+':
            start = 1
        elif str[0] == '-':
            flag = -1
            start = 1

        for i in range(start, len(str)):
            if not str[i].isdigit():
                break
            res = res * 10 + int(str[i])
            if res > 2147483647:
                return 2147483647 if flag == 1 else -2147483648

        return res * flag