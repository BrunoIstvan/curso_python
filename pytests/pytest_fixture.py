class Usuario:

    def __init__(self, nome) -> None:
        self.nome = nome

class ItemDoCarrinho:

    def __init__(self, nome, valor, quantidade) -> None:
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade


class CarrinhoDeCompras:

    def __init__(self, usuario: Usuario) -> None:
        self.usuario = usuario
        self.itens = []
        self._total = 0
        self._subtotal = 0

    def adiciona(self, item: ItemDoCarrinho):
        self._total += (item.valor * item.quantidade)
        self._subtotal = self._total
        self.itens.append(item)

    @property
    def subtotal(self):
        return self._subtotal

    @property
    def total(self):
        return self._total
    
    def aplica_desconto(self, desconto):
        self._total -= desconto
