# Python program showing
# use of __call__() method

class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):

        res = self.function(*args, **kwargs)
        with open('results.txt','a') as f:
            f.write(f"Function '{self.function.__name__}' was called. Result: {res}\n")






@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)