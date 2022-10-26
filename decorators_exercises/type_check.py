def type_check(data_type):
    def decorator(fn):
        def wrapper(arg):
            if data_type == type(arg):
                return fn(arg)
            else:
                return f"Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))
