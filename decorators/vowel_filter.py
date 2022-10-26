def check_for_vowel(char):
    vowels = 'aeiouy'
    if char.lower() in vowels:
        return True


def vowel_filter(fn):
    def wrapper(*args, **kwargs):
        letters = fn(*args,**kwargs)
        res = []
        for char in letters:
            if check_for_vowel(char):
                res.append(char)
        return res

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
