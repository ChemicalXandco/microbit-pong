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
    for coordinates in paddle.boundingBox:
        display.set_pixel(*coordinates, 5)

def render(pong):
    display.clear()
    display.set_pixel(*pong.ball.coordinates, 9)
    renderPaddle(pong.topPaddle)
    renderPaddle(pong.bottomPaddle)