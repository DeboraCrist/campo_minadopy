from sys import exit
from campo_minado import CampoMinado

def main():
    print("Bem-vindo ao Campo Minado!") #falta

    while True:
        jogo = start_game()
        primeira_jogada = True

        while True:
            for row in jogo.tabuleiro:
                print(" ".join(row))

            if primeira_jogada: #falta
                acao = input("Escolha uma ação para a primeira jogada (D para descobrir, B para colocar bandeira, Q para sair ou N para reiniciar): ").upper()
            else:
                acao = input("Escolha uma ação (D para descobrir, B para colocar bandeira, R para remover bandeira, Q para sair ou N para reiniciar): ").upper()

            if acao == 'Q':
                jogo.sair()
                break
            elif acao == 'N': #falta
                print("Reiniciando o jogo.")
                break
            elif acao == 'D': #falta
                x = int(input("Digite a coordenada X: "))
                y = int(input("Digite a coordenada Y: "))
                if primeira_jogada:
                    try:
                        jogo.realizar_primeira_jogada(x, y)
                        primeira_jogada = False
                    except ValueError as e:
                        print(e)
                else:
                    try:
                        jogo.descobrir_zona(x, y)
                    except ValueError as e:
                        print(e)
                        continue
                if jogo.jogo_encerrado: #falta
                    print("Você perdeu!")
                    jogo.revelar_bombas()
                    for row in jogo.tabuleiro:
                        print(" ".join(row))
                    if play_again():
                        break
                    else:
                        return
                elif jogo.jogo_vencido: #falta
                    print("Parabéns! Você venceu!")
                    for row in jogo.tabuleiro:
                        print(" ".join(row))
                    if play_again():
                        break
                    else:
                        return
            elif acao == 'B': #falta
                x = int(input("Digite a coordenada X para colocar a bandeira: "))
                y = int(input("Digite a coordenada Y para colocar a bandeira: "))
                try:
                    jogo.colocar_bandeira(x, y)
                except ValueError as e:
                    print(e)
            elif acao == 'R': #falta
                x = int(input("Digite a coordenada X para remover a bandeira: "))
                y = int(input("Digite a coordenada Y para remover a bandeira: "))
                jogo.remover_bandeira(x, y)
            else: #falta
                print("Ação inválida. Escolha D para descobrir, B para colocar bandeira, R para remover bandeira, N para reiniciar ou Q para sair.")

def play_again():
    while True:
        choice = input("Deseja jogar novamente? (S para Sim, N para Não): ").strip().lower() #falta
        if choice == 's':
            return True
        elif choice == 'n':
            return False
        else:
            print("Opção inválida. Escolha S para Sim ou N para Não.") #falta

def start_game():
    while True: #falta
        nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")
        if nivel.isdigit() and int(nivel) in CampoMinado.NIVEIS:
            nivel = int(nivel)
            return CampoMinado(nivel)
        else: #falta
            print("Nível de dificuldade inválido. Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
