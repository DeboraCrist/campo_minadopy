from campo_minado import CampoMinado

def main():
    print("Bem-vindo ao Campo Minado!")

    while True:
        nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")
        if nivel.isdigit() and int(nivel) in CampoMinado.NIVEIS:
            nivel = int(nivel)
            break
        else:
            print("Nível de dificuldade inválido. Escolha 1, 2 ou 3.")

    jogo = CampoMinado(nivel)

    while True:
        for row in jogo.tabuleiro:
            print(" ".join(row))

        acao = input("Escolha uma ação (D para descobrir, B para colocar bandeira, R para remover bandeira, Q para sair): ").upper()

        if acao == 'Q':
            print("Saindo do jogo.")
            break
        elif acao == 'D':
            x = int(input("Digite a coordenada X: "))
            y = int(input("Digite a coordenada Y: "))
            jogo.descobrir_zona(x, y)
            if jogo.jogo_encerrado:
                print("Você perdeu!")
                jogo.revelar_bombas()
                for row in jogo.tabuleiro:
                    print(" ".join(row))
                break
            elif jogo.jogo_vencido:
                print("Parabéns! Você venceu!")
                for row in jogo.tabuleiro:
                    print(" ".join(row))
                break
        elif acao == 'B':
            x = int(input("Digite a coordenada X para colocar a bandeira: "))
            y = int(input("Digite a coordenada Y para colocar a bandeira: "))
            jogo.colocar_bandeira(x, y)
        elif acao == 'R':
            x = int(input("Digite a coordenada X para remover a bandeira: "))
            y = int(input("Digite a coordenada Y para remover a bandeira: "))
            jogo.remover_bandeira(x, y)
        else:
            print("Ação inválida. Escolha D para descobrir, B para colocar bandeira, R para remover bandeira ou Q para sair.")

if __name__ == "__main__":
    main()