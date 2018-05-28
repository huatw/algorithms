# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):
        st, start, end, res = set(), 0, 0, -1

        while end < len(s):
            while s[end] in st:
                st.remove(s[start])
                start += 1
            if end - start > res:
                res = end - start
            st.add(s[end])
            end += 1

        return res + 1




# map
class Solution:
    def lengthOfLongestSubstring(self, s):
        map, start, end, res = {}, 0, 0, -1

        while end < len(s):
            if s[end] in map and map[s[end]] >= start:
                start = map[s[end]] + 1
            if end - start > res:
                res = end - start
            map[s[end]] = end
            end += 1

        return res + 1




# refact
class Solution:
    def lengthOfLongestSubstring(self, s):
        map, start, res = {}, 0, -1

        for i, ch in enumerate(s):
            if ch in map and map[ch] >= start:
                start = map[ch] + 1
            if i - start > res:
                res = i - start
            map[ch] = i

        return res + 1



