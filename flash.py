import sys
import os
import time

from uflash import flash
from microfs import put

DELAY = 1

def flashFile():
    f = sys.argv[1]
    flash(path_to_python=f)
    print('flash successful')

def copyFile(fpath):
    put(fpath, target=fpath)
    print('successfully copied', fpath)

flashFile()
time.sleep(DELAY)
copyFile('core.py')
time.sleep(DELAY)
copyFile('interface.py')
