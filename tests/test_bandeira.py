import unittest
from campo_minado import CampoMinado
from unittest.mock import patch
from io import StringIO

class TestBandeira(unittest.TestCase):

    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_colocar_bandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], 'F')

    def test_removerBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], '-')

    def test_removerBandeiraDeCelulaSemBandeira(self):
        self.jogo.remover_bandeira(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], '-')

    def test_naoPermitirDescobrirComBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], 'F')

    def test_desvendarCelulaAposRemoverBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_zonasCobertasIniciaisSemBandeiras(self):
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_colocar_bandeiras_igual_numero_de_bombas(self):    
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.assertTrue(self.jogo.jogo_vencido)

    def test_bandeira_em_zona_revelada(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], 'F')  
 
    def test_bandeira_em_zona_reveladaprint(self):
        self.jogo.descobrir_zona(0, 0)

        #  um objeto StringIO para capturar a saída padrão
        output_buffer = StringIO()

        # Redireciona a saída padrão para o objeto de captura
        with patch('sys.stdout', new=output_buffer):
            self.jogo.colocar_bandeira(0, 0)

        # Obtenha a saída capturada como uma string
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar uma bandeira em uma zona já revelada.", output_text)

    def test_descobrir_zona_com_bandeira_print(self):
        self.jogo.colocar_bandeira(0, 0)
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            self.jogo.descobrir_zona(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você deve remover a bandeira antes de descobrir a zona.", output_text)

    def test_colocar_mais_bandeiras_do_que_bombas_print(self):
        self.jogo.bandeiras_colocadas = self.jogo.num_bombas
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            self.jogo.colocar_bandeira(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar mais bandeiras do que o número de bombas.", output_text)
    
    def test_colocar_bandeiras_menos_que_numero_de_bombas(self):
        self.jogo.inicializar_tabuleiro()
        self.jogo.num_bombas = 8
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.assertEqual(self.jogo.bandeiras_colocadas, 8) 
    
    def test_colocar_bandeiras_mais_que_numero_de_bombas(self):
        self.jogo.inicializar_tabuleiro()
        self.jogo.num_bombas = 11
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.assertEqual(self.jogo.bandeiras_colocadas, 10) 

    def test_descobrir_zona_apos_colocar_e_remover_bandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    
if __name__ == '__main__':
    unittest.main()