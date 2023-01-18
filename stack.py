class Node(object):
    def __init__(self,d):
        self.data = d
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, d):
        new_node = Node(d)
        if self.top:
            new_node.next = self.top
        self.top = new_node 
        self.size += 1 
        
    def pop(self):
        if self.is_empty():
            raise StackPopException
        result = self.top.data
        self.top = self.top.next
        self.size -= 1
        return result

    def __len__(self):
        return self.size

    def is_empty(self):
        return True if self.__len__() == 0 else False

    def __str__(self):
        message = ""
        chrs = " -> "
        if (self.top is not None):
            message = message +str(self.top.data)
            while(True):
                if(self.top.next is None): #this is our do-while loop emulation, checking if this is the last Node
                    break
                self.top = self.top.next #update cur so we move on in the next iteration 
                message = message + chrs+str(self.top.data)
        return f"{message}"


class StackPopException(Exception):
    def __init__(self):
        "no initial values"
        pass

    def __str__(self):
        return "stack is empty"
