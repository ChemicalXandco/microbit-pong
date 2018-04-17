# microbit-pong
A relatively simple pong program for the BBC micro:bit using micropython
# Main Instructions:
There are 2 main 'editions': singleplayer and multiplayer. In singleplayer, there is an impossible one and a possible one. In multiplayer
there is a host and a client.
You press the A button to make your paddle go left and the B button to make it go right. When the ball hits the paddle, it will bounce of it. If it hits the top or bottom you will win or lose the game. Press the reset button to start another game.
# Instructions for singleplayer: 
As in the main instructions, but you control the bottom paddle and the program controls the top one. The impossible one is theoretically impossible as it always makes sure that it is blocking the ball. The possible one has an element of random so it might not stop the ball which allows you to win.  
# Instructions for multiplayer:
As in the main instructions, but this program is 'good enough' and is not reliable at all, due to the nature of the microbit's radio system. This program uses the radio module to send and recieve messages. As mentioned in the main instructions, There is a client and host version of the program. For this, you need 2 microbits and a different program flashed on each. You need to start/reset the client !before! you start/reset the host and then they will talk to each other over radio. The range is not very good so It is recommended that you have the microbits close to each other. The client controls the top paddle and the host controls the bottom one. An error will probably interrupt your gameplay but there's not much I can do about that apart from changing the perimeters of the radio module which I don't want to do.
