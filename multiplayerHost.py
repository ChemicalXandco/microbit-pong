import radio

from core import *


class HostXY(XY):
    def __init__(self, *args):
        super().__init__(*args)

    def sync(self):
        


class HostBall(Ball, HostXY):
    def __init__(self, *args):
        super().__init__(*args)


class HostPaddle(Paddle, HostXY):
    def __init__(self, *args):
        super().__init__(*args)


class HostPong(CorePong):
    def __init__(self, *args):
        super().__init__(*args)

        self.ball = HostBall(2, 2)

        self.topPaddle = HostPaddle(2, 0)
        self.bottomPaddle = HostPaddle(1, 4)
