import unittest
from campo_minado import CampoMinado  
import datetime

class TesteHistoricoCampoMinado(unittest.TestCase):
    
    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_historico_vazio_no_inicio(self):
        historico = self.jogo.consultar_historico()
        self.assertEqual(historico, [])

    def test_historico_armazena_resultados(self):
        self.jogo.jogo_vencido = True
        self.jogo.resultados = []  
        self.jogo.reiniciar_jogo()  
        resultados = self.jogo.consultar_historico()
        self.assertEqual(len(resultados), 1)

    def test_historico_nivel(self):
        self.jogo.jogo_vencido = True
        self.jogo.resultados = []  
        self.jogo.reiniciar_jogo()  
        resultados = self.jogo.consultar_historico()
        resultado = resultados[0]
        self.assertEqual(resultado['nivel'], 1)

    def test_historico_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        jogo.resultados = []  
        jogo.reiniciar_jogo()  
        resultados = jogo.consultar_historico()
        resultado = resultados[0]
        self.assertEqual(resultado['nivel'], 2)

    def test_historico_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        jogo.resultados = []  
        jogo.reiniciar_jogo()  
        resultados = jogo.consultar_historico()
        resultado = resultados[0]
        self.assertEqual(resultado['nivel'], 3)

    def test_historico_data(self):
        self.jogo.jogo_vencido = True
        self.jogo.resultados = []  
        self.jogo.reiniciar_jogo()  
        resultados = self.jogo.consultar_historico()
        resultado = resultados[0]
        self.assertTrue(isinstance(resultado['data'], datetime.datetime))

    def test_historico_vitoria(self):
        self.jogo.resultados = []  
        self.jogo.jogo_vencido = True  
        self.jogo.reiniciar_jogo() 
        resultados = self.jogo.consultar_historico()
        resultado = resultados[0]
        self.assertTrue(resultado['vitoria'])

    def test_historico_derrota(self):
        jogo = CampoMinado(1)
        jogo.resultados = []  
        jogo.jogo_vencido = False  
        jogo.reiniciar_jogo() 
        resultados = jogo.consultar_historico()
        resultado = resultados[0]
        self.assertFalse(resultado['vitoria'])

    def test_historico_se_limpa_apos_reiniciar_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = False
        jogo.resultados = []  
        jogo.reiniciar_jogo() 
        resultados = jogo.consultar_historico()
        self.assertEqual(len(resultados), 1)

    def test_historico_se_limpa_apos_reiniciar_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = False
        jogo.resultados = []  
        jogo.reiniciar_jogo() 
        resultados = jogo.consultar_historico()
        self.assertEqual(len(resultados), 1)

    def test_multiplos_resultados_no_historico(self):
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo()  
        historico = self.jogo.consultar_historico()
        self.assertEqual(len(historico), 2)

    def test_multiplos_resultados_no_historico10(self):
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo() 
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo()   
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo()  
        self.jogo.reiniciar_jogo()  
        historico = self.jogo.consultar_historico()
        self.assertEqual(len(historico), 10)

if __name__ == '__main__':
    unittest.main()
