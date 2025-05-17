from Produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, quantidade, preco, data_validade):
        super().__init__(nome, quantidade, preco)
        self.data_validade = data_validade

    def exibir_produto(self):
        print(f"Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: {self.preco} | Validade: {self.data_validade}")

        