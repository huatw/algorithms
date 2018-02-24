class Solution:
    def frequencySort(self, s):
        freq = collections.defaultdict(int)

        for ch in s:
            freq[ch] += 1

        arr = sorted(freq.items(), key=operator.itemgetter(1), reverse = True)

        return ''.join(ch * times for ch, times in arr)




class Solution:
    def frequencySort(self, s):
        return ''.join(ch * times for ch, times in collections.Counter(s).most_common())
