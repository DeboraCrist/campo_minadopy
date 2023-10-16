from sys import exit
from campo_minado import CampoMinado

def main():
    print("Bem-vindo ao Campo Minado!")

    while True:
        jogo = start_game()
        primeira_jogada = True

        while True:
            for row in jogo.tabuleiro:
                print(" ".join(row))

            if primeira_jogada: 
                acao = input("Escolha uma ação para a primeira jogada (D para descobrir, B para colocar bandeira, H para histórico, Q para sair ou N para reiniciar): ").upper()
            else:
                acao = input("Escolha uma ação (D para descobrir, B para colocar bandeira, R para remover bandeira, H para histórico, Q para sair ou N para reiniciar): ").upper()

            if acao == 'Q':
                jogo.sair()
                return  
            elif acao == 'N':
                print("Reiniciando o jogo.")
                break
            elif acao == 'H':
                exibir_historico()
            elif acao == 'D': 
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
                if jogo.jogo_encerrado: 
                    print("Você perdeu!")
                    jogo.revelar_bombas()
                    for row in jogo.tabuleiro:
                        print(" ".join(row))
                    jogo.guardar_resultado()
                    if play_again():
                        break
                    else:
                        return
                elif jogo.jogo_vencido: 
                    print("Parabéns! Você venceu!")
                    for row in jogo.tabuleiro:
                        print(" ".join(row))
                    jogo.guardar_resultado()
                    if play_again():
                        break
                    else:
                        return
            elif acao == 'B': 
                x = int(input("Digite a coordenada X para colocar a bandeira: "))
                y = int(input("Digite a coordenada Y para colocar a bandeira: "))
                try:
                    jogo.colocar_bandeira(x, y)
                except ValueError as e:
                    print(e)
            elif acao == 'R':
                x = int(input("Digite a coordenada X para remover a bandeira: "))
                y = int(input("Digite a coordenada Y para remover a bandeira: "))
                jogo.remover_bandeira(x, y)
            else: 
                print("Ação inválida. Escolha D para descobrir, B para colocar bandeira, R para remover bandeira, H para histórico, N para reiniciar ou Q para sair.")

def play_again():
    while True:
        choice = input("Deseja jogar novamente? (S para Sim, N para Não): ").strip().lower() 
        if choice == 's':
            return True
        elif choice == 'n':
            return False
        else:
            print("Opção inválida. Escolha S para Sim ou N para Não.")

def start_game():
    while True: 
        nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")
        if nivel.isdigit() and int(nivel) in CampoMinado.NIVEIS:
            nivel = int(nivel)
            return CampoMinado(nivel)
        else: 
            print("Nível de dificuldade inválido. Escolha 1, 2 ou 3.")

def exibir_historico():
    try:
        with open('historico.txt', 'r') as arquivo:
            historico = arquivo.read()
            print("Histórico de Partidas:\n")
            print(historico)
    except FileNotFoundError:
        print("Nenhum histórico disponível.")


if __name__ == "__main__":
    main()

