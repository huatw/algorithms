class SnakeGame:
    DIRECTIONS = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def __init__(self, width, height, food):
        self.positions = collections.deque([[0, 0]])
        self.width, self.height = width, height
        self.food = collections.deque(food)

    def will_die(self, x, y):
        if [x, y] in self.positions or not (self.height > x >= 0 and self.width > y >= 0):
            return True

    def move(self, direction):
        new_position = list(map(sum, zip(SnakeGame.DIRECTIONS[direction], self.positions[0])))
        if self.food and self.food[0] == new_position:
            self.food.popleft()
        else:
            self.positions.pop()
            if self.will_die(*new_position):
                return -1
        self.positions.appendleft(new_position)
        return len(self.positions) - 1
