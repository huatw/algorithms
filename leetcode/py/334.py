class Solution:
    def increasingTriplet(self, nums):
        one, two = float('inf'), float('inf')

        for num in nums:
            if num > two:
                return True
            if num > one:
                two = min(two, num)
            one = min(one, num)

        return False