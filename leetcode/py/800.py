class Solution:
    def similarRGB(self, color):
        colors = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
        def get_cloest(s):
            return min(colors, key=lambda c: abs(int(s, 16) - int(c, 16)))

        res = [get_cloest(color[i:i+2]) for i in range(1, 7, 2)]
        return '#' + ''.join(res)
