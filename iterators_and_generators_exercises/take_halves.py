def solution():
    def integers():
        i = 1
        while i < 9999999:
            yield i
            i += 1

    def halves():
        for i in integers():
            res = i / 2
            yield res

    def take(n, seq):
        new_seq = list(seq)[:n]
        return new_seq

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(50, halves()))
