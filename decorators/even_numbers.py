def even_numbers(function):
    def wrapper(*args,**kwargs):
        fn_res = function(*args,**kwargs)
        res = [n for n in fn_res if n % 2 ==0]
        return res
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
