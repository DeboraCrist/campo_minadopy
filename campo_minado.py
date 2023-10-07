import random

class CampoMinado:
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
        if self.nivel == 1:
            self.tamanho = 8
            self.num_bombas = 10
        elif self.nivel == 2:
            self.tamanho = 10
            self.num_bombas = 30
        elif self.nivel == 3:
            self.tamanho = 24
            self.num_bombas = 100
        else:
            raise ValueError("Nível de dificuldade inválido")

        self.tabuleiro = [['-' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.bombas = [[False for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.colocar_bombas()

    def colocar_bombas(self):
        bombas_restantes = self.num_bombas
        while bombas_restantes > 0:
            x = random.randint(0, self.tamanho - 1)
            y = random.randint(0, self.tamanho - 1)
            if not self.bombas[x][y]:
                self.bombas[x][y] = True
                bombas_restantes -= 1

    def reiniciar_jogo(self):
        self.inicializar_tabuleiro()
        self.jogo_encerrado = False
        self.jogo_vencido = False
        self.bandeiras_colocadas = 0
