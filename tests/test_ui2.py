import unittest
import tkinter as tk
from tkinter import ttk
from UI import JogoCampoMinadoGUI, JogoCampoMinadoTabuleiro

class TestCampoMinadoGUI2(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.top = tk.Toplevel(self.root)
        self.app = JogoCampoMinadoGUI(self.top)
        self.root.update()
    
    def test_elementos_da_GUI_texto(self):
        self.assertEqual(self.app.master.title(), "Campo Minado")

    def test_exibir_historico(self):
        with open('historico.txt', 'w') as arquivo:
            arquivo.write("Sample history\n")
        self.app.exibir_historico()


    def tearDown(self):
        self.top.destroy()


if __name__ == "__main__":
    unittest.main()


    