def execute(fn,*args):
    return fn(*args)

# or

# execute = lambda fn, *args: fn(*args)

def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")

def say_bye(name):
    print(f"Bye, {name}")

execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")
