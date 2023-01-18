class Node(object):
    """
    Classe de Nós para a lista 
    """
    def __init__(self,data=None, next=None):
        """
        Inicialiando a classe com os dados
        data e o próximo nó vazio
        """
        self.data = data
        self.next = next
