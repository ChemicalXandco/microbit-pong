from core import CorePong
from multiplayer import HostPaddle, ClientXY, ClientPaddle
from interface import *


class ClientPong(CorePong):
    def __init__(self, *args):
        super().__init__(*args)

        # we don't need to use the ball functions on the client
        self.ball = ClientXY(2, 2)

        self.topPaddle = ClientPaddle(2, 0)
        self.bottomPaddle = ClientPaddle(1, 4)
