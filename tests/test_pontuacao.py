import unittest
import time
import tkinter as tk
from UI import JogoCampoMinadoTabuleiro  # Replace with your actual script name

class TestCampoMinadoHistorico(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.game = JogoCampoMinadoTabuleiro(self.root, nivel=1)

    def test_tempo_registrado_no_historico_apos_fim_de_jogo_resultado(self):
        self.game.update_timer()
        time.sleep(2) 
        self.game.stop_timer()
        self.game.mostrar_fim_de_jogo("Test game result")
        with open('historico.txt', 'r') as history_file:
            history_content = history_file.read()
            self.assertIn("Test game result", history_content) 

    def test_tempo_registrado_no_historico_apos_fim_de_jogo_resultado_nivel2(self):
        game = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        game.update_timer()
        time.sleep(2) 
        game.stop_timer()
        game.mostrar_fim_de_jogo("Test game result")
        with open('historico.txt', 'r') as history_file:
            history_content = history_file.read()
            self.assertIn("Test game result", history_content) 

    def test_tempo_registrado_no_historico_apos_fim_de_jogo_resultado_nivel3(self):
        game = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        game.update_timer()
        time.sleep(2) 
        game.stop_timer()
        game.mostrar_fim_de_jogo("Test game result")
        with open('historico.txt', 'r') as history_file:
            history_content = history_file.read()
            self.assertIn("Test game result", history_content) 

    def test_tempo_registrado_no_historico_apos_fim_de_jogo_pontuacao(self):
        self.game.update_timer()
        time.sleep(2)  
        self.game.stop_timer()
        self.game.mostrar_fim_de_jogo("Test game result")
        with open('historico.txt', 'r') as history_file:
            history_content = history_file.read()
            self.assertRegex(history_content, r'Pontuação: \d+\.\d+ segundos')

    def test_tempo_registrado_no_historico_apos_fim_de_jogo_pontuacao_nivel2(self):
        game = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        game.update_timer()
        time.sleep(2)  
        game.stop_timer()
        game.mostrar_fim_de_jogo("Test game result")
        with open('historico.txt', 'r') as history_file:
            history_content = history_file.read()
            self.assertRegex(history_content, r'Pontuação: \d+\.\d+ segundos')

    def test_tempo_registrado_no_historico_apos_fim_de_jogo_pontuacao_nivel3(self):
        game = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        game.update_timer()
        time.sleep(2)  
        game.stop_timer()
        game.mostrar_fim_de_jogo("Test game result")
        with open('historico.txt', 'r') as history_file:
            history_content = history_file.read()
            self.assertRegex(history_content, r'Pontuação: \d+\.\d+ segundos')
 
    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
