from microbit import *
import random

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

bottomPadX = 1
topPadX = 1

ballX = 2
ballY = 2

ballDirX = (random.choice([-1, 1]))
ballDirY = (random.choice([-1, 1]))
# ballDirX = -1
# ballDirY = -1


def render():  # render all the dots and wait so that they are visible
    display.clear()
    display.set_pixel(topPadX, 0, 5)
    display.set_pixel((topPadX-1), 0, 5)
    display.set_pixel(bottomPadX, 4, 5)
    display.set_pixel((bottomPadX-1), 4, 5)
    display.set_pixel(ballX, ballY, 9)
    return


def transferPresses():  # update the players paddle location
    global bottomPadX
    bottomPadX = bottomPadX+button_b.get_presses()
    bottomPadX = bottomPadX-button_a.get_presses()
    if bottomPadX < 1:
        bottomPadX = 1
    elif bottomPadX > 4:
        bottomPadX = 4
    return


def controlAI():  # control the top paddle
    global topPadX
    if ballX < topPadX-1:
        topPadX = topPadX-1
    elif ballX > topPadX:
        topPadX = topPadX+1


def updatePhysics():  # main game mechanics
    global side
    global ballX
    global ballY
    global ballDirX
    global ballDirY
    if ballY == 2:  # control most of the ball's movement
        ballX = ballX + ballDirX
        ballY = ballY + ballDirY
    elif ballY == 1 or ballY == 3:
        if ballY == 1:
            if topPadX == ballX:
                ballDirX = 1
                ballDirY = 1
            elif topPadX-1 == ballX:
                ballDirX = -1
                ballDirY = 1
        else:
            if bottomPadX == ballX:
                ballDirX = 1
                ballDirY = -1
            elif bottomPadX-1 == ballX:
                ballDirX = -1
                ballDirY = -1
        ballX = ballX + ballDirX
        ballY = ballY + ballDirY
    else:
        ballX = ballX + ballDirX
        ballY = ballY + ballDirY
    if ballX <= 0 or ballX >= 4:  # bounce off sides
        ballDirX = ballDirX * -1
    if ballY <= 0:  # make sure the ball hasn't hit one of the goals
        return 1
    elif ballY >= 4:
        return 2
    else:
        return 0


def doStuff():  # does everything other then rendering
    global side
    transferPresses()
    controlAI()
    # updatePhysics()
    side = updatePhysics()
    # display.scroll(str(ballX)+", "+str(ballY)


render()
sleep(500)
while True:  # main loop
    doStuff()
    render()
    if side != 0:
        break
    sleep(500)
if side == 1:  # show smiley face if the ball hit the top
    display.show(happyFace)
elif side == 2:  # show sad face if the ball hit the bottom
    display.show(sadFace)
while True:  # end: won or lost
    display.set_pixel(ballX, ballY, 9)
    sleep(500)
    display.set_pixel(ballX, ballY, 0)
    sleep(500)
