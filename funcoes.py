import random

def menu():
    print("-----PEDRA, PAPEL E TESOURA-----")
    print("Escolha uma Opção!")
    print()

    print("1 - Um Jogador")
    print("2 - Dois Jogadores")
    print("3 - Sair")






def jogar():
    while True:
        print("Faça uma escolha!")
        print()


        opcoes_computador = ['pedra', 'papel', 'tesoura']

        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if jogador not in opcoes_computador:
            print("Escolha Inválida!")
            continue


        computador = random.choice(opcoes_computador)

        print()

        print(f"Computador escolheu: {computador}\n")
    
        if jogador not in opcoes_computador:
            print("Escolha Inválida!")
            return

        if jogador == computador:
            print("Empate!\n")
        
        elif jogador == 'pedra' and computador == 'tesoura':
            print("Você venceu!\n")
        
        elif jogador == 'papel' and computador == 'pedra':
            print("Você venceu!\n")
        
        elif jogador == 'tesoura' and computador == 'papel':
            print("Você venceu!\n")
        
        else:
            print("Computador venceu!\n")

        print('Deseja jogar novamente?')
        print("S - Sim")
        print('N - Não (Voltar ao menu)')
        verifica_jogar_novamente = input("Digite (S/n): ").lower()
        if verifica_jogar_novamente != "s":
            break
        
           


   




    