class PhoneDirectory:
    def __init__(self, max_num):
        self.num_set = set(i for i in range(max_num))

    def get(self):
        if self.num_set:
            return self.num_set.pop()
        return -1

    def check(self, num):
        return num in self.num_set

    def release(self, num):
        self.num_set.add(num)