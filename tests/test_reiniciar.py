import unittest
from campo_minado import CampoMinado
from unittest.mock import patch

class TestReiniciar(unittest.TestCase):

    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_reiniciar_jogo_vencido(self):
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_reiniciar_jogo_vencido_nivel2(self):
        jogo = CampoMinado(2)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_reiniciar_jogo_vencido_nivel3(self):
        jogo = CampoMinado(3)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_reiniciar_jogo_bandeiras(self):
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_reiniciar_jogo_bandeiras_nivel2(self):
        jogo = CampoMinado(2)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.bandeiras_colocadas, 0)

    def test_reiniciar_jogo_bandeiras_nivel3(self):
        jogo = CampoMinado(3)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.bandeiras_colocadas, 0)

    def test_reiniciarJogo_RedefinirTabuleiroParaEstadoInicial(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_reiniciarJogo_RedefinirTabuleiroParaEstadoInicial_nivel2(self):
        jogo = CampoMinado(2)
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_reiniciarJogo_RedefinirTabuleiroParaEstadoInicial_nivel3(self):
        jogo = CampoMinado(3)
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_reiniciarJogo_JogoEncerradoFalso(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_encerrado, False)

    def test_reiniciarJogo_JogoEncerradoFalso_nivel2(self):
        jogo = CampoMinado(2)
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_encerrado, False)

    def test_reiniciarJogo_JogoEncerradoFalso_nivel3(self):
        jogo = CampoMinado(3)
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_encerrado, False)

    def test_reiniciarJogo_JogoVencidoFalso(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_reiniciarJogo_JogoVencidoFalso_nivel2(self):
        jogo = CampoMinado(2)
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_reiniciarJogo_JogoVencidoFalso_nivel3(self):
        jogo = CampoMinado(3)
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_reiniciarJogoVencidoComDescoberta(self):
        self.jogo.tabuleiro = [['-' for _ in range(self.jogo.linhas)] for _ in range(self.jogo.colunas)]
        self.jogo.jogo_vencido = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_reiniciarJogoVencidoComDescoberta_nivel2(self):
        jogo = CampoMinado(2)
        jogo.tabuleiro = [['-' for _ in range(jogo.linhas)] for _ in range(jogo.colunas)]
        jogo.jogo_vencido = True
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_reiniciarJogoVencidoComDescoberta_nivel3(self):
        jogo = CampoMinado(3)
        jogo.tabuleiro = [['-' for _ in range(jogo.linhas)] for _ in range(jogo.colunas)]
        jogo.jogo_vencido = True
        jogo.descobrir_zona(0, 0)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_vencido, False)

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

if __name__ == '__main__':
    unittest.main()
