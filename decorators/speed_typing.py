import time


def measure_time(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        total = end - start
        print(f"Total time: {total}")
        return res

    return wrapper


@measure_time
def type_word(word):
    typing_word = input()
    if typing_word == word:
        return 'Success'
    return 'Wrong word!'


print(type_word('duma'))
