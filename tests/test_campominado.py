import datetime
import io
import random
import sys
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

    def test_jogoNaoEncerradoNaInicializacaoNivel2(self):
        jogo = CampoMinado(2) 
        self.assertEqual(jogo.jogo_encerrado, False)

    def test_jogoNaoEncerradoNaInicializacaoNivel3(self):
        jogo = CampoMinado(3) 
        self.assertEqual(jogo.jogo_encerrado, False)

    def test_tabuleiroInicializadoComHifens(self):
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_tabuleiroInicializadoComHifensNivel2(self):
        jogo = CampoMinado(2) 
        self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))
    
    def test_tabuleiroInicializadoComHifensNivel3(self):
        jogo = CampoMinado(3) 
        self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))

    def test_descobrirZona(self):
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_descobrirZonaNivel2(self):
        jogo = CampoMinado(2) 
        jogo.descobrir_zona(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_descobrirZonaNivel3(self):
        jogo = CampoMinado(3)
        jogo.descobrir_zona(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_JogoNaoEstaEmEstadoInicial(self):
        self.jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_JogoNaoEstaEmEstadoInicialNivel2(self):
        jogo = CampoMinado(2) 
        jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_JogoNaoEstaEmEstadoInicialNivel3(self):
        jogo = CampoMinado(3) 
        jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_sair_marca_jogo_como_encerradoNivel2(self):
        jogo = CampoMinado(2) 
        jogo.sair()
        self.assertTrue(jogo.jogo_encerrado)

    def test_sair_marca_jogo_como_encerradoNivel3(self):
        jogo = CampoMinado(3) 
        jogo.sair()
        self.assertTrue(jogo.jogo_encerrado)

    def test_sair_nao_afeta_resultados(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(1, 1)
        self.jogo.descobrir_zona(2, 2)
        estado_anterior = self.jogo.tabuleiro
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.jogo.sair()
            self.assertEqual(self.jogo.tabuleiro, estado_anterior)

    def test_sair_nao_afeta_resultadosNivel2(self):
        jogo = CampoMinado(2) 
        jogo.descobrir_zona(0, 0)
        jogo.colocar_bandeira(1, 1)
        jogo.descobrir_zona(2, 2)
        estado_anterior = jogo.tabuleiro
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.jogo.sair()
            self.assertEqual(jogo.tabuleiro, estado_anterior)
    
    def test_sair_nao_afeta_resultadosNivel3(self):
        jogo = CampoMinado(3) 
        jogo.descobrir_zona(0, 0)
        jogo.colocar_bandeira(1, 1)
        jogo.descobrir_zona(2, 2)
        estado_anterior = jogo.tabuleiro
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.jogo.sair()
            self.assertEqual(jogo.tabuleiro, estado_anterior)

    def test_sair_nao_afeta_resultados_print(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(1, 1)
        self.jogo.descobrir_zona(2, 2)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.jogo.sair()
            self.assertEqual(mock_stdout.getvalue().strip(), "Saindo do jogo.")

    def test_sair_nao_afeta_resultados_print_nivel2(self):
        jogo = CampoMinado(2) 
        jogo.descobrir_zona(0, 0)
        jogo.colocar_bandeira(1, 1)
        jogo.descobrir_zona(2, 2)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            jogo.sair()
            self.assertEqual(mock_stdout.getvalue().strip(), "Saindo do jogo.")

    def test_sair_nao_afeta_resultados_print_nivel3(self):
        jogo = CampoMinado(3) 
        jogo.descobrir_zona(0, 0)
        jogo.colocar_bandeira(1, 1)
        jogo.descobrir_zona(2, 2)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            jogo.sair()
            self.assertEqual(mock_stdout.getvalue().strip(), "Saindo do jogo.")

    def test_sair_apos_vitoria(self):
        self.jogo.jogo_vencido = True
        self.jogo.sair()
        self.assertTrue(self.jogo.jogo_vencido)

    def test_sair_apos_vitoria_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        jogo.sair()
        self.assertTrue(jogo.jogo_vencido)

    def test_sair_apos_vitoria_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        jogo.sair()
        self.assertTrue(jogo.jogo_vencido)

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

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com5(self):
        self.jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [False, True, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '5')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com5_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [False, True, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '5')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com5_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [False, True, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '5')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com4(self):
        self.jogo.bombas = [
            [False, True, False],
            [True, False, True],
            [False, True, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '4')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com4_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas = [
            [True, False, False],
            [True, False, True],
            [False, True, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '4')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com4_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas = [
            [True, False, False],
            [True, False, True],
            [False, True, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '4')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com3(self):
        self.jogo.bombas = [
            [False, False, False],
            [True, False, True],
            [False, True, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '3')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com3_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas = [
            [False, False, False],
            [True, False, True],
            [False, True, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '3')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com3_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas = [
            [False, False, False],
            [True, False, True],
            [False, True, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '3')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com1(self):
        self.jogo.bombas = [
            [True, False, False],
            [False, False, False],
            [False, False, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '1')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com1_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas = [
            [True, False, False],
            [False, False, False],
            [False, False, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '1')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com1_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas = [
            [True, False, False],
            [False, False, False],
            [False, False, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '1')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com2(self):
        self.jogo.bombas = [
            [True, False, True],
            [False, False, False],
            [False, False, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '2')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com2_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas = [
            [True, False, True],
            [False, False, False],
            [False, False, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '2')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com2_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas = [
            [True, False, True],
            [False, False, False],
            [False, False, False]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '2')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com7(self):
        self.jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, True, True]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '7')    

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com7_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, True, True]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '7')  

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com7_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, True, True]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '7')    
    
    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com6(self):
        self.jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, False, True]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '6')    

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com6_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, False, True]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '6')    

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com6_nivel2(self):
        jogo = CampoMinado(3)
        jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, False, True]
        ]
        jogo.descobrir_zona(1, 1)
        self.assertEqual(jogo.tabuleiro[1][1], '6')  

    def test_vencer_jogo(self):
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if not self.jogo.bombas[x][y]:
                    self.jogo.descobrir_zona(x, y)
        self.assertTrue(self.jogo.jogo_vencido)

    def test_vencer_jogo_nivel2(self):
        jogo = CampoMinado(2)
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if not jogo.bombas[x][y]:
                    jogo.descobrir_zona(x, y)
        self.assertTrue(jogo.jogo_vencido)

    def test_vencer_jogo_nivel3(self):
        jogo = CampoMinado(3)
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if not jogo.bombas[x][y]:
                    jogo.descobrir_zona(x, y)
        self.assertTrue(jogo.jogo_vencido)

    def test_descobrir_zona_com_jogo_encerrado(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.descobrir_zona(1, 1)
        self.assertTrue(self.jogo.jogo_encerrado)

    def test_descobrir_zona_com_jogo_encerrado_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        jogo.descobrir_zona(1, 1)
        self.assertTrue(jogo.jogo_encerrado)

    def test_descobrir_zona_com_jogo_encerrado_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        jogo.descobrir_zona(0, 0)
        jogo.descobrir_zona(1, 1)
        self.assertTrue(jogo.jogo_encerrado)

    def test_descobrir_zona_com_jogo_vencido(self):
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if not self.jogo.bombas[x][y]:
                    self.jogo.descobrir_zona(x, y)
        self.assertTrue(self.jogo.jogo_vencido)

    def test_descobrir_zona_com_jogo_vencido_nivel2(self):
        jogo = CampoMinado(2)
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if not jogo.bombas[x][y]:
                    jogo.descobrir_zona(x, y)
        self.assertTrue(jogo.jogo_vencido)

    def test_descobrir_zona_com_jogo_vencido_nivel3(self):
        jogo = CampoMinado(3)
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if not jogo.bombas[x][y]:
                    jogo.descobrir_zona(x, y)
        self.assertTrue(jogo.jogo_vencido)
    
    def test_realizar_primeira_jogada_celula_segura(self):
        x, y = 0, 0 
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(self.jogo.bombas[x][y])

    def test_realizar_primeira_jogada_celula_segura_nivel2(self):
        jogo = CampoMinado(2)
        x, y = 0, 0 
        jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(jogo.bombas[x][y])

    def test_realizar_primeira_jogada_celula_segura_nivel3(self):
        jogo = CampoMinado(3)
        x, y = 0, 0 
        jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(jogo.bombas[x][y])

    def test_realizar_primeira_jogada_celula_segura2(self):
        x, y = 0, 0 
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertNotEqual(self.jogo.tabuleiro[x][y], '-')

    def test_realizar_primeira_jogada_celula_segura2_nivel2(self):
        jogo = CampoMinado(2)
        x, y = 0, 0 
        jogo.realizar_primeira_jogada(x, y)
        self.assertNotEqual(jogo.tabuleiro[x][y], '-')

    def test_realizar_primeira_jogada_celula_segura2_nivel3(self):
        jogo = CampoMinado(3)
        x, y = 0, 0 
        jogo.realizar_primeira_jogada(x, y)
        self.assertNotEqual(jogo.tabuleiro[x][y], '-')

    def test_realizar_primeira_jogada_com_bomba(self):
        self.jogo.bombas[0][0] = True
        x, y = 0, 0
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(self.jogo.jogo_encerrado)

    def test_realizar_primeira_jogada_com_bomba_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[0][0] = True
        x, y = 0, 0
        jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(jogo.jogo_encerrado)

    def test_realizar_primeira_jogada_com_bomba_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[0][0] = True
        x, y = 0, 0
        jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(jogo.jogo_encerrado)

    def test_realizar_primeira_jogada_sem_bomba(self):
        self.jogo.bombas[1][0] = True
        x, y = 0, 0
        self.jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(self.jogo.jogo_encerrado)

    def test_realizar_primeira_jogada_sem_bomba_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bombas[1][0] = True
        x, y = 0, 0
        jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(jogo.jogo_encerrado)

    def test_realizar_primeira_jogada_sem_bomba_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bombas[1][0] = True
        x, y = 0, 0
        jogo.realizar_primeira_jogada(x, y)
        self.assertFalse(jogo.jogo_encerrado)

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

    def test_realizar_primeira_jogada_com_multiplas_tentativas_nivel2(self):
        jogo = CampoMinado(2)
        bomb_x, bomb_y = 0, 0
        jogo.bombas[bomb_x][bomb_y] = True
        for _ in range(100):
            x, y = bomb_x, bomb_y
            while x == bomb_x and y == bomb_y:
                x = random.randint(0, jogo.linhas - 1)
                y = random.randint(0, jogo.colunas - 1)
            jogo.realizar_primeira_jogada(x, y)
            if jogo.tabuleiro[x][y] != '-':
                break  
        self.assertFalse(jogo.bombas[x][y])

    def test_realizar_primeira_jogada_com_multiplas_tentativas_nivel3(self):
        jogo = CampoMinado(3)
        bomb_x, bomb_y = 0, 0
        jogo.bombas[bomb_x][bomb_y] = True
        for _ in range(100):
            x, y = bomb_x, bomb_y
            while x == bomb_x and y == bomb_y:
                x = random.randint(0, jogo.linhas - 1)
                y = random.randint(0, jogo.colunas - 1)
            jogo.realizar_primeira_jogada(x, y)
            if jogo.tabuleiro[x][y] != '-':
                break  
        self.assertFalse(jogo.bombas[x][y])

    def test_jogo_nao_encerrado(self):
        self.assertFalse(self.jogo.jogo_encerrado)

    def test_jogo_nao_encerrado_nivel2(self):
        jogo = CampoMinado(2)
        self.assertFalse(jogo.jogo_encerrado)

    def test_jogo_nao_encerrado_nivel3(self):
        jogo = CampoMinado(3)
        self.assertFalse(jogo.jogo_encerrado)

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
