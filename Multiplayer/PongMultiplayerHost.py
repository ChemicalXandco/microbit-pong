from microbit import *
import random
import radio

sadFace = Image.SAD
happyFace = Image.HAPPY

bottomPadX = 1
topPadX = 1

ballX = 2
ballY = 2

ballDirX = -1
ballDirY = (random.choice([-1, 1]))


def clearRadio(): # clear message queue
    lastMessage = 'thing'
    while lastMessage != None:
        lastMessage = radio.receive()


def pingPong(): # sync microbits
    while True:
        radio.send('s')
        lastMessage = radio.receive()
        if lastMessage == 'r':
            break


def render():  # render all the dots and wait so that they are visible
    display.clear()
    display.set_pixel(topPadX, 0, 5)
    display.set_pixel((topPadX-1), 0, 5)
    display.set_pixel(bottomPadX, 4, 5)
    display.set_pixel((bottomPadX-1), 4, 5)
    display.set_pixel(ballX, ballY, 9)


def renderLoading(state):
    display.clear()
    brightness = 9
    for i in state:
        display.set_pixel(i['x'], i['y'], brightness)
        brightness -= 1


def transferPresses():  # update the players paddle location
    global bottomPadX
    bottomPadX = bottomPadX+button_b.get_presses()
    bottomPadX = bottomPadX-button_a.get_presses()
    if bottomPadX < 1:
        bottomPadX = 1
    elif bottomPadX > 4:
        bottomPadX = 4


def updatePaddle():  # send and receive data
    global topPadX
    timeAdded = 150
    while True:
        try:
            clearRadio()
            sleep(50)
            radio.send(str(bottomPadX))
            sleep(50)
            topPadX = int(radio.receive())
            radio.send('good')
            sleep(50)
            lastMessage = radio.receive()
            if lastMessage != 'good':
                raise TypeError('Communication failed.')
            break
        except TypeError:
            timeAdded += 150
            pingPong()
        except ValueError:
            timeAdded += 150
            pingPong()
    return timeAdded


def updatePhysics():  # main game mechanics
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


def updateBall():  # send and receive data
    timeAdded = 50
    while True:
        clearRadio()
        radio.send(str(ballX))
        radio.send(str(ballY))
        radio.send(str(side))
        sleep(50)
        while True:
            lastMessage = radio.receive()
            if (lastMessage == 'good') or (lastMessage == 'bad'):
                radio.receive()
                break
        if lastMessage != 'good':
            timeAdded += 50
            pingPong()
        else:
            break
    return timeAdded


def doStuff():  # does everything other then rendering
    global side
    totalTimeAdded = 0
    transferPresses()
    totalTimeAdded += updatePaddle()
    side = updatePhysics()
    totalTimeAdded += updateBall()
    return totalTimeAdded


radio.on()
loader = [{'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4}, {'x': 1, 'y': 4}, {'x': 2, 'y': 4}, {'x': 3, 'y': 4}, {'x': 4, 'y': 4}]
renderLoading(loader)
while True:
    for i in range(len(loader)):
        currentLoader = loader[i]
        if (currentLoader['x'] == 4) or (currentLoader['y'] == 4):
            if (currentLoader['x'] == 4) and (currentLoader['y'] < 4):
                currentLoader['y'] += 1
            elif (currentLoader['y'] == 4) and (currentLoader['x'] > 0):
                currentLoader['x'] -= 1
            elif (currentLoader['x'] == 0) and (currentLoader['y'] > 0):
                currentLoader['y'] -= 1
        else:
            if (currentLoader['x'] == 0) and (currentLoader['y'] > 0):
                currentLoader['y'] -= 1
            elif (currentLoader['y'] == 0) and (currentLoader['x'] < 4):
                currentLoader['x'] += 1
        loader[i] = currentLoader
    renderLoading(loader)
    lastMessage = radio.receive()
    if lastMessage == 'pong':
        break
    radio.send('ping')
    sleep(100)
currentTime = running_time()
lastMessage = radio.receive()
lastMessage = int(lastMessage)
radio.send(str(lastMessage+1000))
while True:
    if running_time() >= currentTime+1000:
        break
render()
sleep(500)
while True:  # main loop
    timeToWait = 500 - doStuff()
    if timeToWait < 0:
        timeToWait = 0
    render()
    if side != 0:
        break
    sleep(timeToWait)
    pingPong()
    clearRadio()
radio.off()
if side == 1:  # show smiley face if the ball hit the top
    display.show(happyFace)
elif side == 2:  # show sad face if the ball hit the bottom
    display.show(sadFace)
while True:  # end: won or lost
    display.set_pixel(ballX, ballY, 9)
    sleep(500)
    display.set_pixel(ballX, ballY, 0)
    sleep(500)
