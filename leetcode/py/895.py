# follow up
class FreqStack:
    def __init__(self):
        self.freq_nums_map = collections.defaultdict(list)
        self.num_freq_map = collections.defaultdict(int)
        self.max_freq_stack = [0]

    def push(self, num, freq = 1):
        self.num_freq_map[num] += freq
        self.freq_nums_map[self.num_freq_map[num]].append((num, freq))
        if self.num_freq_map[num] > self.max_freq_stack[-1]:
            self.max_freq_stack.append(self.num_freq_map[num])

    def pop(self):
        num, freq = self.freq_nums_map[self.max_freq_stack[-1]].pop()
        self.num_freq_map[num] -= freq
        if not self.freq_nums_map[self.max_freq_stack[-1]]:
            self.max_freq_stack.pop()
        return num


class FreqStack:
    def __init__(self):
        self.num_freq_map = collections.defaultdict(int)
        self.freq_nums_map = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, num):
        self.num_freq_map[num] += 1
        if self.num_freq_map[num] > self.max_freq:
            self.max_freq = self.num_freq_map[num]
        self.freq_nums_map[self.num_freq_map[num]].append(num)

    def pop(self):
        max_freq_nums = self.freq_nums_map[self.max_freq]
        num = max_freq_nums.pop()
        if not max_freq_nums:
            self.max_freq -= 1
        self.num_freq_map[num] -= 1
        return num
