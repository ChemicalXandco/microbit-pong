import sys
import time

from uflash import flash
from microfs import put

DELAY = 1

def flashFile(f, paths_to_microbits=None):
    flash(path_to_python=f, paths_to_microbits=paths_to_microbits)
    print('flash successful')
    time.sleep(DELAY)

def copyFile(fpath, serial=None):
    put(fpath, target=fpath, serial=None)
    print('successfully copied', fpath)
    time.sleep(DELAY)

if __name__ == "main":
    flashFile(sys.argv[1])
    copyFile('core.py')
    copyFile('interface.py')
