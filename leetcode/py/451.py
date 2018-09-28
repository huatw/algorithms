class Solution:
    def frequencySort(self, s):
        idx_ch_map = collections.defaultdict(list)
        ch_freq_map = collections.Counter(s)

        for ch, times in ch_freq_map.items():
            idx_ch_map[times].append(ch * times)

        sorted_chs = [chs for i in reversed(range(len(s) + 1)) for chs in idx_ch_map[i]]
        return ''.join(sorted_chs)


class Solution:
    def frequencySort(self, s):
        ch_freq_map = collections.Counter(s)

        arr = sorted(ch_freq_map.items(), reverse = True, key = lambda item: item[1])

        return ''.join([ch * times for ch, times in arr])


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
