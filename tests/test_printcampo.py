import unittest
from campo_minado import CampoMinado
from unittest.mock import patch
from io import StringIO

class TestCampoMinadoPrint(unittest.TestCase):

    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_sair_imprime_mensagem_de_saindo(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.jogo.sair()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Saindo do jogo.")

    def test_descobrir_zona_com_bandeira_print(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.jogo.colocar_bandeira(1, 1)  
            self.jogo.descobrir_zona(1, 1) 
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Ação inválida. Você deve remover a bandeira antes de descobrir a zona.")

    def teste_colocacao_de_bandeira_invalida_print(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.jogo.colocar_bandeira(1, 1)  
            self.jogo.colocar_bandeira(2, 2) 
            self.jogo.colocar_bandeira(1, 3)  
            self.jogo.colocar_bandeira(2, 4) 
            self.jogo.colocar_bandeira(1, 5)  
            self.jogo.colocar_bandeira(2, 1) 
            self.jogo.colocar_bandeira(1, 2)  
            self.jogo.colocar_bandeira(2, 3) 
            self.jogo.colocar_bandeira(1, 4)  
            self.jogo.colocar_bandeira(2, 5) 
            self.jogo.colocar_bandeira(5, 5)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Ação inválida. Você não pode colocar mais bandeiras do que o número de bombas.")

    def teste_bandeira_em_bomba_invalida_print(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.jogo.realizar_primeira_jogada(0, 0) 
            self.jogo.colocar_bandeira(0, 0)  
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Ação inválida. Você não pode colocar uma bandeira em uma zona já revelada.")

    def teste_bandeira_fora_do_tabuleiro_invalida_print(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.jogo.colocar_bandeira(self.jogo.linhas + 1, self.jogo.colunas + 1)  
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Posição fora do tabuleiro.")

    def teste_nivel_de_dificuldade_invalido_print(self):
        with self.assertRaises(ValueError) as context:
            jogo = CampoMinado(4) 
        exception = context.exception
        self.assertEqual(str(exception), "Nível de dificuldade inválido")

if __name__ == '__main__':
    unittest.main()
