import funcoes


while True:

    funcoes.limpar_terminal()

    funcoes.menu()

    try:
        escolha_inicial = int(input("Digite um número para começar! "))
    except ValueError:
        print("Digite apenas números!")
        continue

    match escolha_inicial:
        case 1:
            funcoes.limpar_terminal()
            funcoes.jogar()
        case 2:
            funcoes.limpar_terminal()
            funcoes.jogar_dois_jogadores()
        case 3:
            funcoes.limpar_terminal()
            print("Jogo Encerrado!")
            break
        case _:
            print("Digite um número válido!")
    
    funcoes.menu()



