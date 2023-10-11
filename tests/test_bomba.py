import unittest
from campo_minado import CampoMinado

class TestBomba(unittest.TestCase):

    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_num_bombas_nivel_facil(self):
        self.assertEqual(self.jogo.num_bombas, 10)

    def test_num_bombas_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.num_bombas, 30)
    
    def test_num_bombas_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.num_bombas, 100)

    def test_colocar_bombas(self):
        bombas_colocadas = sum(sum(1 for bomba in linha if bomba) for linha in self.jogo.bombas)
        self.assertEqual(bombas_colocadas, self.jogo.num_bombas)

    def test_revelarBombas(self):
        self.jogo.bombas[0][0] = True
        self.jogo.revelar_bombas()
        self.assertEqual(self.jogo.tabuleiro[0][0], 'B')

    def test_derrotaAoDescobrirBomba(self):
        self. jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.jogo_encerrado, True)

    def test_jogoNaoVencidoAposDescobrirBomba(self):
        self.jogo.tabuleiro[0][0] = 'B'
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.jogo_vencido, False)
    
    def test_distribuicao_aleatoria_bombas_nivel_1(self):
        bombas_encontradas_em_execucoes = []

        # Execute o método colocar_bombas várias vezes e armazene as coordenadas das bombas
        for _ in range(10):  
            self.jogo.inicializar_tabuleiro()
            self.jogo.colocar_bombas()
            bombas_encontradas_em_execucoes.append(self.jogo.bombas)

        # Verifique se as coordenadas das bombas variam entre as execuções
        for i in range(len(bombas_encontradas_em_execucoes) - 1):
            self.assertNotEqual(bombas_encontradas_em_execucoes[i], bombas_encontradas_em_execucoes[i + 1])
    
    def test_distribuicao_aleatoria_bombas_nivel_2(self):
        jogo = CampoMinado(2)
        bombas_encontradas_em_execucoes = []
        for _ in range(10):  
            jogo.inicializar_tabuleiro()
            jogo.colocar_bombas()
            bombas_encontradas_em_execucoes.append(jogo.bombas)

        for i in range(len(bombas_encontradas_em_execucoes) - 1):
            self.assertNotEqual(bombas_encontradas_em_execucoes[i], bombas_encontradas_em_execucoes[i + 1])

    def test_distribuicao_aleatoria_bombas_nivel_3(self):
        jogo = CampoMinado(3)
        bombas_encontradas_em_execucoes = []
        for _ in range(10):  
            jogo.inicializar_tabuleiro()
            jogo.colocar_bombas()
            bombas_encontradas_em_execucoes.append(jogo.bombas)

        for i in range(len(bombas_encontradas_em_execucoes) - 1):
            self.assertNotEqual(bombas_encontradas_em_execucoes[i], bombas_encontradas_em_execucoes[i + 1])

    def test_bombasNaoPodemSerColocadasNaPrimeiraZonaRevelada(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(1, 1)
        self.assertNotEqual(self.jogo.tabuleiro[1][1], 'B')

    def test_bombas_nao_podem_ser_colocadas_na_primeira_zona_revelada_outro(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 1)
        self.assertNotEqual(self.jogo.tabuleiro[0][1], 'B')

    def test_descobrir_celula_com_bomba_na_primeira_jogada(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.jogo_encerrado, True)
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_vencer_jogo_com_bandeira_na_ultima_bomba_corretamente(self):
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.jogo.verificar_vitoria()
        self.assertTrue(self.jogo.jogo_vencido)

    def test_revelar_bombas_apos_derrota(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.revelar_bombas()
        self.assertEqual(self.jogo.tabuleiro[0][0], 'B')
    
    def test_colocar_mais_bandeiras_do_que_bombas_nao_vence_o_jogo(self):
        self.jogo.bandeiras_colocadas = self.jogo.num_bombas + 1
        self.jogo.verificar_vitoria()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_descobrir_zona_com_bandeira_nao_altera_o_tabuleiro(self):
        self.jogo.bombas[0][0] = True
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], 'F')

    def test_vitoria_descobrir_todas_as_zonas_limpo_sem_bombas_adjacentes(self):
        self.jogo.bombas = [[False] * self.jogo.tamanho for _ in range(self.jogo.tamanho)]
        self.jogo.descobrir_zona(0, 0)
        self.jogo.verificar_vitoria()
        self.assertEqual(self.jogo.jogo_vencido, True)

if __name__ == '__main__':
    unittest.main()