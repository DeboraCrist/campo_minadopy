import unittest
import tkinter as tk
from tkinter import ttk
from UI import JogoCampoMinadoGUI, JogoCampoMinadoTabuleiro

class TestCampoMinadoGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = JogoCampoMinadoGUI(self.root)
        self.root.update()

    def test_elementos_da_GUI_texto(self):
        self.assertEqual(self.app.master.title(), "Campo Minado")

