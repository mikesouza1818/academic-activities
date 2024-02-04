lista_de_compras = []
def adicionar_item(item):
    lista_de_compras.append(item)
    print(f"{item} adicionado à lista.")
def remover_item(item):
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f"{item} removido da lista.")
    else:
        print(f"{item} não encontrado na lista.")
def visualizar_lista():
    if lista_de_compras:
        print("Lista de Compras:")
        for item in lista_de_compras:
            print(f"- {item}")
    else:
        print("A lista de compras está vazia.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Visualizar Lista")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            item = input("Digite o item a ser adicionado: ")
            adicionar_item(item)
        elif escolha == '2':
            item = input("Digite o item a ser removido: ")
            remover_item(item)
        elif escolha == '3':
            visualizar_lista()
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa chamando o menu principal
menu()
1