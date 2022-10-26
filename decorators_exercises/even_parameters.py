def even_parameters(fn):
    def wrapper(*args):
        execute = True
        for el in args:
            if not isinstance(el, (float, int)) or el % 2 != 0:
                execute = False
        if execute:
            return fn(*args)
        else:
            return f'Please use only even numbers!'

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
