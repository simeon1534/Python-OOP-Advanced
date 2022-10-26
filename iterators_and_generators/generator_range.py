def genrange(start, end):
    for num in range(start, end + 1):
        yield num


# genrange = lambda start, end: (num for num in range(start, end + 1))

class GeneratorRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return genrange(self.start, self.end)

gen = GeneratorRange(1, 10)
for i in gen:
    print(i)
