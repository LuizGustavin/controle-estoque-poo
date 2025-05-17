class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def exibir_produto(self):
        print(f"Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: {self.preco}")

    def repor_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque de {self.nome}. Novo estoque: {self.quantidade}")

    def vender(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades de {self.nome} vendidas. Estoque restante: {self.quantidade}")
        else:
            print(f"Estoque insuficiente. Estoque disponível de {self.nome}: {self.quantidade}")
