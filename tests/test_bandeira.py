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

    def test_colocar_bandeira_nivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], 'F')

    def test_colocar_bandeira_nivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], 'F')

    def test_removerBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], '-')

    def test_removerBandeira_nivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], '-')

    def test_removerBandeira_nivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], '-')

    def test_removerBandeiraDeCelulaSemBandeira(self):
        self.jogo.remover_bandeira(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], '-')

    def test_removerBandeiraDeCelulaSemBandeira_nivel2(self):
        jogo = CampoMinado(2)
        jogo.remover_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], '-')

    def test_removerBandeiraDeCelulaSemBandeira_nivel3(self):
        jogo = CampoMinado(3)
        jogo.remover_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], '-')

    def test_naoPermitirDescobrirComBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], 'F')

    def test_naoPermitirDescobrirComBandeira_nivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], 'F')

    def test_naoPermitirDescobrirComBandeira_nivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], 'F')

    def test_desvendarCelulaAposRemoverBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_desvendarCelulaAposRemoverBandeira_nivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_desvendarCelulaAposRemoverBandeira_nivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_zonasCobertasIniciaisSemBandeiras(self):
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_zonasCobertasIniciaisSemBandeiras_nivel2(self):
        jogo = CampoMinado(2)
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_zonasCobertasIniciaisSemBandeiras_nivel3(self):
        jogo = CampoMinado(3)
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_colocar_bandeiras_igual_numero_de_bombas(self):    
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.assertTrue(self.jogo.jogo_vencido)

    def test_colocar_bandeiras_igual_numero_de_bombas_nivel2(self): 
        jogo = CampoMinado(2)   
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                   jogo.colocar_bandeira(x, y)
        self.assertTrue(jogo.jogo_vencido)

    def test_colocar_bandeiras_igual_numero_de_bombas_nivel3(self): 
        jogo = CampoMinado(3)   
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                   jogo.colocar_bandeira(x, y)
        self.assertTrue(jogo.jogo_vencido)

    def test_bandeira_em_zona_revelada(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], 'F')  

    def test_bandeira_em_zona_revelada_nivel2(self):
        jogo = CampoMinado(2)
        jogo.descobrir_zona(0, 0)
        jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], 'F') 

    def test_bandeira_em_zona_revelada_nivel3(self):
        jogo = CampoMinado(3)
        jogo.descobrir_zona(0, 0)
        jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], 'F') 
 
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

    def test_bandeira_em_zona_reveladaprint_nivel2(self):
        jogo = CampoMinado(2)
        jogo.descobrir_zona(0, 0)
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            jogo.colocar_bandeira(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar uma bandeira em uma zona já revelada.", output_text)

    def test_bandeira_em_zona_reveladaprint_nivel3(self):
        jogo = CampoMinado(3)
        jogo.descobrir_zona(0, 0)
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            jogo.colocar_bandeira(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar uma bandeira em uma zona já revelada.", output_text)

    def test_descobrir_zona_com_bandeira_print(self):
        self.jogo.colocar_bandeira(0, 0)
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            self.jogo.descobrir_zona(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você deve remover a bandeira antes de descobrir a zona.", output_text)

    def test_descobrir_zona_com_bandeira_print_nivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            jogo.descobrir_zona(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você deve remover a bandeira antes de descobrir a zona.", output_text)

    def test_descobrir_zona_com_bandeira_print_nivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            jogo.descobrir_zona(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você deve remover a bandeira antes de descobrir a zona.", output_text)

    def test_colocar_mais_bandeiras_do_que_bombas_print(self):
        self.jogo.bandeiras_colocadas = self.jogo.num_bombas
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            self.jogo.colocar_bandeira(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar mais bandeiras do que o número de bombas.", output_text)

    def test_colocar_mais_bandeiras_do_que_bombas_print_nivel2(self):
        jogo = CampoMinado(2)
        jogo.bandeiras_colocadas = jogo.num_bombas
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            jogo.colocar_bandeira(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar mais bandeiras do que o número de bombas.", output_text)

    def test_colocar_mais_bandeiras_do_que_bombas_print_nivel3(self):
        jogo = CampoMinado(3)
        jogo.bandeiras_colocadas = jogo.num_bombas
        output_buffer = StringIO()
        with patch('sys.stdout', new=output_buffer):
            jogo.colocar_bandeira(0, 0)
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar mais bandeiras do que o número de bombas.", output_text)
    
    def test_colocar_bandeiras_menos_que_numero_de_bombas(self):
        self.jogo.inicializar_tabuleiro()
        self.jogo.num_bombas = 8
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.assertEqual(self.jogo.bandeiras_colocadas, 8) 

    def test_colocar_bandeiras_menos_que_numero_de_bombas_nivel2(self):
        jogo = CampoMinado(2)
        jogo.inicializar_tabuleiro()
        jogo.num_bombas = 8
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    jogo.colocar_bandeira(x, y)
        self.assertEqual(jogo.bandeiras_colocadas, 8) 

    def test_colocar_bandeiras_menos_que_numero_de_bombas_nivel3(self):
        jogo = CampoMinado(3)
        jogo.inicializar_tabuleiro()
        jogo.num_bombas = 8
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    jogo.colocar_bandeira(x, y)
        self.assertEqual(jogo.bandeiras_colocadas, 8) 
    
    def test_colocar_bandeiras_mais_que_numero_de_bombas(self):
        self.jogo.inicializar_tabuleiro()
        self.jogo.num_bombas = 11
        for x in range(self.jogo.linhas):
            for y in range(self.jogo.colunas):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.assertEqual(self.jogo.bandeiras_colocadas, 10) 

    def test_colocar_bandeiras_mais_que_numero_de_bombas_nivel2(self):
        jogo = CampoMinado(2)
        jogo.inicializar_tabuleiro()
        jogo.num_bombas = 31
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    jogo.colocar_bandeira(x, y)
        self.assertEqual(jogo.bandeiras_colocadas, 30) 

    def test_colocar_bandeiras_mais_que_numero_de_bombas_nivel3(self):
        jogo = CampoMinado(3)
        jogo.inicializar_tabuleiro()
        jogo.num_bombas = 101
        for x in range(jogo.linhas):
            for y in range(jogo.colunas):
                if jogo.bombas[x][y]:
                    jogo.colocar_bandeira(x, y)
        self.assertEqual(jogo.bandeiras_colocadas, 100) 

    def test_descobrir_zona_apos_colocar_e_remover_bandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zona_apos_colocar_e_remover_bandeira_nivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_descobrir_zona_apos_colocar_e_remover_bandeira_nivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        jogo.descobrir_zona(0, 0)
        self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    def test_contagem_de_uma_bandeiras(self):
        self.jogo.inicializar_tabuleiro()
        self.jogo.colocar_bandeira(0, 0)
        self.assertEqual(self.jogo.bandeiras_colocadas, 1)

    def test_contagem_de_uma_bandeiras_nivel2(self):
        jogo = CampoMinado(2)
        jogo.inicializar_tabuleiro()
        jogo.colocar_bandeira(0, 0)
        self.assertEqual(jogo.bandeiras_colocadas, 1)

    def test_contagem_de_uma_bandeiras_nivel3(self):
        jogo = CampoMinado(3)
        jogo.inicializar_tabuleiro()
        jogo.colocar_bandeira(0, 0)
        self.assertEqual(jogo.bandeiras_colocadas, 1)
        
    def test_contagem_de_maximo_bandeiras(self):
        self.jogo.inicializar_tabuleiro()
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.colocar_bandeira(1, 1)
        self.jogo.colocar_bandeira(2, 2)
        self.jogo.colocar_bandeira(3, 3)
        self.jogo.colocar_bandeira(4, 4)
        self.jogo.colocar_bandeira(5, 5)
        self.jogo.colocar_bandeira(6, 6)
        self.jogo.colocar_bandeira(7, 7)
        self.jogo.colocar_bandeira(5, 1)
        self.jogo.colocar_bandeira(4, 2)
        self.assertEqual(self.jogo.bandeiras_colocadas, 10)

    def test_contagem_de_bandeiras_colocareremover(self):
        self.jogo.inicializar_tabuleiro()
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.jogo.colocar_bandeira(0, 0)
        self.assertEqual(self.jogo.bandeiras_colocadas, 1)

    def test_contagem_de_bandeiras_colocareremover_nivel2(self):
        jogo = CampoMinado(2)
        jogo.inicializar_tabuleiro()
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        jogo.colocar_bandeira(0, 0)
        self.assertEqual(jogo.bandeiras_colocadas, 1)

    def test_contagem_de_bandeiras_colocareremover_nivel3(self):
        jogo = CampoMinado(3)
        jogo.inicializar_tabuleiro()
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        jogo.colocar_bandeira(0, 0)
        self.assertEqual(jogo.bandeiras_colocadas, 1)

if __name__ == '__main__':
    unittest.main()