from interfaces.formas import FormasInterface


class Engenheiro:
    def __init__(self, nome):
        self.nome = nome

    def mede_area(self, terreno: type(FormasInterface)):
        area = terreno.get_area()
        return f'O engenheiro {self.nome} mediu uma área de {area}m2 '

    def mede_perimetro(self, terreno: type(FormasInterface)):
        perimetro = terreno.get_perimetro()
        return f'O engenheiro {self.nome} mediu um perímetro de {perimetro}m'
