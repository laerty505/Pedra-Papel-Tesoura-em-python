import funcoes


funcoes.menu()


while True:
    try:
        escolha_inicial = int(input("Digite um número para começar! "))
    except ValueError:
        print("Digite apenas números!")
        continue

    match escolha_inicial:
        case 1:
            funcoes.jogar()
        case 2:
            pass
        case 3:
            print("Jogo Encerrado!")
            break
        case _:
            print("Digite um número válido!")
    
    funcoes.menu()



