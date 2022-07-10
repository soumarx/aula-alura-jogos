import adivinhacao
import forca

print("Escolha o seu Jogo!")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual Jogo?: "))
jogar_adivinhar = adivinhacao == 1
jogo_forca = forca == 2

if jogo == 1:
    print("Jogando forca...")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()
else:
    print("Você não selecionou o jogo")
