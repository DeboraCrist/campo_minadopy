import tkinter as tk
import unittest
from UI import JogoCampoMinadoTabuleiro 

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

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
