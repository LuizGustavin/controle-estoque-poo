class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def exibir_produto(self):
        print(f"o produto {self.nome} tem {self.quantidade} no estoque ----> preço: {self.preco} | a data de validade: {self.data_validade} ")