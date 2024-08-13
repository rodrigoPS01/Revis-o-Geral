carrinho = []

def adicionar_produto():
    produto = {
        'nome': input('Qual o nome do produto: '),
        'valor': float(input('Qual o valor do produto: ')),
        'quantidade': int(input('Qual a quantidade que você pegou: '))
    }

    produto['total'] = round(produto['valor'] * produto['quantidade'], 2)
    
    carrinho.append(produto)
    
    print(f"Produto {produto['nome']} adicionado ao carrinho.")

def remover_produto():
    produto = input('Qual o nome do produto: ')

    for produto_atual in carrinho:
        if produto_atual['nome'] == produto:
            carrinho.remove(produto_atual)
            print(f"Produto {produto} removido do carrinho.")
            break
    else:
        print(f"Produto {produto} não encontrado no carrinho.")

def ver_carrinho():
    if not carrinho:
        print("O carrinho está vazio.")
        return
    
    print("Lista de produtos no carrinho:")
    valor_total_geral = 0

    for produto in carrinho:
        print(f"Nome: {produto['nome']}, Valor Unitário: R${produto['valor']:.2f}, Quantidade: {produto['quantidade']}, Total: R${produto['total']:.2f}")
        valor_total_geral += produto['total']

    print(f"Valor total de todos os produtos: R${valor_total_geral:.2f}")

def atualizar_carrinho():
    produto = input('Qual o nome do produto que você deseja atualizar: ')

    for produto_atual in carrinho:
        if produto_atual['nome'] == produto:
            while True:
                menu = int(input('''
                                 1 - Atualizar nome
                                 2 - Atualizar valor
                                 3 - Atualizar quantidade
                                 0 - Encerrar
                                 Escolha: '''))
                if menu == 1:
                    produto_atual['nome'] = input('Qual o novo nome do produto: ')
                    print(f"Nome do produto atualizado para {produto_atual['nome']}.")
                elif menu == 2:
                    produto_atual['valor'] = float(input('Qual o novo preço do produto: '))
                    produto_atual['total'] = round(produto_atual['valor'] * produto_atual['quantidade'], 2)
                    print(f"Valor do produto atualizado para R${produto_atual['valor']:.2f}.")
                elif menu == 3:
                    produto_atual['quantidade'] = int(input('Qual a nova quantidade do produto: '))
                    produto_atual['total'] = round(produto_atual['valor'] * produto_atual['quantidade'], 2)
                    print(f"Quantidade do produto atualizada para {produto_atual['quantidade']}.")
                elif menu == 0:
                    break
                else:
                    print('Escolha uma opção válida.')
            break
    else:
        print(f"Produto {produto} não encontrado no carrinho.")

while True:
    
    menu = int(input('''
                    1 - Adicionar produto
                    2 - Ver carrinho
                    3 - Atualizar carrinho
                    4 - Remover produto
                    0 - Encerrar
                    Escolha: '''))
    
    match menu:
        case 1:
            adicionar_produto()
        case 2:
            ver_carrinho()
        case 3:
            atualizar_carrinho()
        case 4:
            remover_produto()
        case 0:
            break
        case _:
            print('Digite uma opção válida.')
