import sys

from campo_minado import CampoMinado

def mostrar_tabuleiro(tabuleiro):
    print("Tabuleiro:")
    for linha in tabuleiro:
        for celula in linha:
            print(celula, end=" ")
        print()

def main():
    print("Bem-vindo ao Campo Minado!")
    tamanho = int(input("Informe o tamanho do tabuleiro: "))
    num_bombas = int(input("Informe o número de bombas: "))

    jogo = CampoMinado(tamanho, num_bombas)

    while not jogo.jogo_encerrado:
        mostrar_tabuleiro(jogo.tabuleiro)

        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        acao = input("Escolha uma ação (D para descobrir, F para colocar bandeira, R para remover bandeira): ")

        if acao.upper() == "D":
            jogo.descobrir_zona(linha, coluna)
        elif acao.upper() == "F":
            jogo.colocar_bandeira(linha, coluna)
        elif acao.upper() == "R":
            jogo.remover_bandeira(linha, coluna)
        else:
            print("Ação inválida. Use D, F ou R.")

    if jogo.jogo_encerrado and not jogo.is_descoberta(0, 0):
        print("Você perdeu! Fim de jogo.")
        mostrar_tabuleiro(jogo.tabuleiro)
    else:
        print("Parabéns! Você venceu!")

if __name__ == "__main__":
    main()
