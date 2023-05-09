from interface import CarrinhoInterface
# from typing import Type
class Produto(CarrinhoInterface):
    def __init__(self, prod_nome: str, prod_valor: int) -> None:
        self.prod_nome = prod_nome
        self.prod_valor = prod_valor
        self.__produtos = []

    def informacoes_produto(self) -> None:
        print(f'Produto: {self.prod_nome} / valor R$ {self.prod_valor},00')

    def adicionar_produto_ou_servico(self, produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compras(self) -> None:
        print('Compras finalizadas com sucesso!')

        for produto in self.__produtos:
            produto.informacoes_produto()


