class FreqWord:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        return self.freq < other.freq or (self.freq == other.freq and other.word < self.word)


class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = []

        for word, freq in count.items():
            heapq.heappush(heap, FreqWord(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap).word for _ in range(k)][::-1]