class Solution:
    def plusOne(self, digits):
        tenth = 1
        for i, digit in reversed(list(enumerate(digits))):
            tenth, digits[i] = divmod(digit + tenth, 10)
            if tenth == 0:
                break

        if tenth == 0:
            return digits

        return [tenth, *digits]