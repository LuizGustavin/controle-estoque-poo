from Produto import Produto
from ProdutoAlimenticio import ProdutoAlimeticio

lista_Produto = []
def mostrar_menu():
    print("\n ==== Menu ====\n")
    print("1. Cadastrar produto não alimenticio")
    print("2. Cadastrar produto alimenticio")
    print("3. Listar produtos em estoque")
    print("4. Sair ")
mostrar_menu()
opcao = input("Qual opção você ira escolher: ")
while opcao !=4:
    if opcao == "1":
       nome = input("Informe o nome do produto que você quer cadastrar (informe um produto não alimenticio): ")
       quantidade = int(input("Informe a quantidade: "))
       preco = float(input("Informe o preço: "))
      
       produto = Produto(nome, quantidade, preco)
       lista_Produto.append(produto)
       print(f"Foi cadastrado o produto: {nome} | Sua quantidade é: {quantidade} | Preço: {preco} ")
       
       
    elif opcao == "2":
       nome = input("Informe o nome do produto que você quer cadastrar: ")
       quantidade = int(input("Informe a quantidade: "))
       preco = float(input("Informe o preço: "))
       data_validade = input("Informe a data de validade: ")
      
       produto_alimenticio = ProdutoAlimeticio(nome, quantidade, preco, data_validade)
       lista_Produto.append(produto_alimenticio)
       print(f"Foi cadastrado o produto: {nome} | Sua quantidade é: {quantidade} | Preço: {preco} | Data de validade: {data_validade}")
    
    
    elif opcao == "3":
        for i in lista_Produto: 
            i.exibir_produtos()
            
    elif opcao == "4":
        print("saindo....")
        break
    
    else:
        print("Opcão invalida")
        

    
        