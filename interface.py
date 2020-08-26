from microbit import *

sadFace = Image("00000:"
                "09090:"
                "09990:"
                "90009:"
                "00000")
happyFace = Image("00000:"
                  "09090:"
                  "90009:"
                  "09990:"
                  "00000")

def renderPaddle(paddle):
    for coordinates in paddle.getBoundingBox():
        display.set_pixel(coordinates[0], coordinates[1], 5)

def render(pong):
    display.clear()
    display.set_pixel(pong.ball.x, pong.ball.y, 9)
    renderPaddle(pong.topPaddle)
    renderPaddle(pong.bottomPaddle)

def getChange():
    change = button_b.get_presses()
    change -= button_a.get_presses()
    return change
