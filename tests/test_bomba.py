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

    def test_colocar_bombas_nivel2(self):
        jogo = CampoMinado(2)
        bombas_colocadas = sum(sum(1 for bomba in linha if bomba) for linha in jogo.bombas)
        self.assertEqual(bombas_colocadas, jogo.num_bombas)

    def test_colocar_bombas_nivel3(self):
        jogo = CampoMinado(3)
        bombas_colocadas = sum(sum(1 for bomba in linha if bomba) for linha in jogo.bombas)
        self.assertEqual(bombas_colocadas, jogo.num_bombas)

    def test_revelarBombas(self):
        self.jogo.bombas[0][0] = True
        self.jogo.revelar_bombas()
        self.assertEqual(self.jogo.tabuleiro[0][0], 'B')

    def test_revelarBombas_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.revelar_bombas()
        self.assertEqual(jogo.tabuleiro[0][0], 'B')

    def test_revelarBombas_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.revelar_bombas()
        self.assertEqual(jogo.tabuleiro[0][0], 'B')

    def test_derrotaAoDescobrirBomba(self):
        self. jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.jogo_encerrado, True)

    def test_derrotaAoDescobrirBomba_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_encerrado, True)

    def test_derrotaAoDescobrirBomba_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_encerrado, True)

    def test_jogoNaoVencidoAposDescobrirBomba(self):
        self.jogo.tabuleiro[0][0] = 'B'
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_jogoNaoVencidoAposDescobrirBomba_nivel2(self):
        jogo = CampoMinado(2)
        jogo.tabuleiro[0][0] = 'B'
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_vencido, False)

    def test_jogoNaoVencidoAposDescobrirBomba_nivel3(self):
        jogo = CampoMinado(3)
        jogo.tabuleiro[0][0] = 'B'
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_vencido, False)
    
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

    def test_bombasNaoPodemSerColocadasNaPrimeiraZonaRevelada_nivel2(self):
        jogo = CampoMinado(2)
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(1, 1)
        self.assertNotEqual(self.jogo.tabuleiro[1][1], 'B')

    def test_bombasNaoPodemSerColocadasNaPrimeiraZonaRevelada_nivel3(self):
        jogo = CampoMinado(3)
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(1, 1)
        self.assertNotEqual(self.jogo.tabuleiro[1][1], 'B')

    def test_bombas_nao_podem_ser_colocadas_na_primeira_zona_revelada_outro(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 1)
        self.assertNotEqual(self.jogo.tabuleiro[0][1], 'B')

    def test_bombas_nao_podem_ser_colocadas_na_primeira_zona_revelada_outro_nivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        jogo.descobrir_zona(0, 1)
        self.assertNotEqual(jogo.tabuleiro[0][1], 'B')

    def test_bombas_nao_podem_ser_colocadas_na_primeira_zona_revelada_outro_nivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        jogo.descobrir_zona(0, 1)
        self.assertNotEqual(jogo.tabuleiro[0][1], 'B')

    def test_descobrir_celula_com_bomba_na_primeira_jogada(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.jogo_encerrado, True)

    def test_descobrir_celula_com_bomba_na_primeira_jogada_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_encerrado, True)

    def test_descobrir_celula_com_bomba_na_primeira_jogada_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_encerrado, True)

    def test_descobrir_celula_com_bomba_na_primeira_jogada_false(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_descobrir_celula_com_bomba_na_primeira_jogada_false_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_vencido, False)

    def test_descobrir_celula_com_bomba_na_primeira_jogada_false_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.jogo_vencido, False)

    def test_vencer_jogo_com_bandeira_na_ultima_bomba_corretamente(self):
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.jogo.verificar_vitoria()
        self.assertTrue(self.jogo.jogo_vencido)

    def test_vencer_jogo_com_bandeira_na_ultima_bomba_corretamente_nivel2(self):
        jogo = CampoMinado(2)
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    jogo.colocar_bandeira(x, y)
        jogo.verificar_vitoria()
        self.assertTrue(jogo.jogo_vencido)

    def test_vencer_jogo_com_bandeira_na_ultima_bomba_corretamente_nivel3(self):
        jogo = CampoMinado(3)
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    jogo.colocar_bandeira(x, y)
        jogo.verificar_vitoria()
        self.assertTrue(jogo.jogo_vencido)

    def test_revelar_bombas_apos_derrota(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.revelar_bombas()
        self.assertEqual(self.jogo.tabuleiro[0][0], 'B')

    def test_revelar_bombas_apos_derrota_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        jogo.revelar_bombas()
        self.assertEqual(jogo.tabuleiro[0][0], 'B')

    def test_revelar_bombas_apos_derrota_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        jogo.revelar_bombas()
        self.assertEqual(jogo.tabuleiro[0][0], 'B')
    
    def test_colocar_mais_bandeiras_do_que_bombas_nao_vence_o_jogo(self):
        self.jogo.bandeiras_colocadas = self.jogo.num_bombas + 1
        self.jogo.verificar_vitoria()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_colocar_mais_bandeiras_do_que_bombas_nao_vence_o_jogo_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bandeiras_colocadas = jogo.num_bombas + 1
        jogo.verificar_vitoria()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_colocar_mais_bandeiras_do_que_bombas_nao_vence_o_jogo_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bandeiras_colocadas = jogo.num_bombas + 1
        jogo.verificar_vitoria()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_descobrir_zona_com_bandeira_nao_altera_o_tabuleiro(self):
        self.jogo.bombas[0][0] = True
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], 'F')

    def test_descobrir_zona_com_bandeira_nao_altera_o_tabuleiro_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.colocar_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], 'F')

    def test_descobrir_zona_com_bandeira_nao_altera_o_tabuleiro_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.colocar_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], 'F')

    def test_vitoria_descobrir_todas_as_zonas_limpo_sem_bombas_adjacentes(self):
        self.jogo.bombas = [[False] * self.jogo.linhas for _ in range(self.jogo.colunas)]
        self.jogo.descobrir_zona(0, 0)
        self.jogo.verificar_vitoria()
        self.assertEqual(self.jogo.jogo_vencido, True)

    def test_bomba_explode_inicio(self):
        self.jogo.bombas = [
            [False, True, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False]
        ]
        self.jogo.descobrir_zona(0, 0)
        self.jogo.descobrir_zona(0, 1)
        self.assertTrue(self.jogo.jogo_encerrado)
    
    def test_bomba_explode_meio(self):
        self.jogo.bombas = [
            [False, False, False, False, False, False, False, False],
            [False, True, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, True, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False]
        ]
        self.jogo.descobrir_zona(0, 0)
        self.jogo.descobrir_zona(5, 5)
        self.assertFalse(self.jogo.jogo_vencido)

    def test_bomba_explode_fim(self):
        self.jogo.bombas = [
            [False, False, False, False, False, False, False, False],
            [False, True, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, True]
        ]
        self.jogo.descobrir_zona(0, 0)
        self.jogo.descobrir_zona(7, 7)
        self.assertTrue(self.jogo.jogo_encerrado)

    def test_realocacao_de_bombas_apos_primeira_jogada(self):
        self.jogo.bombas[0][0] = True
        self.jogo.realizar_primeira_jogada(0, 0)
        bombas_realocadas = 0
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if self.jogo.bombas[x][y]:
                    bombas_realocadas += 1
        self.assertEqual(bombas_realocadas, self.jogo.num_bombas)

    def test_realocacao_de_bombas_apos_primeira_jogada_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.realizar_primeira_jogada(0, 0)
        bombas_realocadas = 0
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    bombas_realocadas += 1
        self.assertEqual(bombas_realocadas, jogo.num_bombas)

    def test_realocacao_de_bombas_apos_primeira_jogada_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.realizar_primeira_jogada(0, 0)
        bombas_realocadas = 0
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    bombas_realocadas += 1
        self.assertEqual(bombas_realocadas, jogo.num_bombas)
        
if __name__ == '__main__':
    unittest.main()
    