from datetime import datetime, timedelta
from time import sleep
import psutil


def generate_report(duration: timedelta):
    measurements = []

    end_time = datetime.now() + duration

    now = datetime.now()
    while now < end_time:
        measurements.append((now, psutil.cpu_percent))
        now = datetime.now()
        sleep(0.02)

    return measurements


print(generate_report(duration=timedelta(seconds=3)))
