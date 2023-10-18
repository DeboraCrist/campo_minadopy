from ast import main
from io import StringIO
import io
import unittest
from unittest.mock import patch
from campo_minado import CampoMinado

from main import exibir_historico, play_again, start_game

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
    
    def test_exibir_historico_existente(self):
        with open('historico.txt', 'w') as arquivo:
            arquivo.write("Jogo 1: Vitória\nJogo 2: Derrota")
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            exibir_historico()
            output = mock_stdout.getvalue()
        self.assertEqual(output, "Histórico de Partidas:\n\nJogo 1: Vitória\nJogo 2: Derrota\n")

    def test_exibir_historico_inexistente(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            exibir_historico()
            output = mock_stdout.getvalue()
        self.assertNotEqual(output, "Nenhum histórico disponível.\n")

    def test_coordenadas_validas(self):
        jogo = CampoMinado(1)
        try:
            jogo.colocar_bandeira(0, 0)
            jogo.remover_bandeira(5, 5)
            jogo.realizar_primeira_jogada(3, 3)
        except ValueError:
            self.fail("Coordenadas válidas geraram exceção")

    def test_coordenadas_validas_nivel2(self):
        jogo = CampoMinado(2)
        try:
            jogo.colocar_bandeira(0, 0)
            jogo.remover_bandeira(5, 5)
            jogo.realizar_primeira_jogada(3, 3)
        except ValueError:
            self.fail("Coordenadas válidas geraram exceção")

    def test_coordenadas_validas_nivel3(self):
        jogo = CampoMinado(3)
        try:
            jogo.colocar_bandeira(0, 0)
            jogo.remover_bandeira(5, 5)
            jogo.realizar_primeira_jogada(3, 3)
        except ValueError:
            self.fail("Coordenadas válidas geraram exceção")

if __name__ == '__main__':
    unittest.main()

