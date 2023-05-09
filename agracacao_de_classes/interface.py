from abc import ABC, abstractmethod


class CarrinhoInterface(ABC):

    @abstractmethod
    def adicionar_produto_ou_servico(self):
        ...

    @abstractmethod
    def finalizar_compras(self):
        ...
