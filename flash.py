import sys
import os
import time

from uflash import flash
from microfs import put

DELAY = 1

def copyFile(fpath):
    put(fpath, target=fpath)
    print('successfully copied', fpath)

def copyGame():
    for path, subdirs, files in os.walk('game'):
        for fname in files:
            copyFile('game/' + fname)
            time.sleep(DELAY)

def flashFile():
    f = sys.argv[1]
    flash(path_to_python=f)
    print('flash successful')

flashFile()
time.sleep(DELAY)
copyGame()
