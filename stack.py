class Stack:
    def __init__(self):
        self.elements = []
        self.top = 0

    def push(self, data):
        self.elements.append(data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise StackPopException
        else:
            self.top -= 1
            return self.elements.pop()

    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        return True if self.__len__() == 0 else False

    def __repr__(self):
        message = ""
        chrs = " -> "
        for i in range(self.top-1,-1,-1):
            if(i == self.top -1):
                message = message +str(self.elements[i])
            else:
                message = message + chrs+str(self.elements[i])

        return f"{message}"


class StackPopException(Exception):
    def __init__(self):
        "no initial values"
        pass

    def __str__(self):
        return "stack is empty"
