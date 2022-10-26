class vowels:
    vowels_tuple = ('a', 'e', 'i', 'o', 'y', 'u', 'A', 'E', 'I', 'O', 'Y', 'U')

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            if self.string[self.index] in self.vowels_tuple:
                current_vowel = self.string[self.index]
                self.index += 1
                return current_vowel
            self.index += 1
        raise StopIteration()


my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)

