import radio

from game.core import *


class ClientXY(XY):
    def __init__(self, *args):
        super().__init__(*args)

    def sync(self):
        


class ClientBall(Ball, ClientXY):
    def __init__(self, *args):
        super().__init__(*args)


class ClientPaddle(Paddle, ClientXY):
    def __init__(self, *args):
        super().__init__(*args)


class ClientPong(CorePong):
    def __init__(self, *args):
        super.__init__(*args)

        self.ball = ClientBall(2, 2)

        self.topPaddle = ClientPaddle(2, 0)
        self.bottomPaddle = ClientPaddle(1, 4)
