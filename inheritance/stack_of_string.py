class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        return self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

stack = Stack()
stack.push('baba')
stack.push('dqdo')
print(str(stack))