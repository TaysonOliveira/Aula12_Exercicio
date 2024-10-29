ListaDeCompras = []

opcao = 10

while opcao != 0:
    print('\n ==================\n')
    print('1 - Adicionar Novo Item')
    print('2 - Remover Item')
    print('3 - Exibir Lista Completa')
    print('0 - Sair')
    opcao = int(input('Digite a Opção Desejada: '))

    if opcao == 1:
        print('\n ===> ADICIONAR ITEM <===\n')

        novo_item = input('Digite o Novo Item a Ser Adicionado: ')
        ListaDeCompras = ListaDeCompras + [novo_item]

    elif opcao == 2:
        print('\n ===> REMOVER ITEM <===\n')

        for i in range(len(ListaDeCompras)):
            print(f'{i+1} - {ListaDeCompras[i]}')

        print('\n ====')

        item_removedor = int(input('Digite o Codigo Do Item: ')) - 1
        del ListaDeCompras[item_removedor]

    elif opcao == 3:
        print('\n ===> LISTA COMPLETA <===\n')

        for i in range(len(ListaDeCompras)):
            print(f'{i+1} - {ListaDeCompras[i]}')