from node import Node

class Stack:
    """
    Classe Stack implementada com Linked List
    """
    def __init__(self):
        """
        Inicializando com o topo vazio
        e tamanho size = 0
        """
        self.top = None
        self.size = 0
    def push(self, data):
        """
        Método push que adiciona um novo elemento
        à Pilha, atualizando o top e o size
        """
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node 
        self.size += 1 
        
    def pop(self):
        """
        Método pop que remove o elemento top da 
        Pilha, atualizando o top e o size
        Se a Pilha for vazia, gera a excessão
        """
        if self.is_empty():
            raise StackPopException
        result = self.top.data
        self.top = self.top.next
        self.size -= 1
        return result

    def __len__(self):
        """
        Método que permite usar len(stack)
        retornando o tamanho da Pilha
        """
        return self.size

    def is_empty(self):
        """
        Método que retorna se a Pilha 
        é vazia ou não
        """
        return True if self.__len__() == 0 else False

    
    def __str__(self):
        """
        Método que permite a impressão da Pilha
        """
        message = ""
        chrs = " -> "
        temp = self.top
        if (temp is not None):
            message = message +str(temp.data)
            while (temp):
                if(temp.next is None): 
                    break
                temp = temp.next # mover para a próxima iteracao 
                message = message + chrs+str(temp.data)
            
        return f"{message}"


class StackPopException(Exception):
    """
    Classe De Excessão para uma Pilha vazia
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
        return "stack is empty"
