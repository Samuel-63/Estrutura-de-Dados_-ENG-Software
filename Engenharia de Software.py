class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir_recursivo(no.direita, valor)
        return no

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no, valor):
        if no is None:
            return False
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        else:
            return self._buscar_recursivo(no.direita, valor)

    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)
        print()

    def _em_ordem_recursivo(self, no):
        if no:
            self._em_ordem_recursivo(no.esquerda)
            print(no.valor, end=' ')
            self._em_ordem_recursivo(no.direita)

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return None
        if valor < no.valor:
            no.esquerda = self._remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            temp = self._min_valor(no.direita)
            no.valor = temp.valor
            no.direita = self._remover_recursivo(no.direita, temp.valor)
        return no

    def _min_valor(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual

def exemplo_sistema_notas():
    arvore_notas = ArvoreBinariaBusca()

    notas = [75, 88, 92, 60, 70, 85, 50]
    for nota in notas:
        arvore_notas.inserir(nota)

    print("Notas cadastradas (ordem crescente):")
    arvore_notas.em_ordem()

    nota_procurada = 85
    if arvore_notas.buscar(nota_procurada):
        print(f"\nNota {nota_procurada} foi registrada.")
    else:
        print(f"\nNota {nota_procurada} não encontrada.")

    nota_errada = 60
    print(f"\nRemovendo a nota {nota_errada}...")
    arvore_notas.remover(nota_errada)

    print("Notas após remoção:")
    arvore_notas.em_ordem()

if __name__ == "__main__":
    exemplo_sistema_notas()