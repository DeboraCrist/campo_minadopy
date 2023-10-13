from ast import main
import unittest
from unittest.mock import patch

from main import play_again

class TestCampoMinado(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1', 'N', 'Q'])
    def test_main_quit_nivel1(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['1', 'N', 'D', '0', '0', 'Q'])
    def test_main_descobrir_quit_nivel1(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['1', 'N', 'D', '0', '0', 'B', '0', '0', 'R', '0', '0', 'Q'])
    def test_main_descobrir_bandeira_remover_quit_nivel1(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['2', 'N', 'Q'])
    def test_main_quit_nivel2(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['2', 'N', 'D', '0', '0', 'Q'])
    def test_main_descobrir_quit_nivel2(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['2', 'N', 'D', '0', '0', 'B', '0', '0', 'R', '0', '0', 'Q'])
    def test_main_descobrir_bandeira_remover_quit_nivel2(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['3', 'N', 'Q'])
    def test_main_quit_nivel3(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['3', 'N', 'D', '0', '0', 'Q'])
    def test_main_descobrir_quit_nivel3(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.input', side_effect=['3', 'N', 'D', '0', '0', 'B', '0', '0', 'R', '0', '0', 'Q'])
    def test_main_descobrir_bandeira_remover_quit_nivel3(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    def test_interface_sair_do_jogo(self):
        with patch('builtins.input', side_effect=['Q']):
            with self.assertRaises(SystemExit):
                main()

    def test_interface_reiniciar_jogo(self):
        with patch('builtins.input', side_effect=['N']):
            with self.assertRaises(SystemExit):
                main()

    def test_jogar_novamente_sim(self):
        with patch('builtins.input', return_value='S'):
            resultado = play_again()
            self.assertTrue(resultado)

    def test_jogar_novamente_nao(self):
        with patch('builtins.input', return_value='N'):
            resultado = play_again()
            self.assertFalse(resultado)

    def test_entrada_invalida(self):
        with patch('builtins.input', return_value='X'):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertNotEqual(cm.exception.code, None)

  
if __name__ == '__main__':
    unittest.main()

