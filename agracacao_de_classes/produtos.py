from interface import CarrinhoInterface


class Produto(CarrinhoInterface):
    def __init__(self, prod_nome: str, prod_valor: int) -> None:
        self.prod_nome = prod_nome
        self.prod_valor = prod_valor

    def __repr__(self):
        return {f'{self.prod_nome}' ':' f'{self.prod_valor}'}
