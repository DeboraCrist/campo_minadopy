import unittest
from campo_minado import CampoMinado
from unittest.mock import patch
from io import StringIO

class TestCampoMinado(unittest.TestCase):

    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_nivel_facil(self):
        self.assertEqual(self.jogo.nivel, 1)

    def test_tamanho_nivel_facil(self):
        self.assertEqual(self.jogo.tamanho, 8)

    def test_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.nivel, 2)

    def test_tamanho_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.tamanho, 10)

    def test_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.nivel, 3)

    def test_tamanho_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.tamanho, 24)

    def test_reiniciar_jogo_vencido(self):
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_reiniciar_jogo_bandeiras(self):
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_jogoNaoEncerradoNaInicializacao(self):
        self.assertEqual(self.jogo.jogo_encerrado, False)

    def test_tabuleiroInicializadoComHifens(self):
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def mostrar_tabuleiro(self):
        for row in self.tabuleiro:
            print(" ".join(row))

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

    def test_vitoria(self):
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if not self.jogo.bombas[x][y]:
                    self.jogo.descobrir_zona(x, y)
        self.assertTrue(self.jogo.venceu_jogo())

    def test_naoPermitirDescobrirComBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertEqual(self.jogo.tabuleiro[0][0], 'F')

    def test_desvendarCelulaAposRemoverBandeira(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.remover_bandeira(0, 0)
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_descobrirZona(self):
        self.jogo.descobrir_zona(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_reiniciarJogo_RedefinirTabuleiroParaEstadoInicial(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_reiniciarJogo_JogoEncerradoFalso(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_encerrado, False)

    def test_reiniciarJogo_JogoVencidoFalso(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_zonasCobertasIniciaisSemBandeiras(self):
        self.assertEqual(self.jogo.bandeiras_colocadas, 0)

    def test_reiniciarJogoVencidoComDescoberta(self):
        self.jogo.tabuleiro = [['-' for _ in range(self.jogo.tamanho)] for _ in range(self.jogo.tamanho)]
        self.jogo.jogo_vencido = True
        self.jogo.descobrir_zona(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertEqual(self.jogo.jogo_vencido, False)

    def test_colocar_bandeiras_igual_numero_de_bombas(self):    
        for x in range(self.jogo.tamanho):
            for y in range(self.jogo.tamanho):
                if self.jogo.bombas[x][y]:
                    self.jogo.colocar_bandeira(x, y)
        self.assertTrue(self.jogo.jogo_vencido)

    def test_JogoNaoEstaEmEstadoInicial(self):
        self.jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], '-')

    def test_ReiniciarJogo(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_ReiniciarJogoNivel2(self):
        jogo = CampoMinado(2)
        jogo.colocar_bandeira(0, 0)
        jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))
    
    def test_ReiniciarJogonivel3(self):
        jogo = CampoMinado(3)
        jogo.colocar_bandeira(0, 0)
        jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))
    
    def test_ReiniciarJogoEmMeioAoJogo(self):
        self.jogo.colocar_bandeira(0, 0)
        self.jogo.descobrir_zona(1, 1)
        self.jogo.reiniciar_jogo()
        self.assertTrue(all(cell == '-' for row in self.jogo.tabuleiro for cell in row))

    def test_bandeira_em_zona_revelada(self):
        self.jogo.descobrir_zona(0, 0)
        self.jogo.colocar_bandeira(0, 0)
        self.assertNotEqual(self.jogo.tabuleiro[0][0], 'F')  
 
    def test_bandeira_em_zona_revelada(self):
        self.jogo.descobrir_zona(0, 0)

        #  um objeto StringIO para capturar a saída padrão
        output_buffer = StringIO()

        # Redireciona a saída padrão para o objeto de captura
        with patch('sys.stdout', new=output_buffer):
            self.jogo.colocar_bandeira(0, 0)

        # Obtenha a saída capturada como uma string
        output_text = output_buffer.getvalue()
        self.assertIn("Ação inválida. Você não pode colocar uma bandeira em uma zona já revelada.", output_text)

if __name__ == '__main__':
    unittest.main()
