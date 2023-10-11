import tkinter as tk
import unittest
from UI import JogoCampoMinadoGUI, JogoCampoMinadoTabuleiro


class TestCampoMinadoGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = JogoCampoMinadoTabuleiro(self.root, nivel=1)
    
    def test_interface_inicial(self):
        self.assertEqual(self.app.nivel, 1)
        self.assertEqual(self.app.jogo.tamanho, 8)

    def test_clicar_celula(self):
        self.app.clicar_celula(0, 0)
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_atualizar_interface(self):
        self.app.jogo.tabuleiro[0][0] = '1'
        self.app.atualizar_interface()
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['text'], '1')

    def teste_perda_do_jogo(self):
        self.app.jogo.bombas[0][0] = True
        self.app.clicar_celula(0, 0)
        self.assertTrue(self.app.jogo.jogo_encerrado)

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
