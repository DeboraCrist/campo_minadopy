import random

class CampoMinado:
    NIVEIS = {
        1: {'tamanho': 8, 'num_bombas': 10},
        2: {'tamanho': 10, 'num_bombas': 30},
        3: {'tamanho': 24, 'num_bombas': 100}
    }

    def __init__(self, nivel):
        self.nivel = nivel
        self.tabuleiro = []
        self.bombas = []
        self.tamanho = 0
        self.num_bombas = 0
        self.jogo_encerrado = False
        self.jogo_vencido = False
        self.bandeiras_colocadas = 0
        self.inicializar_tabuleiro()

    def inicializar_tabuleiro(self):
        if self.nivel not in self.NIVEIS:
            raise ValueError("Nível de dificuldade inválido")

        nivel_info = self.NIVEIS[self.nivel]
        self.tamanho = nivel_info['tamanho']
        self.num_bombas = nivel_info['num_bombas']

        self.tabuleiro = [['-' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.bombas = [[False for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.colocar_bombas()

    def descobrir_zona(self, x, y):
        if not self.jogo_encerrado and not self.jogo_vencido:
            if self.bombas[x][y]:
                self.jogo_encerrado = True
                self.mostrar_bombas()
            else:
                self.descobrir_vizinhanca(x, y)
                if self.venceu_jogo():
                    self.jogo_vencido = True

    def descobrir_vizinhanca(self, x, y):
        if 0 <= x < self.tamanho and 0 <= y < self.tamanho and self.tabuleiro[x][y] == '-':
            bombas_adjacentes = self.contar_bombas_adjacentes(x, y)
            self.tabuleiro[x][y] = str(bombas_adjacentes) if bombas_adjacentes > 0 else ' '
            if bombas_adjacentes == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        self.descobrir_vizinhanca(x + dx, y + dy)
                    
    def colocar_bombas(self):
        bombas_restantes = self.num_bombas
        while bombas_restantes > 0:
            x = random.randint(0, self.tamanho - 1)
            y = random.randint(0, self.tamanho - 1)
            if not self.bombas[x][y]:
                self.bombas[x][y] = True
                bombas_restantes -= 1

    def contar_bombas_adjacentes(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < self.tamanho and 0 <= y + dy < self.tamanho and self.bombas[x + dx][y + dy]:
                    count += 1
        return count

    def revelar_bombas(self):
        for x in range(self.tamanho):
            for y in range(self.tamanho):
                if self.bombas[x][y]:
                    self.tabuleiro[x][y] = 'B'

    def colocar_bandeira(self, x, y):
        if not self.jogo_encerrado and not self.jogo_vencido:
            if 0 <= x < self.tamanho and 0 <= y < self.tamanho and self.tabuleiro[x][y] == '-':
                self.tabuleiro[x][y] = 'F'
                self.bandeiras_colocadas += 1

    def remover_bandeira(self, x, y):
        if not self.jogo_encerrado and not self.jogo_vencido:
            if 0 <= x < self.tamanho and 0 <= y < self.tamanho and self.tabuleiro[x][y] == 'F':
                self.tabuleiro[x][y] = '-'
                self.bandeiras_colocadas -= 1

    def venceu_jogo(self):
        for x in range(self.tamanho):
            for y in range(self.tamanho):
                if not self.bombas[x][y] and self.tabuleiro[x][y] == '-':
                    return False
        return True

    def reiniciar_jogo(self):
        self.inicializar_tabuleiro()
        self.jogo_encerrado = False
        self.jogo_vencido = False
        self.bandeiras_colocadas = 0
