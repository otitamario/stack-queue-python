from node import Node

class Queue:
    """
    Classe Queue implementada com Linked List
    """
    
    def __init__(self):
        """
        Inicializando o primeiro e o último
        da fila como vazios e tamanho = 0
        """
        self.head = None
        self.last = None
        self.size = 0
 
    def __len__(self):
        """
        Método que permite usar len(queue)
        retornando o tamanho da Fila
        """
        return self.size

    def is_empty(self):
        """
        Método que retorna se a Fila 
        é vazia ou não
        """
        return True if self.__len__() == 0 else False


    def enqueue(self, data):
        """
        Método que adiciona um novo elemento
        ao Final da Fila, atualizando o head, last
        e size
        """
        
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
        self.size += 1
 
    def dequeue(self):
        """
        Método pop que remove o primeiro elemento da 
        Fila, atualizando o head e o size.
        Se a Fila for vazia, gera a excessão
        """
        
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
    """
    Classe De Excessão para uma Fila
    """
    def __init__(self):
        """
        Sem valores iniciais
        """
        pass

    def __str__(self):
        """
        Permite a impressão da classe
        """
        return "queue is empty"
