def gen_dict(dict_obj):
    for x, y in dict_obj.items():
        yield x, y


class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.keys = [key for key in self.dict_obj.keys()]
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.keys):
            raise StopIteration()
        current_key = self.keys[self.idx]
        current_value = self.dict_obj[current_key]
        self.idx += 1
        return current_key, current_value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
