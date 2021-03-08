
import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    total_de_tentativas = 6

    print(letras_acertadas)

    while (not acertou and not enforcou and palavra_secreta != ""):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Erro {} de {}".format(erros, total_de_tentativas))

        enforcou = erros == total_de_tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if (acertou):
            imprime_mensagem_vencedor()
        elif(enforcou):
            imprime_mensagem_perdedor()

    print("Fim do jogo")


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("jogos/palavras.txt", "r")
    palavras = []
    palavra_secreta = ""

    with open("jogos/palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def imprime_mensagem_vencedor():
    print("Você ganhou!")


def imprime_mensagem_perdedor():
    print("Você perdeu!")


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


if (__name__ == "__main__"):
    jogar()
