import random

# Este bloco define a classe carta como sendo um objeto que possui os atributos cor e tipo
class Carta:
    def __init__(self, cor, tipo):
        self.cor = cor
        self.tipo = tipo

    def __str__(self):
        if (self.tipo == "+4" or self.tipo == "escolhacor"):
            return "Carta " + str(self.tipo)
        else:
            return "Carta " + str(self.tipo) + " " + str(self.cor)

    def __repr__(self):
        return self.__str__()


# Este bloco define a classe Monte (que modela a pilha de compra da partida) como sendo uma lista que possui os
# metodos desempilhaMonte, que retorna 1 carta da lista, e getMonte, que retorna toda a lista
class Monte:
    def __init__(self):
        self.CORES_VALIDAS = ["amarelo", "azul", "verde", "vermelho"]
        self.TIPOS_VALIDOS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "reverso", "pula", "escolhacor", "+4"]
        self._monte = []
        
        for i in self.CORES_VALIDAS:
            for j in self.TIPOS_VALIDOS:
                # FIX: Isso aqui pode gerar mais de uma carta 0. Também pode gerar cartas inválidas, por ex 'preto azul'
                self._monte.append(Carta(i, j))
                self._monte.append(Carta(i, j))
        random.shuffle(self._monte)

    def getMonte(self):
        temp = []
        for x in self._monte:
            temp.append(x)
        return temp

    def desempilhaMonte(self):
        return self._monte.pop()
