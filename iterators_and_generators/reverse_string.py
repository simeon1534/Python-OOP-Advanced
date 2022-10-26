def reverse_text(string):
    reverse_string = string[::-1]
    for s in reverse_string:
        yield s

for char in reverse_text("step"):
    print(char, end='')
