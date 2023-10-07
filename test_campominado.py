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
        nivel = 1
        jogo = CampoMinado(nivel)
        bombas_colocadas = sum(row.count(True) for row in jogo.bombas)
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

if __name__ == '__main__':
    unittest.main()
