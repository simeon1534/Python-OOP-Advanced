class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.countdown = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.countdown == -1:
            raise StopIteration()
        current_countdown = self.countdown
        self.countdown -= 1
        return current_countdown


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
