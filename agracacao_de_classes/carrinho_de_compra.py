from interface import CarrinhoInterface
from typing import Type


class Compras:
    def __init__(self):
        self._compras = {}

    def adicionar_compra(self, produto: Type[CarrinhoInterface]) -> None:
        produto = str(produto)
        print(produto)
        self._compras.update(produto)
        for compra, valor in self._compras.items():
            print(compra, ':', valor)




