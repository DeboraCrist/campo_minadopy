import tkinter as tk
import unittest
from UI import JogoCampoMinadoGUI, JogoCampoMinadoTabuleiro
from campo_minado import CampoMinado

class TestCampoMinadoGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = JogoCampoMinadoTabuleiro(self.root, nivel=1)

    def test_clicar_celula(self):
        self.app.clicar_celula(0, 0)
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_clicar_celula_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.clicar_celula(0, 0)
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_clicar_celula_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.clicar_celula(0, 0)
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_atualizar_interface(self):
        self.app.jogo.tabuleiro[0][0] = '1'
        self.app.atualizar_interface()
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['text'], '1')

    def test_atualizar_interface_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.tabuleiro[0][0] = '1'
        app.atualizar_interface()
        botao = app.botoes[0][0]
        self.assertEqual(botao['text'], '1')

    def test_atualizar_interface_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.tabuleiro[0][0] = '1'
        app.atualizar_interface()
        botao = app.botoes[0][0]
        self.assertEqual(botao['text'], '1')

    def teste_perda_jogo_na_primeira_jogada(self):
        self.app.jogo.bombas[0][0] = True
        self.app.clicar_celula(0, 0)
        self.assertFalse(self.app.jogo.jogo_encerrado)
    
    def teste_perda_jogo_na_primeira_jogada_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.bombas[0][0] = True
        app.clicar_celula(0, 0)
        self.assertFalse(app.jogo.jogo_encerrado)

    def teste_perda_jogo_na_primeira_jogada_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.bombas[0][0] = True
        app.clicar_celula(0, 0)
        self.assertFalse(app.jogo.jogo_encerrado)

    def teste_perda_jogo_na_segunda_jogada(self):
        self.app.jogo.bombas[0][0] = True
        self.app.clicar_celula(0, 0)
        self.app.atualizar_interface()
        self.app.jogo.bombas[1][0] = True
        self.app.clicar_celula(1, 0)
        self.assertTrue(self.app.jogo.jogo_encerrado)

    def teste_perda_jogo_na_segunda_jogada_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.bombas[0][0] = True
        app.clicar_celula(0, 0)
        app.atualizar_interface()
        app.jogo.bombas[1][0] = True
        app.clicar_celula(1, 0)
        self.assertTrue(app.jogo.jogo_encerrado)

    def teste_perda_jogo_na_segunda_jogada_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.bombas[0][0] = True
        app.clicar_celula(0, 0)
        app.atualizar_interface()
        app.jogo.bombas[1][0] = True
        app.clicar_celula(1, 0)
        self.assertTrue(app.jogo.jogo_encerrado)

    def test_vitoria_jogo(self):
        for x in range(self.app.jogo.linhas):
            for y in range(self.app.jogo.colunas):
                if not self.app.jogo.bombas[x][y]:
                    self.app.clicar_celula(x, y)
        self.assertTrue(self.app.jogo.jogo_vencido)

    def test_vitoria_jogo_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        for x in range(app.jogo.linhas):
            for y in range(app.jogo.colunas):
                if not app.jogo.bombas[x][y]:
                    app.clicar_celula(x, y)
        self.assertTrue(app.jogo.jogo_vencido)

    def test_vitoria_jogo_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        for x in range(app.jogo.linhas):
            for y in range(app.jogo.colunas):
                if not app.jogo.bombas[x][y]:
                    app.clicar_celula(x, y)
        self.assertTrue(app.jogo.jogo_vencido)

    def test_interface_inicial(self):
        self.assertEqual(self.app.botoes[0][0]['state'], 'normal')

    def test_interface_inicial_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertEqual(app.botoes[0][0]['state'], 'normal')

    def test_interface_inicial_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertEqual(app.botoes[0][0]['state'], 'normal')

    def test_interface_inicial1(self):
        self.assertEqual(self.app.botoes[0][1]['state'], 'normal')

    def test_interface_inicial1_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertEqual(app.botoes[0][1]['state'], 'normal')
        
    def test_interface_inicial1_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertEqual(app.botoes[0][1]['state'], 'normal')

    def test_interface_inicial8(self):
        self.assertEqual(self.app.botoes[7][7]['state'], 'normal')

    def test_interface_inicial8_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertEqual(app.botoes[7][7]['state'], 'normal')

    def test_interface_inicial8_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertEqual(app.botoes[7][7]['state'], 'normal')

    def test_interface_inicial53(self):
        self.assertEqual(self.app.botoes[5][3]['state'], 'normal')

    def test_interface_inicial53_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertEqual(app.botoes[5][3]['state'], 'normal')

    def test_interface_inicial53_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertEqual(app.botoes[5][3]['state'], 'normal')

    def test_reiniciar_jogo(self):
        self.app.clicar_celula(0, 0)
        self.app.reiniciar_jogo()
        self.assertEqual(self.app.botoes[0][0]['state'], 'active')

    def test_reiniciar_jogo_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.clicar_celula(0, 0)
        app.reiniciar_jogo()
        self.assertEqual(app.botoes[0][0]['state'], 'active')

    def test_reiniciar_jogo_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.clicar_celula(0, 0)
        app.reiniciar_jogo()
        self.assertEqual(app.botoes[0][0]['state'], 'active')

    def test_botao_clicado_depois_da_vitoria(self):
        self.app.jogo.jogo_vencido = True
        self.app.clicar_celula(0, 0)
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_botao_clicado_depois_da_vitoria_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.jogo_vencido = True
        app.clicar_celula(0, 0)
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_botao_clicado_depois_da_vitoria_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.jogo_vencido = True
        app.clicar_celula(0, 0)
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'disabled')

    def test_botao_clicado_depois_da_derrota(self):
        self.app.jogo.jogo_encerrado = True
        self.app.clicar_celula(0, 0)
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'normal')

    def test_botao_clicado_depois_da_derrota_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.jogo_encerrado = True
        app.clicar_celula(0, 0)
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'normal')

    def test_botao_clicado_depois_da_derrota_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.jogo_encerrado = True
        app.clicar_celula(0, 0)
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'normal')

    def test_botao_clicado_apos_vitoria_reiniciar(self):
        self.app.jogo.jogo_vencido = True
        self.app.clicar_celula(0, 0)
        self.app.reiniciar_jogo()
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_botao_clicado_apos_vitoria_reiniciar_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.jogo_vencido = True
        app.clicar_celula(0, 0)
        app.reiniciar_jogo()
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_botao_clicado_apos_vitoria_reiniciar_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.jogo_vencido = True
        app.clicar_celula(0, 0)
        app.reiniciar_jogo()
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_botao_clicado_apos_derrota_reiniciar(self):
        self.app.jogo.jogo_encerrado = True
        self.app.clicar_celula(0, 0)
        self.app.reiniciar_jogo()
        botao = self.app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_botao_clicado_apos_derrota_reiniciar_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.jogo_encerrado = True
        app.clicar_celula(0, 0)
        app.reiniciar_jogo()
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_botao_clicado_apos_derrota_reiniciar_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.jogo_encerrado = True
        app.clicar_celula(0, 0)
        app.reiniciar_jogo()
        botao = app.botoes[0][0]
        self.assertEqual(botao['state'], 'active')

    def test_descobrir_celula_com_numero(self):
        self.app.jogo.tabuleiro[0][0] = '1'
        self.app.clicar_celula(0, 0)
        self.assertEqual(self.app.botoes[0][0]['state'], 'disabled')

    def test_descobrir_celula_com_numero_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.jogo.tabuleiro[0][0] = '1'
        app.clicar_celula(0, 0)
        self.assertEqual(app.botoes[0][0]['state'], 'disabled')

    def test_descobrir_celula_com_numero_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.jogo.tabuleiro[0][0] = '1'
        app.clicar_celula(0, 0)
        self.assertEqual(app.botoes[0][0]['state'], 'disabled')

    def test_modo_bandeiraon(self):
        self.app.alternar_modo_bandeira()
        self.assertTrue(self.app.modo_bandeira)

    def test_modo_bandeiraon_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.alternar_modo_bandeira()
        self.assertTrue(app.modo_bandeira)

    def test_modo_bandeiraon_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        self.assertTrue(app.modo_bandeira)

    def test_modo_bandeiraoff(self):
        self.app.alternar_modo_bandeira()
        self.app.alternar_modo_bandeira()
        self.assertFalse(self.app.modo_bandeira)

    def test_modo_bandeiraoff_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.alternar_modo_bandeira()
        app.alternar_modo_bandeira()
        self.assertFalse(app.modo_bandeira)

    def test_modo_bandeiraoff_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        app.alternar_modo_bandeira()
        self.assertFalse(app.modo_bandeira)

    def test_colocar_bandeiramodo(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.assertEqual(self.app.jogo.tabuleiro[0][0], 'F')

    def test_colocar_bandeiramodo_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        self.assertEqual(app.jogo.tabuleiro[0][0], 'F')

    def test_colocar_bandeiramodo_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        self.assertEqual(app.jogo.tabuleiro[0][0], 'F')

    def test_remover_bandeiramodo(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.app.clicar_celula(0, 0)
        self.assertEqual(self.app.jogo.tabuleiro[0][0], '-')

    def test_remover_bandeiramodo_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        app.clicar_celula(0, 0)
        self.assertEqual(app.jogo.tabuleiro[0][0], '-')

    def test_remover_bandeiramodo_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        app.clicar_celula(0, 0)
        self.assertEqual(app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zonamodo(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.assertNotEqual(self.app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zonamodo_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        self.assertNotEqual(app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zonamodo_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        self.assertNotEqual(app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zona(self):
        self.app.alternar_modo_bandeira()
        self.app.clicar_celula(0, 0)
        self.assertNotEqual(self.app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zona_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        self.assertNotEqual(app.jogo.tabuleiro[0][0], '-')

    def test_descobrir_zona_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        app.clicar_celula(0, 0)
        self.assertNotEqual(app.jogo.tabuleiro[0][0], '-')
    
    def test_contar_bandeiras_colocadas(self):
        self.app.alternar_modo_bandeira()
        for i in range(5):
            self.app.clicar_celula(i, i)
        self.assertEqual(self.app.jogo.bandeiras_colocadas, 5)

    def test_contar_bandeiras_colocadas_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        for i in range(5):
            app.clicar_celula(i, i)
        self.assertEqual(app.jogo.bandeiras_colocadas, 5)

    def test_contar_bandeiras_colocadas_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.alternar_modo_bandeira()
        for i in range(5):
            app.clicar_celula(i, i)
        self.assertEqual(app.jogo.bandeiras_colocadas, 5)

    def test_botoes_no_tabuleiro(self):
        for linha in self.app.botoes:
            for botao in linha:
                self.assertTrue(botao.winfo_exists())  

    def test_botao_reiniciar(self):
        self.assertTrue(self.app.reiniciar_button.winfo_exists())

    def test_botao_sair(self):
        self.assertTrue(self.app.sair_button.winfo_exists())

    def test_botao_modo_bandeira(self):
        self.assertTrue(self.app.modo_bandeira_button.winfo_exists())

    def test_label_num_bandeiras(self):
        self.assertTrue(self.app.num_bandeiras_label.winfo_exists())

    def test_botoes_no_tabuleiro_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        for linha in app.botoes:
            for botao in linha:
                self.assertTrue(botao.winfo_exists())  

    def test_botao_reiniciar_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertTrue(app.reiniciar_button.winfo_exists())

    def test_botao_sair_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertTrue(app.sair_button.winfo_exists())

    def test_botao_modo_bandeira_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertTrue(app.modo_bandeira_button.winfo_exists())

    def test_label_num_bandeiras_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertTrue(app.num_bandeiras_label.winfo_exists())

    def test_botoes_no_tabuleiro_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        for linha in app.botoes:
            for botao in linha:
                self.assertTrue(botao.winfo_exists())  

    def test_botao_reiniciar_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertTrue(app.reiniciar_button.winfo_exists())

    def test_botao_sair_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertTrue(app.sair_button.winfo_exists())

    def test_botao_modo_bandeira_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertTrue(app.modo_bandeira_button.winfo_exists())

    def test_label_num_bandeiras_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertTrue(app.num_bandeiras_label.winfo_exists())

    def test_celulas_estao_vazias_inicialmente(self):
        for linha in self.app.botoes:
            for botao in linha:
                self.assertEqual(botao.cget('text'), '', "A célula deve estar vazia inicialmente")

    def test_celulas_estao_vazias_inicialmente_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        for linha in app.botoes:
            for botao in linha:
                self.assertEqual(botao.cget('text'), '', "A célula deve estar vazia inicialmente")

    def test_celulas_estao_vazias_inicialmente_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        for linha in app.botoes:
            for botao in linha:
                self.assertEqual(botao.cget('text'), '', "A célula deve estar vazia inicialmente")

    def test_celulas_estao_vazias_inicialmente_normal(self):
        for linha in self.app.botoes:
            for botao in linha:
                self.assertEqual(botao.cget('state'), 'normal', "O estado da célula deve ser 'normal'")

    def test_celulas_estao_vazias_inicialmente_normal_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        for linha in app.botoes:
            for botao in linha:
                self.assertEqual(botao.cget('state'), 'normal', "O estado da célula deve ser 'normal'")

    def test_celulas_estao_vazias_inicialmente_normal_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        for linha in app.botoes:
            for botao in linha:
                self.assertEqual(botao.cget('state'), 'normal', "O estado da célula deve ser 'normal'")
    
    def test_celulas_estao_vazias_inicialmente_cor(self):
        for linha in self.app.botoes:
            for botao in linha:
                self.assertIn(botao.cget('bg'), {'light gray', '#d9d9d9'}, "A cor de fundo da célula deve ser 'light gray'")
   
    def test_celulas_estao_vazias_inicialmente_cor_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        for linha in app.botoes:
            for botao in linha:
                self.assertIn(botao.cget('bg'), {'light gray', '#d9d9d9'}, "A cor de fundo da célula deve ser 'light gray'")
    
    def test_celulas_estao_vazias_inicialmente_cor_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        for linha in app.botoes:
            for botao in linha:
                self.assertIn(botao.cget('bg'), {'light gray', '#d9d9d9'}, "A cor de fundo da célula deve ser 'light gray'")
    
    def test_alternar_modo_bandeira(self):
        initial_text = self.app.modo_bandeira_button.cget('text')
        self.app.alternar_modo_bandeira()
        new_text = self.app.modo_bandeira_button.cget('text')
        self.assertNotEqual(initial_text, new_text)

    def test_alternar_modo_bandeira_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        initial_text = app.modo_bandeira_button.cget('text')
        app.alternar_modo_bandeira()
        new_text = app.modo_bandeira_button.cget('text')
        self.assertNotEqual(initial_text, new_text)

    def test_alternar_modo_bandeira_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        initial_text = app.modo_bandeira_button.cget('text')
        app.alternar_modo_bandeira()
        new_text = app.modo_bandeira_button.cget('text')
        self.assertNotEqual(initial_text, new_text)

    def test_atualizar_num_bandeiras(self):
        self.app.jogo.bandeiras_colocadas = 5
        self.app.atualizar_num_bandeiras()
        expected_text = f'Bandeiras: 5/{self.app.jogo.num_bombas}'
        self.assertEqual(self.app.num_bandeiras_var.get(), expected_text)

    def test_atualizar_num_bandeiras_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.app.jogo.bandeiras_colocadas = 5
        self.app.atualizar_num_bandeiras()
        expected_text = f'Bandeiras: 5/{self.app.jogo.num_bombas}'
        self.assertEqual(self.app.num_bandeiras_var.get(), expected_text)

    def test_atualizar_num_bandeiras_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.app.jogo.bandeiras_colocadas = 5
        self.app.atualizar_num_bandeiras()
        expected_text = f'Bandeiras: 5/{self.app.jogo.num_bombas}'
        self.assertEqual(self.app.num_bandeiras_var.get(), expected_text)

    def test_atualizar_num_bandeiras_initial_state(self):
        expected_text = f'Bandeiras: 0/10'  
        initial_text = self.app.num_bandeiras_var.get()
        self.assertEqual(initial_text, expected_text)

    def test_atualizar_num_bandeiras_initial_state_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        expected_text = f'Bandeiras: 0/30'  
        initial_text = app.num_bandeiras_var.get()
        self.assertEqual(initial_text, expected_text)

    def test_atualizar_num_bandeiras_initial_state_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        expected_text = f'Bandeiras: 0/100'  
        initial_text = app.num_bandeiras_var.get()
        self.assertEqual(initial_text, expected_text)

    def test_alternar_modo_bandeira_initia(self):
        expected_text = "Modo Bandeira"
        initial_text = self.app.modo_bandeira_button.cget('text')
        self.assertEqual(initial_text, expected_text)

    def test_alternar_modo_bandeira_initial_state_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        expected_text = "Modo Bandeira"
        initial_text = app.modo_bandeira_button.cget('text')
        self.assertEqual(initial_text, expected_text)

    def test_alternar_modo_bandeira_initial_state_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        expected_text = "Modo Bandeira"
        initial_text = app.modo_bandeira_button.cget('text')
        self.assertEqual(initial_text, expected_text)

    def test_reiniciar_jogo_pelafuncao(self):
        self.app.reiniciar_jogo()

    def test_reiniciar_jogo_pelafuncao_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.reiniciar_jogo()

    def test_reiniciar_jogo_pelafuncao_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.reiniciar_jogo()

    def test_tempo_initial_state(self):
        self.assertEqual(self.app.tempo_var.get(), "00:00")

    def test_tempo_initial_state_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        self.assertEqual(self.app.tempo_var.get(), "00:00")

    def test_tempo_initial_state_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        self.assertEqual(self.app.tempo_var.get(), "00:00")

    def test_mostrar_fim_de_jogo(self):
        self.app.mostrar_fim_de_jogo("Parabéns! Você venceu!")
        
    def test_mostrar_fim_de_jogo_nivel2(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=2)
        app.mostrar_fim_de_jogo("Parabéns! Você venceu!")

    def test_mostrar_fim_de_jogo_nivel3(self):
        app = JogoCampoMinadoTabuleiro(self.root, nivel=3)
        app.mostrar_fim_de_jogo("Parabéns! Você venceu!")    

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()

