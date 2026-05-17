import random

def jogar():
    print("Faça uma escolha!")
    print()


    opcoes = ['pedra', 'papel', 'tesoura']

    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    computador = random.choice(opcoes)

    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif jogador == 'pedra' and computador == 'tesoura':
        print("Você venceu!")
    elif jogador == 'papel' and computador == 'pedra':
        print("Você venceu!")
    elif jogador == 'tesoura' and computador == 'papel':
        print("Você venceu!")
    else:
        print("Computador venceu!")


    