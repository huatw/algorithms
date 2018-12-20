class Codec:
    BASE_URL = 'http://tinyurl.com/'
    STR = string.ascii_letters + string.digits

    def __init__(self):
        self.short_long_map = {}
        self.long_short_map = {}

    def encode(self, long_url):
        if long_url not in self.long_short_map:
            short_url = BASE_URL + ''.join(random.choice(STR) for _ in range(6))
            self.long_short_map[long_url] = short_url
            self.short_url[short_url] = long_url
        return self.long_short_map[long_url]

    def decode(self, short_url):
        if short_url in self.short_long_map:
            return self.short_long_map[short_url]
