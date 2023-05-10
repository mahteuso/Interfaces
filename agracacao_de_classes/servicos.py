from interface import CarrinhoInterface


class Servico(CarrinhoInterface):
    def __init__(self, ser_nome: str, ser_valor: int) -> None:
        self.ser_nome = ser_nome
        self.ser_valor = ser_valor

    def __repr__(self):
        return {f'{self.ser_nome}' ':' f'{self.ser_valor}'}
