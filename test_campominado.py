import unittest
from campo_minado import CampoMinado

class TestCampoMinado(unittest.TestCase):
    def test_nivel_facil(self):
        jogo = CampoMinado(1)
        self.assertEqual(jogo.nivel, 1)

    def test_tamanho_nivel_facil(self):
        jogo = CampoMinado(1)
        self.assertEqual(jogo.tamanho, 8)

    def test_num_bombas_nivel_facil(self):
        jogo = CampoMinado(1)
        self.assertEqual(jogo.num_bombas, 10)

    def test_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.nivel, 2)

    def test_tamanho_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.tamanho, 10)

    def test_num_bombas_nivel_intermediario(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.num_bombas, 30)

    def test_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.nivel, 3)

    def test_tamanho_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.tamanho, 24)

    def test_num_bombas_nivel_dificil(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.num_bombas, 100)

    def test_colocar_bombas(self):
        jogo = CampoMinado(1)
        bombas_colocadas = sum(sum(1 for bomba in linha if bomba) for linha in jogo.bombas)
        self.assertEqual(bombas_colocadas, jogo.num_bombas)

    def test_reiniciar_jogo(self):
        jogo = CampoMinado(1)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_encerrado, False)

    def test_reiniciar_jogo_vencido(self):
        jogo = CampoMinado(1)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.jogo_vencido, False)

    def test_reiniciar_jogo_bandeiras(self):
        jogo = CampoMinado(1)
        jogo.reiniciar_jogo()
        self.assertEqual(jogo.bandeiras_colocadas, 0)

    def test_escolherNivelDeDificuldade(self):
        jogo = CampoMinado(1)
        self.assertEqual(jogo.nivel, 1)

    def test_escolherNivelDeDificuldade2(self):
        jogo = CampoMinado(2)
        self.assertEqual(jogo.nivel, 2)

    def test_escolherNivelDeDificuldade3(self):
        jogo = CampoMinado(3)
        self.assertEqual(jogo.nivel, 3)

    def test_jogoNaoEncerradoNaInicializacao(self):
        jogo = CampoMinado(1)
        self.assertEqual(jogo.jogo_encerrado, False)

    def test_tabuleiroInicializadoComHifens(self):
        jogo = CampoMinado(1)
        self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))

    def mostrar_tabuleiro(self):
        for row in self.tabuleiro:
            print(" ".join(row))

    def test_colocar_bandeira(self):
        jogo = CampoMinado(1)
        jogo.colocar_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], 'F')

    def test_removerBandeira(self):
        jogo = CampoMinado(1)
        jogo.colocar_bandeira(0, 0)
        jogo.remover_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], '-')

    def test_removerBandeiraDeCelulaSemBandeira(self):
        jogo = CampoMinado(1)
        jogo.remover_bandeira(0, 0)
        self.assertEqual(jogo.tabuleiro[0][0], '-')
    
    def test_revelarBombas(self):
        jogo = CampoMinado(1)
        jogo.bombas[0][0] = True
        jogo.revelar_bombas()

        self.assertEqual(jogo.tabuleiro[0][0], 'B')
        
    # def test_derrotaAoDescobrirBomba(self):
    #     jogo = CampoMinado(1)

    #     # Set a bomb at cell (0, 0) for testing
    #     jogo.bombas[0][0] = True

    #     # Uncover the bomb cell using the descobrir_celula method
    #     jogo.descobrir_celula(0, 0)

    #     # Check if the game is marked as "encerrado" (jogo_encerrado = True)
    #     self.assertEqual(jogo.jogo_encerrado, True)

    # def test_jogoNaoVencidoAposDescobrirBomba(self):
    #     jogo = CampoMinado(1)
    #     jogo.tabuleiro[0][0] = 'B'
    #     jogo.descobrir_celula(0, 0)
    #     self.assertEqual(jogo.jogo_vencido, False)

    # def test_vitoria(self):
    #     jogo = CampoMinado(1)
    #     # Configurar o tabuleiro de tal forma que todas as células não sejam bombas
    #     # e todas as células não bombas sejam reveladas
    #     jogo.tabuleiro = [['-' for _ in range(jogo.tamanho)] for _ in range(jogo.tamanho)]
    #     jogo.bombas = [[False for _ in range(jogo.tamanho)] for _ in range(jogo.tamanho)]
    #     jogo.jogo_vencido = False
    #     jogo.descobrir_celula(0, 0)  # Simular a revelação de todas as células não bombas
    #     self.assertEqual(jogo.jogo_vencido, True)

    # def test_naoPermitirDescobrirComBandeira(self):
    #     jogo = CampoMinado(1)
    #     jogo.colocar_bandeira(0, 0)
    #     jogo.descobrir_celula(0, 0)
    #     self.assertEqual(jogo.tabuleiro[0][0], 'P')

    # def test_jogoNaoVencidoAoRevelarBomba(self):
    #     jogo = CampoMinado(1)
    #     jogo.tabuleiro[0][0] = 'B'
    #     jogo.descobrir_celula(0, 0)
    #     self.assertEqual(jogo.jogo_vencido, False)

    def test_jogoNaoVencidoAoColocarBandeiraEmTodasAsBombas(self):
        jogo = CampoMinado(1)
        for i in range(jogo.tamanho):
            for j in range(jogo.tamanho):
                if jogo.tabuleiro[i][j] == 'B':
                    jogo.colocar_bandeira(i, j)
        self.assertEqual(jogo.jogo_vencido, False)

    # def test_desvendarCelulaAposRemoverBandeira(self):
    #     jogo = CampoMinado(1)
    #     jogo.colocar_bandeira(0, 0)
    #     jogo.remover_bandeira(0, 0)
    #     jogo.descobrir_celula(0, 0)
    #     self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    # def test_impedirAcaoDeBandeiraEmZonaRevelada(self):
    #     jogo = CampoMinado(1)
    #     jogo.descobrir_celula(0, 0)
    #     jogo.colocar_bandeira(0, 0)
    #     self.assertEqual(jogo.tabuleiro[0][0], '-')

    # def test_descobrirZona(self):
    #     jogo = CampoMinado(1)
    #     jogo.descobrir_celula(0, 0)
    #     self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    # def test_reiniciarJogo_RedefinirTabuleiroParaEstadoInicial(self):
    #     jogo = CampoMinado(1)
    #     jogo.descobrir_celula(0, 0)
    #     jogo.reiniciar_jogo()
    #     self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))

    # def test_reiniciarJogo_JogoEncerradoFalso(self):
    #     jogo = CampoMinado(1)
    #     jogo.descobrir_celula(0, 0)
    #     jogo.reiniciar_jogo()
    #     self.assertEqual(jogo.jogo_encerrado, False)

    # def test_reiniciarJogo_JogoVencidoFalso(self):
    #     jogo = CampoMinado(1)
    #     jogo.descobrir_celula(0, 0)
    #     jogo.reiniciar_jogo()
    #     self.assertEqual(jogo.jogo_vencido, False)

    def test_zonasCobertasIniciaisSemBandeiras(self):
        jogo = CampoMinado(1)
        self.assertEqual(jogo.bandeiras_colocadas, 0)

    def test_distribuicaoAleatoriaBombasNivelFacil(self):
        jogo = CampoMinado(1)
        bombas_colocadas = sum(row.count(True) for row in jogo.bombas)
        expected_bombas = jogo.num_bombas
        error_margin = 2 
        self.assertLessEqual(abs(bombas_colocadas - expected_bombas), error_margin)

    def test_distribuicaoAleatoriaBombasNivelIntermediario(self):
        jogo = CampoMinado(2)
        bombas_colocadas = sum(row.count(True) for row in jogo.bombas)
        expected_bombas = jogo.num_bombas
        error_margin = 2 
        self.assertLessEqual(abs(bombas_colocadas - expected_bombas), error_margin)

    
    def test_distribuicaoAleatoriaBombasNivelDificil(self):
        jogo = CampoMinado(3)
        bombas_colocadas = sum(row.count(True) for row in jogo.bombas)
        expected_bombas = jogo.num_bombas
        error_margin = 2  
        self.assertLessEqual(abs(bombas_colocadas - expected_bombas), error_margin)

    # def test_reiniciarJogoVencidocomDescoberta(self):
    #     jogo = CampoMinado(1)
    #     jogo.tabuleiro = [['-' for _ in range(jogo.tamanho)] for _ in range(jogo.tamanho)]
    #     jogo.jogo_vencido = True
    #     jogo.descobrir_celula(0, 0)
    #     jogo.reiniciar_jogo()
    #     self.assertEqual(jogo.jogo_vencido, True)

    # def test_testNumeroDeBandeirasNaoExcedeTotalDeCelulas(self):
    #     jogo = CampoMinado(1)
    #     total_celulas = jogo.tamanho ** 2
    #     jogo.colocar_bandeira(0, 0)
    #     self.assertLessEqual(jogo.bandeiras_colocadas, total_celulas)

    # def test_testColocarBandeirasIgualAoNumeroDeBombas(self):
    #     jogo = CampoMinado(1)
    #     total_bombas = jogo.num_bombas
    #     for i in range(jogo.tamanho):
    #         for j in range(jogo.tamanho):
    #             if jogo.tabuleiro[i][j] == 'B':
    #                 jogo.colocar_bandeira(i, j)
    #     self.assertEqual(jogo.bandeiras_colocadas, total_bombas)

    # def test_testJogoNaoEstaEmEstadoInicial(self):
    #     jogo = CampoMinado(1)
    #     jogo.colocar_bandeira(0, 0)
    #     self.assertNotEqual(jogo.tabuleiro[0][0], '-')

    # def test_testReiniciarJogo(self):
    #     jogo = CampoMinado(1)
    #     jogo.colocar_bandeira(0, 0)
    #     jogo.reiniciar_jogo()
    #     self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))
    
    # def test_testReiniciarJogoEmMeioAoJogo(self):
    #     jogo = CampoMinado(1)
    #     jogo.colocar_bandeira(0, 0)
    #     jogo.descobrir_celula(1, 1)
    #     jogo.reiniciar_jogo()
    #     self.assertTrue(all(cell == '-' for row in jogo.tabuleiro for cell in row))
    
    # def test_testBombasNaoPodemSerColocadasNaPrimeiraZonaRevelada(self):
    #     jogo = CampoMinado(1)
    #     jogo.descobrir_celula(0, 0)
    #     jogo.colocar_bandeira(1, 1)
    #     self.assertNotEqual(jogo.tabuleiro[1][1], 'B')


if __name__ == '__main__':
    unittest.main()
