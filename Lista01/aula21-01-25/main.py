from controllers.produto_controller import ProdutoController

def menu():
    print("\n--- CRUD de Produtos ---")
    print("1. Criar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Produto")
    print("4. Deletar Produto")
    print("5. Buscar Produto por nome")
    print("6. Buscar por faixa de preço")
    print("7. Ordenar produtos")
    print("0. Sair")
    return input("Escolha uma opção:")

if __name__ == "__main__":
    controller = ProdutoController()

while True:
    opcao = menu()
    if opcao == "1":
        id = int(input("Digite o ID do Produto:"))
        nome = input("Digite o Nome do Produto:")
        preco = float(input("Digite o Preço do Produto:"))
        controller.criar_produto(id, nome, preco)
    
    elif opcao == "2":
        controller.listar_produtos()
    
    elif opcao == "3":
        id = int(input("Digite o ID do Produto que deseja atualizar:"))
        nome = input("Digite o novo nome (ou deixe em branco):")
        preco = float(input("Digite o novo preço (ou deixe em branco):"))      
        controller.atualizar_produto(id, nome, preco)
    
    elif opcao == "4":
        id = int(input("Digite o ID do Produto que deseja deleta:"))
        controller.deletar_produto(id)        
    
    elif opcao == "5":
        nome = input("Digite o nome do produto:")
        controller.busca_produto_nome(nome)

    elif opcao == "6":
        inicio = float(input("Digite o valor Inicial"))
        fim = float(input("Digite o valor final"))
        controller.buscar_produto_preco(inicio, fim)

    elif opcao == "7":
            print("Escolha um critério de ordenação: 'id', 'nome', 'preco' ou 'todos'")
            criterio = input("Ceitério: ").lower()
            controller.ordenar_produtos(criterio)

    elif opcao == "0":
        print("Encerrando")
        break
    else:
        print("Opção Invalida")