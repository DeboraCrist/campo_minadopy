import datetime
import random
import unittest
from campo_minado import CampoMinado
from unittest.mock import patch

class TestCampoMinado(unittest.TestCase):

    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_nivel_facil(self):
        self.assertEqual(self.jogo.nivel, 1)

    def test_linhas_nivel_facil(self):
        self.assertEqual(self.jogo.linhas, 8)

    def test_colunas_nivel_facil(self):
        self.assertEqual(self.jogo.colunas, 8)

    def test_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.nivel, 2)

    def test_linhas_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.linhas, 10)

    def test_colunas_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.colunas, 16)

    def test_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.nivel, 3)

    def test_linhas_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.linhas, 24)

    def test_colunas_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.colunas, 24)

    def test_jogoNaoEncerradoNaInicializacao(self):
        self.assertEqual(self.jogo.jogo_encerrado, False)

    def test_tabuleiroInicializadoComHifens(self):
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_descobrirZona(self):
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_JogoNaoEstaEmEstadoInicial(self):
        self.jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_sair_marca_jogo_como_encerrado(self):
        self.jogo.sair()
        self.assertTrue(self.jogo.jogo_encerrado)

    def test_sair_nao_afeta_resultados(self):
        self.jogo.guardar_resultado()  
        self.jogo.sair()
        self.assertNotEqual(self.jogo.resultados, [])

    def test_sair_apos_vitoria(self):
        self.jogo.jogo_vencido = True
        self.jogo.sair()
        self.assertTrue(self.jogo.jogo_vencido)

    def test_descobrir_vizinhanca_celula_vazia(self):
        self.jogo.bombas = [[False] * 8 for _ in range(8)]
        self.jogo.descobrir_vizinhanca(4, 4) 
        tabuleiro_esperado = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        self.assertEqual(self.jogo.tabuleiro, tabuleiro_esperado)

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com4(self):
        self.jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [False, True, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '5')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com4(self):
        self.jogo.bombas = [
            [False, True, False],
            [True, False, True],
            [False, True, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '4')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com3(self):
        self.jogo.bombas = [
            [False, False, False],
            [True, False, True],
            [False, True, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '3')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com1(self):
        self.jogo.bombas = [
            [True, False, False],
            [False, False, False],
            [False, False, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '1')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com1(self):
        self.jogo.bombas = [
            [True, False, True],
            [False, False, False],
            [False, False, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '2')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com7(self):
        self.jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, True, True]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '7')    
    
    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com6(self):
        self.jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, False, True]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '6')    

    def test_vencer_jogo(self):
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if not self.jogo.bombas[x][y]:
                    self.jogo.descobrir_zona(x, y)
        self.assertTrue(self.jogo.jogo_vencido)

    def test_descobrir_zona_com_jogo_encerrado(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.descobrir_zona(1, 1)
        self.assertTrue(self.jogo.jogo_encerrado)

    def test_descobrir_zona_com_jogo_vencido(self):
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if not self.jogo.bombas[x][y]:
                    self.jogo.descobrir_zona(x, y)
        self.assertTrue(self.jogo.jogo_vencido)
    
    def test_realizar_primeira_jogada_celula_segura(self):
        x, y = 0, 0 
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(self.jogo.bombas[x][y])

    def test_realizar_primeira_jogada_celula_segura2(self):
        x, y = 0, 0 
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertNotEqual(self.jogo.tabuleiro[x][y], '-')

    def test_realizar_primeira_jogada_com_bomba(self):
        self.jogo.bombas[0][0] = True
        x, y = 0, 0
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(self.jogo.jogo_encerrado)

    def test_realizar_primeira_jogada_sem_bomba(self):
        self.jogo.bombas[1][0] = True
        x, y = 0, 0
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(self.jogo.jogo_encerrado)

    def test_realizar_primeira_jogada_com_multiplas_tentativas(self):
        bomb_x, bomb_y = 0, 0
        self.jogo.bombas[bomb_x][bomb_y] = True
        for _ in range(100):
            x, y = bomb_x, bomb_y
            while x == bomb_x and y == bomb_y:
                x = random.randint(0, self.jogo.linhas - 1)
                y = random.randint(0, self.jogo.colunas - 1)
            self.jogo.realizar_primeira_jogada(x, y)
            if self.jogo.tabuleiro[x][y] != '-':
                break  
        self.assertFalse(self.jogo.bombas[x][y])

    def test_jogo_nao_encerrado(self):
        self.assertFalse(self.jogo.jogo_encerrado)

    def test_niveis_dificuldade_invalidos(self):
        with self.assertRaises(ValueError):
            CampoMinado(4)

    def test_jogador_vence2(self):
        self.jogo.tabuleiro = [['1', 'B', ' ', ' ', ' ', 'B', '2', ' '],
                              ['1', '3', 'B', '1', '1', '3', 'B', '2'],
                              [' ', ' ', ' ', ' ', 'B', '2', 'B', 'B'],
                              [' ', '1', 'B', '3', 'B', '2', '2', '1'],
                              [' ', '1', '2', 'B', '2', 'B', '2', ' '],
                              ['1', '2', '2', '1', '1', '2', '2', ' '],
                              ['B', '2', 'B', '1', 'B', '2', 'B', '1'],
                              ['1', '1', '1', '1', '2', '3', 'B', 'B']]
        
        self.assertTrue(self.jogo.venceu_jogo())


if __name__ == '__main__':
    unittest.main()
