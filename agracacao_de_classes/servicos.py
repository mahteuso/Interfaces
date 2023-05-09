from interface import CarrinhoInterface
# from typing import Type
class Servico(CarrinhoInterface):
    def __init__(self, ser_nome: str, ser_valor: int) -> None:
        self.ser_nome = ser_nome
        self.ser_valor = ser_valor
        self.__servicos = []

    def informacoes_servico(self) -> None:
        print(f'Serviço: {self.ser_nome} / valor R$ {self.ser_valor},00')

    def adicionar_produto_ou_servico(self, produto) -> None:
        self.__servicos.append(produto)

    def finalizar_compras(self) -> None:
        print('Compras finalizadas com sucesso!')

        for produto in self.__servicos:
            produto.informacoes_produto()