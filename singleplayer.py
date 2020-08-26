from micropython import const
from random import randint

from core import *
from interface import *

DIFFICULTY = const(0)


class SingleplayerPong(CorePong):
    def __init__(self, *args):
        super().__init__(*args)

        self.ball = Ball(2, 2)

        self.topPaddle = Paddle(2, 0)
        self.bottomPaddle = Paddle(1, 4)


pong = SingleplayerPong()
while True:
    pong.bottomPaddle.move(pong, getChange())
    render(pong)
