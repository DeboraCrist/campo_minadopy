from ast import main
import unittest
from unittest.mock import patch

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

if __name__ == '__main__':
    unittest.main()

