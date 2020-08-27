from serial import *
import sys
import threading

from flash import *

"""
py multi_flash.py K: COM4 L: COM5
"""

BAUDRATE = 115200

def copyAll(file, path, port):
    flashFile(file, [path])
    serial = Serial(
        port=port,
        baudrate=BAUDRATE,
        bytesize=EIGHTBITS,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        timeout=1,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False,
    )
    copyFile('core.py', serial)
    copyFile('interface.py', serial)
    copyFile('multiplayer.py', serial)

threads = [
    threading.Thread(target=copyAll, args=('multiplayerHost.py', sys.argv[1], sys.argv[2])),
    threading.Thread(target=copyAll, args=('multiplayerClient.py', sys.argv[3], sys.argv[4])),
]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
