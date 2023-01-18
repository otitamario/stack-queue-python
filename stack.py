class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return True if self.size() == 0 else False
