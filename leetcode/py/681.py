class Solution:
    def nextClosestTime(self, time):
        now = 60 * int(time[:2]) + int(time[3:])
        digit_set = {int(x) for x in time if x != ':'}
        while True:
            now = (now + 1) % (24 * 60)
            if all(digit in digit_set
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))


class Solution:
    def nextClosestTime(self, time):
        START = 60 * int(time[:2]) + int(time[3:])
        digit_set = {int(x) for x in time if x != ':'}
        min_time, min_elapsed = START, 24 * 60

        for h1, h2, m1, m2 in itertools.product(digit_set, repeat = 4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                elapsed = (cur - START) % (24 * 60)
                if 0 < elapsed < min_elapsed:
                    min_time, min_elapsed = cur, elapsed

        return "{:02d}:{:02d}".format(*divmod(min_time, 60))