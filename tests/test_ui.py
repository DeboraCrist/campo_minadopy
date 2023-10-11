import tkinter as tk
import unittest
from UI import JogoCampoMinadoTabuleiro

class TestCampoMinadoGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = JogoCampoMinadoTabuleiro(self.root, nivel=1)

    def test_clicar_celula(self):
        self.app.clicar_celula(0, 0)
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_atualizar_interface(self):
        self.app.jogo.tabuleiro[0][0] = '1'
        self.app.atualizar_interface()
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['text'], '1')

    def teste_perda_do_jogo(self):
        self.app.jogo.bombas[0][0] = True
        self.app.clicar_celula(0, 0)
        self.assertTrue(self.app.jogo.jogo_encerrado)

    def test_vitoria_jogo(self):
        for x in range(self.app.jogo.tamanho):
            for y in range(self.app.jogo.tamanho):
                if not self.app.jogo.bombas[x][y]:
                    self.app.clicar_celula(x, y)
        self.assertTrue(self.app.jogo.jogo_vencido)

    def test_interface_inicial(self):
        self.assertEqual(self.app.botoes[0][0]['state'], 'normal')

    def test_interface_inicial1(self):
        self.assertEqual(self.app.botoes[0][1]['state'], 'normal')

    def test_interface_inicial8(self):
        self.assertEqual(self.app.botoes[7][7]['state'], 'normal')

    def test_interface_inicial53(self):
        self.assertEqual(self.app.botoes[5][3]['state'], 'normal')

    def test_reiniciar_jogo(self):
        self.app.clicar_celula(0, 0)
        self.app.reiniciar_jogo()
        self.assertEqual(self.app.botoes[0][0]['state'], 'active')

    def test_sair_jogo(self):
        with self.assertRaises(SystemExit):
            self.app.sair_jogo()
    
    def test_botao_clicado_depois_da_vitoria(self):
        self.app.jogo.jogo_vencido = True
        self.app.clicar_celula(0, 0)
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_botao_clicado_depois_da_derrota(self):
        self.app.jogo.jogo_encerrado = True
        self.app.clicar_celula(0, 0)
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'normal')

    def test_botao_clicado_apos_vitoria_reiniciar(self):
        self.app.jogo.jogo_vencido = True
        self.app.clicar_celula(0, 0)
        self.app.reiniciar_jogo()
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_botao_clicado_apos_derrota_reiniciar(self):
        self.app.jogo.jogo_encerrado = True
        self.app.clicar_celula(0, 0)
        self.app.reiniciar_jogo()
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_descobrir_celula_com_numero(self):
        self.app.jogo.tabuleiro[0][0] = '1'
        self.app.clicar_celula(0, 0)
        self.assertEqual(self.app.botoes[0][0]['state'], 'disabled')

    def test_modo_bandeiraon(self):
        self.app.alternar_modo_bandeira()
        self.assertTrue(self.app.modo_bandeira)

    def test_modo_bandeiraoff(self):
        self.app.alternar_modo_bandeira()
        self.app.alternar_modo_bandeira()
        self.assertFalse(self.app.modo_bandeira)

    def test_colocar_bandeiramodo(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.assertEqual(self.app.jogo.tabuleiro[0][0], 'F')

    def test_remover_bandeiramodo(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.app.clicar_celula(0, 0)
        self.assertEqual(self.app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zonamodo(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.assertNotEqual(self.app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zona(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.assertNotEqual(self.app.jogo.tabuleiro[0][0], '-')
    
    def test_contar_bandeiras_colocadas(self):
        self.app.alternar_modo_bandeira()
        for i in range(5):
            self.app.clicar_celula(i, i)
        self.assertEqual(self.app.jogo.bandeiras_colocadas, 5)

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()

