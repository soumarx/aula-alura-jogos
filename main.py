print("Bem vindo ao jogo de Adivinhação!")

numero_secreto = 45

chute = input("Digite um numero:")

print("Você digitou: ", chute)

if numero_secreto == chute:
    print("Você acertou!")
else:
    print("Você errou!")
