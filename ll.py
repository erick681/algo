class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no

    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.primeiro is None:
            self.primeiro = novo_no
            return
        ultimo = self.primeiro
        while ultimo.proximo:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_no

    def remover(self, dado):
        atual = self.primeiro
        if atual is None:
            return
        if atual.dado == dado:
            self.primeiro = atual.proximo
            return
        while atual.proximo:
            if atual.proximo.dado == dado:
                atual.proximo = atual.proximo.proximo
                return
            atual = atual.proximo

    def imprimir(self):
        atual = self.primeiro
        while atual:
            print(atual.dado, end=' ')
            atual = atual.proximo
        print()

# Exemplo de uso:
lista = ListaEncadeada()
lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)
lista.inserir_fim(4)
lista.imprimir()  # Saída: 3 2 1 4
lista.remover(2)
lista.imprimir()  # Saída: 3 1 4

