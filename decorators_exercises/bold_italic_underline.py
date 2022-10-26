def make_bold(fn):
    def wrapper(*args):
        text = fn(*args)
        new_text = f"<b>{text}</b>"
        return new_text

    return wrapper


def make_italic(fn):
    def wrapper(*args):
        text = fn(*args)
        new_text = f"<i>{text}</i>"
        return new_text

    return wrapper


def make_underline(fn):
    def wrapper(*args):
        text = fn(*args)
        new_text = f"<u>{text}</u>"
        return new_text

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

