from Produto import Produto 

class ProdutoAlimeticio(Produto):
    def __init__(self, nome, preco, quantidade ,data_validade):
        super().__init__ (nome, preco, quantidade )
        self.data_validade = data_validade
        