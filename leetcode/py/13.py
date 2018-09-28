class Solution:
    def romanToInt(self, s):
        sym_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        for i, ch in enumerate(s[:-1]):
            if sym_val[ch] >= sym_val[s[i + 1]]:
                total += sym_val[ch]
            else:
                total -= sym_val[ch]

        return total + sym_val[s[-1]]
