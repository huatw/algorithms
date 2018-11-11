class Logger:
    def __init__(self):
        self.msg_time_map = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.msg_time_map or timestamp - self.msg_time_map[message] >= 10:
            self.msg_time_map[message] = timestamp
            return True
        return False