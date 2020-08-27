from microbit import sleep
from micropython import const
from random import randint

from core import *
from interface import *

# value from 0 - 100, 100 is impossible
DIFFICULTY = const(90)

START_SPEED = const(1000)
MIN_SPEED = const(100)
SPEED_CHANGE_RATE = const(5)


class SingleplayerPong(CorePong):
    def __init__(self, *args):
        super().__init__(*args)

        self.ball = Ball(2, 2)

        self.topPaddle = Paddle(2, 0)
        self.bottomPaddle = Paddle(1, 4)


def getAIChange():
    ballX = pong.ball.x + pong.ball.direction.x
    if pong.topPaddle.x < ballX:
        return 1
    elif pong.topPaddle.x + 1 > ballX:
        return -1
    return 0


pong = SingleplayerPong()
speed = START_SPEED
while True:
    if randint(1, 100) <= DIFFICULTY:
        pong.topPaddle.move(pong, getAIChange())
    pong.bottomPaddle.move(pong, getChange())
    pong.ball.move(pong)
    render(pong)

    sleep(speed)
    speed -= SPEED_CHANGE_RATE * (speed / START_SPEED)
    if speed < MIN_SPEED:
        speed = MIN_SPEED

    winner = pong.getWinner()
    if winner:
        displayWinner(winner, 2)
        break
flashBall(pong.ball)
