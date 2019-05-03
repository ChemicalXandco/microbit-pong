from microbit import *
import radio

sadFace = Image.SAD
happyFace = Image.HAPPY

bottomPadX = 1
topPadX = 1

ballX = 2
ballY = 2


def render():  # render all the dots and wait so that they are visible
    display.clear()
    display.set_pixel(topPadX, 0, 5)
    display.set_pixel((topPadX-1), 0, 5)
    display.set_pixel(bottomPadX, 4, 5)
    display.set_pixel((bottomPadX-1), 4, 5)
    display.set_pixel(ballX, ballY, 9)


def transferPresses():  # update the players paddle location
    global topPadX
    topPadX = topPadX+button_b.get_presses()
    topPadX = topPadX-button_a.get_presses()
    if topPadX < 1:
        topPadX = 1
    elif topPadX > 4:
        topPadX = 4


def updatePaddle():  # send and receive data
    global bottomPadX
    timeAdded = 100
    while True:
        try:
            radio.send(str(topPadX))
            sleep(50)
            bottomPadX = int(radio.receive())
            radio.send('good')
            sleep(50)
            lastMessage = radio.receive()
            if lastMessage != 'good':
                raise TypeError('Communication failed.')
            break
        except TypeError:
            timeAdded += 100
            while True:
                lastMessage = radio.receive()
                if lastMessage == 'ping':
                    break
            radio.send('pong')
    return timeAdded


def updateBall():  # send and receive data
    global ballX
    global ballY
    global side
    timeAdded = 50
    while True:
        try:
            sleep(50)
            ballX = int(radio.receive())
            ballY = int(radio.receive())
            side = int(radio.receive())
            radio.send('good')
            break
        except TypeError:
            timeAdded += 50
            radio.send('bad')
            while True:
                lastMessage = radio.receive()
                if lastMessage == 'ping':
                    break
            radio.send('pong')
    return timeAdded


def doStuff():  # does everything other then rendering
    totalTimeAdded = 0
    transferPresses()
    totalTimeAdded += updatePaddle()
    totalTimeAdded += updateBall()
    return totalTimeAdded


radio.on()
while True:
    lastMessage = radio.receive()
    if lastMessage == 'ping':
        radio.send('pong')
        sleep(100)
        break
radio.send(str(running_time()))
while True:
    lastMessage = radio.receive()
    if type(lastMessage) is str:
        break
lastMessage = int(lastMessage)
while True:
    if running_time() >= lastMessage:
        break
render()
sleep(500)
while True:  # main loop
    timeToWait = 500 - doStuff()
    render()
    if side != 0:
        break
    sleep(timeToWait)
radio.off()
if side == 1:  # show sad face if the ball hit the top
    display.show(sadFace)
elif side == 2:  # show smiley face if the ball hit the bottom
    display.show(happyFace)
while True:  # end: won or lost
    display.set_pixel(ballX, ballY, 9)
    sleep(500)
    display.set_pixel(ballX, ballY, 0)
    sleep(500)
