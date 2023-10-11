import unittest
from campo_minado import CampoMinado
from unittest.mock import patch
from io import StringIO

class TestCampoMinado(unittest.TestCase):

    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_nivel_facil(self):
        self.assertEqual(self.jogo.nivel, 1)

    def test_tamanho_nivel_facil(self):
        self.assertEqual(self.jogo.tamanho, 8)

    def test_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.nivel, 2)

    def test_tamanho_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.tamanho, 10)

    def test_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.nivel, 3)

    def test_tamanho_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.tamanho, 24)

    def test_reiniciar_jogo_vencido(self):
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_reiniciar_jogo_bandeiras(self):
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_jogoNaoEncerradoNaInicializacao(self):
        self.assertEqual(self.jogo.jogo_encerrado, False)

    def test_tabuleiroInicializadoComHifens(self):
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_descobrirZona(self):
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_reiniciarJogo_RedefinirTabuleiroParaEstadoInicial(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_reiniciarJogo_JogoEncerradoFalso(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_encerrado, False)

    def test_reiniciarJogo_JogoVencidoFalso(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_reiniciarJogoVencidoComDescoberta(self):
        self.jogo.tabuleiro = [['-' for _ in range(self.jogo.tamanho)] for _ in range(self.jogo.tamanho)]
        self.jogo.jogo_vencido = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_JogoNaoEstaEmEstadoInicial(self):
        self.jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_ReiniciarJogo(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_ReiniciarJogoNivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))
    
    def test_ReiniciarJogonivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))
    
    def test_ReiniciarJogoEmMeioAoJogo(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(1, 1)
        self.jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_sair_lanca_excecao_system_exit(self):
        with self.assertRaises(SystemExit):
            self.jogo.sair()

    def test_sair_codigo_excecao_system_exit_e_nulo(self):
        with self.assertRaises(SystemExit) as cm:
            self.jogo.sair()
        self.assertIsNone(cm.exception.code)

    def test_sair_imprime_mensagem_de_saindo(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit):
                self.jogo.sair()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Saindo do jogo.")

    # def test_descobrir_celula_ja_descoberta(self):
    #     # Inicializar o jogo, revelando algumas células
    #     self.jogo.descobrir_zona(1, 1)
    #     self.jogo.descobrir_zona(2, 2)
        
    #     # Tentar descobrir uma célula que já foi descoberta
    #     self.jogo.descobrir_zona(1, 1)
    #     self.assertEqual(self.jogo.tabuleiro[1][1], '1')  

    
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

    # def test_descobrir_celula_revelada(self):
    #     jogo = CampoMinado(1)  # Substitua pelo nível desejado
    #     jogo.descobrir_zona(0, 0)
    #     jogo.descobrir_zona(0, 1)  # Tente descobrir uma célula vizinha
    #     self.assertTrue(jogo.tabuleiro[0][1] == ' ', "A célula deve ser revelada")

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com4(self):
        self.jogo.bombas = [
            [False, True, False],
            [True, False, True],
            [False, True, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '4')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com1(self):
        self.jogo.bombas = [
            [True, False, False],
            [False, False, False],
            [False, False, False]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '1')

    def test_numeros_nas_zonas_limpo_com_bombas_adjacentes_com7(self):
        self.jogo.bombas = [
            [True, True, False],
            [True, False, True],
            [True, True, True]
        ]
        self.jogo.descobrir_zona(1, 1)
        self.assertEqual(self.jogo.tabuleiro[1][1], '7')

    # def test_espacos_vazios_sem_bombas_adjacentes(self):
    #   
    #     jogo = CampoMinado(1)
    #     jogo.bombas = [
    #         [False, False, False],
    #         [False, False, False],
    #         [False, False, False]
    #     
    #     jogo.descobrir_zona(1, 1)

    #     self.assertEqual(jogo.tabuleiro[1][1], ' ')

    def test_vencer_jogo(self):
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if not self.jogo.bombas[x][y]:
                    self.jogo.descobrir_zona(x, y)
        self.assertTrue(self.jogo.jogo_vencido)

    def test_descobrir_zona_com_jogo_encerrado(self):
        self.jogo.bombas[0][0] = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.descobrir_zona(1, 1)
        self.assertTrue(self.jogo.jogo_encerrado)

    def test_descobrir_zona_com_jogo_vencido(self):
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if not self.jogo.bombas[x][y]:
                    self.jogo.descobrir_zona(x, y)
        self.assertTrue(self.jogo.jogo_vencido)
  
if __name__ == '__main__':
    unittest.main()
