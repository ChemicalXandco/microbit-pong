import random


class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def applyDelta(self, x, y):
        self.x += x
        self.y += y


class Ball(XY):
    def __init__(self, *args):
        super().__init__(*args)

        self.direction = XY(*[ random.choice([-1, 1]) for i in range(2) ])

    def move(self, pong):
        newX = self.x + self.direction.x
        if newX < 0 or newX > pong.x:
            self.direction.x *= -1

        for paddle in [pong.topPaddle, pong.bottomPaddle]:
            for i, coordinates in enumerate(paddle.getBoundingBox()):
                if self.x + self.direction.x == coordinates[0] and self.y + self.direction.y == coordinates[1]:
                    # bounce
                    self.direction.x = (i * 2) - 1
                    self.direction.y *= -1

        self.x += self.direction.x
        self.y += self.direction.y


class Paddle(XY):
    def __init__(self, *args):
        super().__init__(*args)

    def getBoundingBox(self):
        return [
            [self.x, self.y],
            [self.x+1, self.y]
        ]

    def move(self, pong, amount):
        self.x += amount
        if self.x < 0:
            self.x = 0
        elif self.x > pong.x - 1:
            self.x = pong.x - 1


class CorePong(XY):
    def __init__(self, x=4, y=4):
        super().__init__(x, y)
