class Atleta:
    def __init__(self, peso, aposentado=False):
        self.peso = peso
        self.aposentado = aposentado

    def aposentar(self):
        if self.aposentado is False:
            self.aposentado = True
            print("Atleta aposentou... bateu as chuteiras")
        else:
            print("Atleta já está aposentado, é golpe?")

    def aquecer(self):
        if self.aposentado is True and self.peso > 60:
            print("Não pode aquecer, pois está aposentado!")
        else:
            print("Aquecendo para a competição.....")


class Corredor(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    def correr(self):
        if self.aposentado is True:
            print("Não consegue correr, está aposentado")
        else:
            print("Correndo tão rápido que voê não viu... fiummmnnnnnn")

class Nadador(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    def nadar(self):
        if self.aposentado is True:
            print("Não consegue nadar, está aposentado")
        else:
            print("nadando....... tchá, tchá, tchá")

class Ciclista(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    def pedalar(self):
        if self.aposentado is True:
            print("Não consegue pedalar, está aposentado")
        else:
            print("Pedalando... saia da frente")


class TriAtleta(Nadador, Corredor, Ciclista):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)

