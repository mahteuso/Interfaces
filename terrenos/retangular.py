from interfaces.formas import FormasInterface

class TerrenoRetangular(FormasInterface):

    def __init__(self, lado: int, altura: int) -> None:
        self.lado = lado
        self.altura = altura

    def get_area(self):
        area = self.lado * self.altura
        return area

    def get_perimetro(self):
        perimetro = (self.lado * 2) + (self.altura * 2)
        return perimetro