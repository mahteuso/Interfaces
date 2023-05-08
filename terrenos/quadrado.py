from interfaces.formas import FormasInterface


class TerrenoQuadrado(FormasInterface):
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def get_area(self):
        area = self.lado * self.lado
        return area

    def get_perimetro(self):
        perimetro = self.lado * 4
        return perimetro


