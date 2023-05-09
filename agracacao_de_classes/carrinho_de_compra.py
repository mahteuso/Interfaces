from interface import CarrinhoInterface
from produtos import Produto
from servicos import Servico
from typing import Type

class Compras:
    def __init__(self):
        self.produto = Produto('simplas', 1)
        self.servico = Servico('simples', 2)

    def adicionar_compra(self, produto: Type[CarrinhoInterface]) -> None:
        produto.adicionar_produto_ou_servico(produto)

    def finalizar(self):
        self.produto.finalizar_compras()
        self.servico.finalizar_compras()

