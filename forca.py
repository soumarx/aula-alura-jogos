import random


def jogar():

    imprime_mensagem_abertura_forca()
    palavra_secreta = carrega_palavras()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    # variáveis
    enforcou = False
    acertou = False
    erros = 0
    tentativas = 3

    print(letras_acertadas)
    print("Você terá {} tentativas".format(len(letras_acertadas) + tentativas))

    while not acertou and not enforcou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == len(letras_acertadas) + tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura_forca():
    print("Bem vindo ao jogo de Forca!")


def carrega_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Você ganhou! Fim do jogo!")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu! Fim do jogo!")
    print("A palavra era {}".format(palavra_secreta))


if __name__ == "__main__":
    jogar()
