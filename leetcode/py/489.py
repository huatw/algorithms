#class Robot:
#    def move(self):
#    def turnLeft(self):
#    def turnRight(self):
#    def clean(self):
# The initial direction of the robot will be facing up.
class Solution:
    def cleanRoom(self, robot):
        seen = set()
        DIRECTIONS = [(0, 0, -1), (1, 1, 0), (2, 0, 1), (3, -1, 0)] # clockwise, up
        def try_move():
            return robot.move()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()

        def turn_next_direction():
            robot.turnRight()

        def dfs(x, y, offset):
            seen.add((x, y))
            robot.clean()
            for i, dx, dy in DIRECTIONS[offset:] + DIRECTIONS[:offset]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in seen and try_move():
                    dfs(nx, ny, i)
                    go_back()
                else:
                    turn_next_direction()

        dfs(0, 0, 0)

