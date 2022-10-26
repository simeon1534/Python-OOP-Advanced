class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        res = f"{self.hours}:{self.minutes}:{self.seconds}"
        if self.seconds < 10:
            res = f"{self.hours}:{self.minutes}:0{self.seconds}"
            if self.minutes < 10:
                res = f"{self.hours}:0{self.minutes}:0{self.seconds}"
                if self.hours < 10:
                    res = f"0{self.hours}:0{self.minutes}:0{self.seconds}"

        return res

    def next_second(self):
        self.seconds = (self.seconds + 1) % 60
        self.minutes = (self.minutes + (self.seconds == 0)) % 60
        self.hours = (self.hours + (self.minutes == 0)) % 24
        return self.get_time()
time = Time(2, 59, 4)
print(time.next_second())
