# dict1: key => freq
# dict2: freq => ordereddict3(key: value)
class LFUCache:
    def __init__(self, capacity):
        self.k_freq = collections.defaultdict(int) # init value with 0
        self.freq_nodes = collections.defaultdict(collections.OrderedDict) # init value with OrderedDict
        self.cap = capacity
        self.min = 1


    def get(self, key):
        if key not in self.k_freq:
            return -1
        freq = self.k_freq[key]
        value = self.freq_nodes[freq][key]
        self.update(key, value)
        return value


    def put(self, key, value):
        self.update(key, value)


    def update(self, key, value):
        freq = self.k_freq[key]
        self.k_freq[key] = freq + 1
        if freq:
            self.freq_nodes[freq].pop(key)
        self.freq_nodes[freq + 1][key] = value
        if len(self.k_freq) > self.cap:
            k, _ = self.freq_nodes[self.min].popitem(last=False)#FIFO
            self.k_freq.pop(k)
        if freq == self.min and not self.freq_nodes[freq]:
            self.min = freq + 1
        else:
            self.min = min(self.min, freq + 1)




# mine
class LFUCache:
    def __init__(self, capacity):
        self.k_freq = collections.defaultdict(int)
        self.freq_oDict = collections.defaultdict(collections.OrderedDict)
        self.capacity = capacity
        self.min_freq = 1


    def get(self, key):
        if key not in self.k_freq:
            return -1

        freq = self.k_freq[key]
        value = self.freq_oDict[freq][key]

        self.k_freq[key] = freq + 1
        self.freq_oDict[freq].pop(key)
        self.freq_oDict[freq+1][key] = value

        if freq == self.min_freq and not self.freq_oDict[freq]:
            self.min_freq += 1

        return value


    def put(self, key, value):
        if self.capacity == 0:
            return
        if key not in self.k_freq:
            if self.capacity == len(self.k_freq):
                k, _ = self.freq_oDict[self.min_freq].popitem(last=False)
                self.k_freq.pop(k)
            self.min_freq = 1
            # self.k_freq[key] = 1
            # self.freq_oDict[1][key] = value
            # return

        freq = self.k_freq[key]
        self.freq_oDict[freq][key] = value
        self.get(key)




# map: key-node
# map: linked list(freq) -> linked list(in same freq) or OrderedDict
# head -> FreqNode1 -> FreqNode2 ... -> FreqNodeN -> tail
#            |             |      |          |
#          node          node    nodes      node
#            |             |      |          |
#          node          node    nodes      node
