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

    def test_sair_print(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.jogo.sair()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Saindo do jogo.")
    
if __name__ == '__main__':
    unittest.main()
