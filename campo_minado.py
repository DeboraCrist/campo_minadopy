import datetime
import random

class CampoMinado:
    NIVEIS = {
        1: {'linhas': 8, 'colunas': 8, 'num_bombas': 10},
        2: {'linhas': 10, 'colunas': 16, 'num_bombas': 30},
        3: {'linhas': 24, 'colunas': 24, 'num_bombas': 100}
    }

    def __init__(self, nivel):
        self.nivel = nivel
        self.linhas = 0
        self.colunas = 0
        self.num_bombas = 0
        self.tabuleiro = []
        self.bombas = []
        self.jogo_encerrado = False
        self.jogo_vencido = False
        self.bandeiras_colocadas = 0
        self.resultados = []
        self.end_time = None
        self.start_time = datetime.datetime.now() 
        self.inicializar_tabuleiro()

    def realizar_primeira_jogada(self, x, y):
        if not self.bombas[x][y]:
            self.descobrir_vizinhanca(x, y)
            self.start_time = datetime.datetime.now()
        else:
            self.inicializar_tabuleiro()
            self.realizar_primeira_jogada(x, y)

    def inicializar_tabuleiro(self):
        if self.nivel not in self.NIVEIS:
            raise ValueError("Nível de dificuldade inválido")

        nivel_info = self.NIVEIS[self.nivel]
        self.linhas = nivel_info['linhas']
        self.colunas = nivel_info['colunas']
        self.num_bombas = nivel_info['num_bombas']

        self.tabuleiro = [['-' for _ in range(self.colunas)] for _ in range(self.linhas)]
        self.bombas = [[False for _ in range(self.colunas)] for _ in range(self.linhas)]
        self.colocar_bombas()

    def descobrir_zona(self, x, y):
        if not self.jogo_encerrado and not self.jogo_vencido:
            if self.tabuleiro[x][y] == 'F':
                print("Ação inválida. Você deve remover a bandeira antes de descobrir a zona.")
                return
            if self.tabuleiro[x][y] == ' ' or self.tabuleiro[x][y].isdigit():
                return
            if self.bombas[x][y]:
                self.jogo_encerrado = True
                self.revelar_bombas()
            else:
                self.descobrir_vizinhanca(x, y)
                if self.venceu_jogo():
                    self.jogo_vencido = True
            
    def descobrir_vizinhanca(self, x, y):
        if 0 <= x < self.linhas and 0 <= y < self.colunas and self.tabuleiro[x][y] == '-':
            bombas_adjacentes = self.contar_bombas_adjacentes(x, y)
            self.tabuleiro[x][y] = str(bombas_adjacentes) if bombas_adjacentes > 0 else ' '
            if bombas_adjacentes == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        self.descobrir_vizinhanca(x + dx, y + dy)

    def colocar_bombas(self):
        bombas_restantes = self.num_bombas
        primeiro_revelado = False
        x_primeiro_revelado = 0
        y_primeiro_revelado = 0

        while bombas_restantes > 0 and not self.jogo_encerrado:
            x = random.randint(0, self.linhas - 1)
            y = random.randint(0, self.colunas - 1)

            if not primeiro_revelado:
                if self.tabuleiro[x][y] != '-':
                    continue
                primeiro_revelado = True
                x_primeiro_revelado = x
                y_primeiro_revelado = y
                continue 

            if x == x_primeiro_revelado and y == y_primeiro_revelado:
                continue 

            if not self.bombas[x][y]:
                self.bombas[x][y] = True
                bombas_restantes -= 1
                # print(f"Bomba colocada em ({x}, {y})") 
    
    def contar_bombas_adjacentes(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < self.linhas and 0 <= y + dy < self.colunas:
                    if self.bombas[x + dx][y + dy]:
                        count += 1
        return count

    def revelar_bombas(self):
        for x in range(self.linhas):
            for y in range(self.colunas):
                if self.bombas[x][y]:
                    self.tabuleiro[x][y] = 'B'

    def colocar_bandeira(self, x, y):
        if not self.jogo_encerrado and not self.jogo_vencido:
            if 0 <= x < self.linhas and 0 <= y < self.colunas:
                if self.tabuleiro[x][y] == '-' and self.bandeiras_colocadas < self.num_bombas:
                    self.tabuleiro[x][y] = 'F'
                    self.bandeiras_colocadas += 1

                    if self.bandeiras_colocadas == self.num_bombas:
                        self.verificar_vitoria()
                elif self.bandeiras_colocadas == self.num_bombas:
                    print("Ação inválida. Você não pode colocar mais bandeiras do que o número de bombas.")
                elif self.tabuleiro[x][y] == 'F':
                    self.tabuleiro[x][y] = '-'
                    self.bandeiras_colocadas -= 1
                else:
                    print("Ação inválida. Você não pode colocar uma bandeira em uma zona já revelada.")
            else:
                print("Posição fora do tabuleiro.") 

    def verificar_vitoria(self):
        if self.bandeiras_colocadas == self.num_bombas:
            for x in range(self.linhas):
                for y in range(self.colunas):
                    if self.bombas[x][y] and self.tabuleiro[x][y] != 'F':
                        return
            self.end_time = datetime.datetime.now()
            self.jogo_vencido = True

    def remover_bandeira(self, x, y):
        if not self.jogo_encerrado and not self.jogo_vencido:
            if 0 <= x < self.linhas and 0 <= y < self.colunas and self.tabuleiro[x][y] == 'F':
                self.tabuleiro[x][y] = '-'
                self.bandeiras_colocadas -= 1
                self.guardar_resultado()

    def venceu_jogo(self):
        for x in range(self.linhas):
            for y in range(self.colunas):
                if not self.bombas[x][y] and self.tabuleiro[x][y] == '-':
                    return False
        return True

    def reiniciar_jogo(self):
        self.inicializar_tabuleiro()
        self.jogo_encerrado = False
        self.jogo_vencido = False
        self.bandeiras_colocadas = 0
        self.start_time = None
        self.end_time = None
        
    def guardar_resultado(self, score=""):
        if self.jogo_vencido:
            resultado = f"Vitória\n{score}"
        elif self.jogo_encerrado:
            resultado = f"Derrota\n{score}"
        else:
            resultado = "Jogo não encerrado"

        data_hora = datetime.datetime.now()
        resultado_str = f"Data e Hora: {data_hora}\nNível: {self.nivel}\nResultado: {resultado}\n"

        with open('historico.txt', 'a') as arquivo:
            arquivo.write(resultado_str + "\n")

    def obter_resultados(self):
        return self.resultados

    def sair(self):
        print("Saindo do jogo.")
        self.jogo_encerrado = True

