from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
 
    def __len__(self):
        return self.size

    def is_empty(self):
        return True if self.__len__() == 0 else False


    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
        self.size += 1
 
    def dequeue(self):
        if self.head is None:
            raise QueueDequeueException
        else:
            to_return = self.head.data
            self.head = self.head.next
            self.size -= 1
            return to_return

    def __str__(self):
        message = ""
        chrs = " -> "
        if (self.head is not None):
            message = message +str(self.head.data)
            while(True):
                if(self.head.next is None): #this is our do-while loop emulation, checking if this is the last Node
                    break
                self.head = self.head.next #update cur so we move on in the next iteration 
                message = message + chrs+str(self.head.data)
        return f"{message}"


class QueueDequeueException(Exception):
    def __init__(self):
        "no initial values"
        pass

    def __str__(self):
        return "queue is empty"
