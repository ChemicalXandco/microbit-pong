import random


class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __list__(self):
        return [self.x, self.y]

    def applyDelta(self, x, y):
        self.x += x
        self.y += y


class Ball(XY):
    def __init__(self, *args):
        super().__init__(*args)

        self.direction = XY(*[ random.choice([-1, 1]) for i in range(2) ])


class Paddle(XY):
    def __init__(self, *args):
        super().__init__(*args)

    def getBoundingBox(self):
        return [
            list(self),
            [self.x+1, self.y]
        ]

    def move(self, pong, amount):
        self.x += amount
        if self.x < 0:
            self.x = 0
        elif self.x > pong.x:
            self.x = pong.x


class CorePong(XY):
    def __init__(self, x=4, y=4):
        super().__init__(x, y)

        self.ball = Ball(2, 2)

        self.topPaddle = Paddle(2, 0)
        self.bottomPaddle = Paddle(1, 4)
