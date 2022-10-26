def fibonacci():
    pre_previous_num = 0
    yield pre_previous_num
    previous_num = 1
    yield previous_num

    while True:
        new_num = pre_previous_num + previous_num
        yield new_num
        pre_previous_num = previous_num
        previous_num = new_num




generator = fibonacci()
for i in range(10):
    print(next(generator))
