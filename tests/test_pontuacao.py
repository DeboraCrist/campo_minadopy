import time
import unittest
from campo_minado import CampoMinado 
import datetime

class TestCampoMinado(unittest.TestCase):
    def setUp(self):
        self.game = CampoMinado(nivel=1)

    def test_pontuacao_derrota_mensagem(self):
        campo = CampoMinado(1)
        campo.realizar_primeira_jogada(3, 3)
        campo.descobrir_zona(4, 4)  
        pontuacao = campo.calcular_pontuacao()
        self.assertTrue(pontuacao.startswith("Você perdeu"))

    def test_pontuacao_derrota_tempo_mensagem(self):
        campo = CampoMinado(1)
        campo.realizar_primeira_jogada(3, 3)
        campo.descobrir_zona(4, 4) 
        pontuacao = campo.calcular_pontuacao()
        self.assertTrue(pontuacao.startswith("Você perdeu em"))

    def test_pontuacao_derrota_tempo_segundos(self):
        campo = CampoMinado(1)
        campo.realizar_primeira_jogada(3, 3)
        campo.descobrir_zona(4, 4) 
        pontuacao = campo.calcular_pontuacao()
        self.assertTrue("segundos" in pontuacao)

    def test_calculate_score_win(self):
        game = CampoMinado(nivel=1)
        game.start_time = datetime.datetime.now()
        time.sleep(2)  
        game.jogo_vencido = True
        score = game.calcular_pontuacao()
        self.assertEqual(score, "Você venceu em 2.00 segundos.")

    def test_calculate_score_loss(self):
        game = CampoMinado(nivel=2)
        game.start_time = datetime.datetime.now()
        time.sleep(3)  
        game.jogo_encerrado = True
        score = game.calcular_pontuacao()
        self.assertEqual(score, "Você perdeu em 3.00 segundos.")

    def test_pontuacao_vitoria_tempo_mensagem(self):
        game = CampoMinado(1)
        game.start_time = datetime.datetime.now()
        time.sleep(4)
        game.jogo_vencido = True
        score = game.calcular_pontuacao()
        self.assertTrue(score.startswith("Você venceu em"))

    def test_pontuacao_vitoria_tempo_segundos(self):
        game = CampoMinado(1)
        game.start_time = datetime.datetime.now()
        time.sleep(5)  
        game.jogo_vencido = True
        score = game.calcular_pontuacao()
        self.assertTrue("segundos" in score)

    def test_pontuacao_loss_instant_loss(self):
        game = CampoMinado(1)
        game.start_time = datetime.datetime.now()
        game.jogo_encerrado = True
        score = game.calcular_pontuacao()
        self.assertTrue(score.startswith("Você perdeu em 0.00 segundos."))

    def test_pontuacao_vitoria_zero_seconds(self):
        game = CampoMinado(1)
        game.start_time = datetime.datetime.now()
        game.jogo_vencido = True
        score = game.calcular_pontuacao()
        self.assertTrue(score.startswith("Você venceu em 0.00 segundos."))

    def test_pontuacao_custom_time_win(self):
        game = CampoMinado(1)
        custom_start_time = datetime.datetime.now() - datetime.timedelta(seconds=10)  
        game.start_time = custom_start_time
        game.jogo_vencido = True
        score = game.calcular_pontuacao()
        self.assertEqual(score, "Você venceu em 10.00 segundos.")

    def test_pontuacao_custom_time_loss(self):
        game = CampoMinado(1)
        custom_start_time = datetime.datetime.now() - datetime.timedelta(seconds=15)  
        game.start_time = custom_start_time
        game.jogo_encerrado = True
        score = game.calcular_pontuacao()
        self.assertEqual(score, "Você perdeu em 15.00 segundos.")

    def tearDown(self):
        self.game = None

if __name__ == '__main__':
    unittest.main()
