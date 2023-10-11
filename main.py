from sys import exit
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

    while True: 
        jogo = CampoMinado(nivel)
        continue_game = True  

        while continue_game:  
            for row in jogo.tabuleiro:
                print(" ".join(row))

            acao = input("Escolha uma ação (D para descobrir, B para colocar bandeira, R para remover bandeira, Q para sair ou N para reiniciar): ").upper()

            if acao == 'Q':
                jogo.sair()
                continue_game = False  # Set the flag to False instead of raising SystemExit
            elif acao == 'N':
                print("Reiniciando o jogo.")
                break  
            elif acao == 'D':
                x = int(input("Digite a coordenada X: "))
                y = int(input("Digite a coordenada Y: "))
                try:
                    jogo.descobrir_zona(x, y)
                except ValueError as e:
                    print(e) 
                jogo.descobrir_zona(x, y)
                if jogo.jogo_encerrado:
                    print("Você perdeu!")
                    jogo.revelar_bombas()
                    for row in jogo.tabuleiro:
                        print(" ".join(row))
                    continue_game = False
                elif jogo.jogo_vencido:
                    print("Parabéns! Você venceu!")
                    for row in jogo.tabuleiro:
                        print(" ".join(row))
                    continue_game = False
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
                print("Ação inválida. Escolha D para descobrir, B para colocar bandeira, R for remover bandeira, N para reiniciar ou Q para sair.")

if __name__ == "__main__":
    main()
