from core import CorePong
from multiplayer import HostBall, HostPaddle, ClientPaddle
from interface import *

# value from 0 - 100, 100 is impossible
DIFFICULTY = const(90)

START_SPEED = const(1000)
MIN_SPEED = const(100)
SPEED_CHANGE_RATE = const(5)


class HostPong(CorePong):
    def __init__(self, *args):
        super().__init__(*args)

        self.ball = HostBall(2, 2)

        self.topPaddle = ClientPaddle(2, 0)
        self.bottomPaddle = HostPaddle(1, 4)


pong = HostPong()
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
