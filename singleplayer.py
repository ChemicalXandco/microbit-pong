from microbit import sleep
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


def getAIChange():
    if pong.topPaddle.x < pong.ball.x:
        return 1
    elif pong.topPaddle.x > pong.ball.x:
        return -1
    return 0


pong = SingleplayerPong()
while True:
    pong.topPaddle.move(pong, getAIChange())
    pong.bottomPaddle.move(pong, getChange())
    pong.ball.move(pong)
    render(pong)
    sleep(1000)
