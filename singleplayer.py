from micropython import const
from random import randint

from game.core import CorePong
from game.interface import *

DIFFICULTY = const(0)


class SingleplayerPong(CorePong):
    def __init__(self, *args):
        super.__init__(*args)


pong = SingleplayerPong()
while True:
    pong.bottomPaddle.move(pong, getChange())
    render(pong)
