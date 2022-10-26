class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = [s for s in sequence]
        self.number = number
        self.idx = 0
        self.repeats = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.repeats == self.number:
            raise StopIteration()
        if self.idx == len(self.sequence):
            self.idx = 0
        current_idx = self.sequence[self.idx]
        self.idx +=1
        self.repeats +=1
        return current_idx

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
