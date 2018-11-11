import heapq, collections

class Solution:
    def alienOrder(self, words):
        self.second_first = collections.defaultdict(int)
        self.first_second = collections.defaultdict(list)
        res = ''
        total = 0
        word_set = set()
        for word in words: # avg_len(word) x len(words)
            for ch in word:
                if ch not in word_set:
                    self.second_first[ch] = 0
                    total += 1
                    word_set.add(ch)

        self.build_graph(words) # avg_len(word) x len(words)

        hq = []
        for (k, v) in self.second_first.items():
            if v == 0:
                heapq.heappush(hq, k)

        while hq:
            first = heapq.heappop(hq) # V E
            res += first
            for second in self.first_second[first]:
                self.second_first[second] -= 1
                if self.second_first[second] == 0:
                    heapq.heappush(hq, second)

        return res if total == len(res) else ''

    # avg_len(word) x len(words)
    def build_graph(self, words):
        if len(words) <= 1:
            return

        next_level = []
        state = ('', [])
        for word in words:
            if state[0] != word[0]:
                if state[0]:
                    self.second_first[word[0]] += 1
                    self.first_second[state[0]].append(word[0])
                next_level.append(state[1])
                state = (word[0], [])
            if word[1:]:
                state[1].append(word[1:])
        next_level.append(state[1])

        for level in next_level:
            self.build_graph(level)





class Solution:
    def alienOrder(self, words):
        self.ch_graph = {}
        res = ''

        total = 0
        for word in words:
            for ch in word:
                if ch not in self.ch_graph:
                    self.ch_graph[ch] = set()
                    total += 1
        self.build_graph(words)

        hq = []
        for (k, v) in self.ch_graph.items():
            if not v:
                heapq.heappush(hq, k)

        # 26 * 26 * log(26)
        while hq:
            dep = heapq.heappop(hq)
            res += dep

            for (k, v) in self.ch_graph.items():
                if len(v) == 1 and dep in v:
                    heapq.heappush(hq, k)
                v.discard(dep)

        return res if total == len(res) else ''


    # time comp: avg_len(word) x len(words)
    def build_graph(self, words):
        if len(words) <= 1:
            return

        next_level = []
        state = ('', [])

        for word in words:
            # change state
            if state[0] != word[0]:
                if state[0]:
                    self.ch_graph[word[0]].add(state[0])
                next_level.append(state[1])
                state = (word[0], [])
            if word[1:]:
                state[1].append(word[1:])

        next_level.append(state[1])

        for level in next_level:
            self.build_graph(level)


