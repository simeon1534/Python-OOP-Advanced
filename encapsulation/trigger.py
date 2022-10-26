# Import the required library

import time
import subprocess
from multiprocessing import Process
from test import counter as c


def trigger_timer():
    subprocess.call("auto_stop.py", shell=True)


while True:
    if c == 8:
        trigger_timer()
        break
