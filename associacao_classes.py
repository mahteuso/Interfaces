"Usando a associação de classes"

from typing import Type


class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def ligar(self):
        print(f'Acendendo a luz do {self.__comodo}')

    def desligar(self):
        print(f'Apagando a luz do {self.__comodo}')

class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.ligar()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.desligar()


