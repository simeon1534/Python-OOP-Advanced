class reverse_iter:
    def __init__(self, iterator):
        self.iterator = iterator  # [1,2,3,4]
        self.i = len(iterator) - 1  # 3 index
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            curr_item = self.iterator[self.i]
            self.i -= 1

            return curr_item
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
