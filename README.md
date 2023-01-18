# Detalhes da Implementação

Foi usada a versão 3.10.6 do Python.
Armazenei código num repositório privado no github, se precisarem passo o acesso.
A Pilha (Stack) e a Fila (Queue) foram implementadas com Linked Listas.
Para isso criei a clase nó (Node) que armazena os dados e a posição next.

## Implementação da Pilha (Stack)

Basicamente precisa ficar atualizando o topo (top) e o tamanho size da Stack
a cada operação push ou pop.

Implementei o método `__len__` para poder usar len(stack) e o método `__str__` para
permitir a impressão print(stack)

## Implementação da Fila (Queue)

Basicamente precisa ficar atualizando o primeiro (head) e o tamanho size da Queue
a cada operação enqueue ou dequeue.

Implementei o método `__len__` para poder usar len(queue) e o método `__str__` para
permitir a impressão print(queue)

## Os testes

O código passou em todos os testes porém no arquivo de testes precisei modificar duas coisas:

<ul>
<li>
No método `test_push_items()` da stack estava `stack.add(test)` e o correto é `stack.push(test)`
</li>
<li>
Nos métodos `test_print()` não dá para comparar a saída de print() com string, portanto
comparei o print() esperado com o print() resultante
</li>

</ul>
