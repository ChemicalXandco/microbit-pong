import random


class XY:
    def __init__(self, x, y):
        self.coordinates = x, y

    @property
    def coordinates(self):
        return (x, y)

    @coordinates.setter
    def coordinates(self, coordinates):
        self.x, self.y = coordinates

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

    @property
    def boundingBox(self):
        otherXY = XY(self.coordinates)
        otherXY.applyDelta(1, 0)
        return (
            self.coordinates,
            otherXY.coordinates
        )


class CorePong(XY)
    def __init__(self, x=5, y=5):
        super().__init__(self, x, y)

        self.ball = Ball(2, 2)

        self.topPaddle = Paddle(2, 0)
        self.bottomPaddle = Paddle(1, 4)
