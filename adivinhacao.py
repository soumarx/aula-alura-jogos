import random
import time


def jogar():
    print("Bem vindo ao jogo de Adivinhação!")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    dificuldade = int(input("Defina a Dificuldade: "))

    time.sleep(2)

    if dificuldade == 1:
        tentativas = 20
    elif dificuldade == 2:
        tentativas = 10
    elif dificuldade == 3:
        tentativas = 5
    else:
        print("Você não digitou um valor válido!")

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))

        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 101:
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            time.sleep(2)
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    time.sleep(2)
    print("Fim do jogo! O número secreto era {}".format(numero_secreto))


if __name__ == "__main__":
    jogar()
