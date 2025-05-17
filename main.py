from Produto import Produto
from ProdutoAlimenticio import ProdutoAlimenticio

lista_Produto = []

def mostrar_menu():
    print("\n ==== Menu ====\n")
    print("1. Cadastrar produto não alimentício")
    print("2. Cadastrar produto alimentício")
    print("3. Listar produtos em estoque")
    print("4. Repor estoque de produto")
    print("5. Venda de produto")
    print("6. Sair")

while True:
    mostrar_menu()
    opcao = input("Qual opção você irá escolher: ")

    if opcao == "1":
        nome = input("Nome do produto (não alimentício): ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        produto = Produto(nome, quantidade, preco)
        lista_Produto.append(produto)
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do produto alimentício: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        data_validade = input("Data de validade: ")
        produto = ProdutoAlimenticio(nome, quantidade, preco, data_validade)
        lista_Produto.append(produto)
        print("Produto alimentício cadastrado com sucesso!")

    elif opcao == "3":
        for produto in lista_Produto:
            produto.exibir_produto()

    elif opcao == "4":
        nome = input("Informe o nome do produto para repor o estoque: ")
        encontrado = False
        for produto in lista_Produto:
            if produto.nome == nome:
                quantidade = int(input("Informe a quantidade a ser adicionada: "))
                produto.repor_estoque(quantidade)
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")


    elif opcao == "5":
        nome = input("Informe o nome do produto que deseja vender: ")
        encontrado = False
        for produto in lista_Produto:
            if produto.nome == nome:
                quantidade = int(input("Informe a quantidade a ser vendida: "))
                produto.vender(quantidade)
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")

        

    
        