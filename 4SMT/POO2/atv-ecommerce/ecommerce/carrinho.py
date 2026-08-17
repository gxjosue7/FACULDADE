from ecommerce.item_carrinho import ItemCarrinho
from ecommerce.pedido import Pedido


class Carrinho:

    def __init__(self) -> None:
        self.itens: list[ItemCarrinho] = []

    def adicionar_item(self, produto: "Produto", quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        self.itens.append(ItemCarrinho(produto, quantidade))

    def remover_item(self, produto: "Produto") -> None:
        self.itens = [i for i in self.itens if i.produto is not produto]

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self.itens)

    def quantidade_itens(self) -> int:
        return len(self.itens)

    def finalizar(self) -> Pedido:
        if not self.itens:
            raise ValueError("Carrinho vazio")
        pedido = Pedido()
        for item in self.itens:
            pedido.adicionar_item(item.produto, item.quantidade)
        return pedido