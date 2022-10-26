# Import the required library
from tkinter import *
from tkinter import messagebox
import time
import subprocess
from multiprocessing import Process


def trigger_timer():
    subprocess.call("auto_stop.py", shell=True)


SCHEDULED_TIME = 10

counter = 0
while counter < SCHEDULED_TIME:
    time.sleep(1)  # currently 10
    counter += 1
    if counter == 9:
        trigger_timer()
        messagebox.showinfo("", "Shutting down!")
