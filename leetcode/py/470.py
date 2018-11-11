# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


# 2.45
class Solution:
    def rand10(self):
        # 7 * (rand7() - 1) => 0 7 14 21 28 25 42
        # rand7() - 1       => 0 1 2 3 4 5 6
        # 1 - 49
        n = 7 * (rand7() - 1) + rand7() - 1
        while n >= 40:
            n = 7 * (rand7() - 1) + rand7() - 1

        # n : 0 - 39
        return n % 10 + 1
