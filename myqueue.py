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
        """
        Método que permite a impressão da Pilha
        """
        message = ""
        chrs = " -> "
        temp = self.head
        if (temp is not None):
            message = message +str(temp.data)
            while (temp):
                if(temp.next is None): 
                    break
                temp = temp.next # mover para a próxima iteracao 
                message = message + chrs+str(temp.data)
            
        return f"{message}"



class QueueDequeueException(Exception):
    def __init__(self):
        "no initial values"
        pass

    def __str__(self):
        return "queue is empty"
