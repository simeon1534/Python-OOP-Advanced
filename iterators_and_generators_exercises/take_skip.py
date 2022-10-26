class take_skip:
    def __init__(self, step, skip):
        self.step = step
        self.skip = skip
        self.curr_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        curr_val = self.curr_value
        self.curr_value += self.step

        if curr_val / self.step  == self.skip:
            raise StopIteration()
        return curr_val


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
