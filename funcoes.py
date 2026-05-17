import random
from getpass import getpass

def menu():
    print("-----PEDRA, PAPEL E TESOURA-----")
    print("Escolha uma Opção!")
    print()

    print("1 - Um Jogador")
    print("2 - Dois Jogadores")
    print("3 - Sair")






def jogar():
    while True:
        print("Faça uma escolha!\n")


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

def jogar_dois_jogadores():
    while True:
        opcoes = ["pedra", "papel", "tesoura"]
        print('Jogador 1, Escolha!\n')

        jogador1 = getpass("Escolha pedra, papel ou tesoura:").lower()

        if jogador1 not in opcoes:
            print("Escolha Inválida!")
            continue

        print('Jogador 2, Escolha!\n')

        jogador2 = getpass("Escolha pedra, papel ou tesoura:").lower()

        if jogador2 not in opcoes:
            print('Escolha inválida')
            continue

        if jogador1 == jogador2:
            print("Empate!\n")
        
        elif jogador1 == 'pedra' and jogador2 == 'tesoura':
            print("Jogador 1 venceu!\n")
        
        elif jogador1 == 'papel' and jogador2 == 'pedra':
            print("Jogador 1 venceu!\n")
        
        elif jogador1 == 'tesoura' and jogador2 == 'papel':
            print("Jogador 1 venceu!\n")
        
        else:
            print("Jogador 2 venceu!\n")
        print(f"Jogador 1 = {jogador1}")
        print(f"Jogador 2 = {jogador2}\n")

        print('Deseja jogar novamente?')
        print("S - Sim")
        print('N - Não (Voltar ao menu)')
        verifica_jogar_novamente = input("Digite (S/n): ").lower()
        if verifica_jogar_novamente != "s":
            break


           


   




    