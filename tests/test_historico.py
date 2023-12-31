import io
import unittest

from mock import patch
from campo_minado import CampoMinado  
class TesteHistoricoCampoMinado(unittest.TestCase):
    
    def setUp(self):
        self.jogo = CampoMinado(1) 

    def test_historico_inicial_vazio(self):
        self.assertEqual(len(self.jogo.resultados), 0)

    def test_historico_inicial_vazio_nivel2(self):
        jogo = CampoMinado(2) 
        self.assertEqual(len(jogo.resultados), 0)
    
    def test_historico_inicial_vazio_nivel3(self):
        jogo = CampoMinado(3) 
        self.assertEqual(len(jogo.resultados), 0)

    def test_guardar_resultados(self):
        self.jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.jogo.guardar_resultado()
            with open('historico.txt', 'r') as arquivo:
                resultado_gravado = arquivo.read()
            self.assertIn("Vitória", resultado_gravado)

    def test_guardar_resultados_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            jogo.guardar_resultado()
            with open('historico.txt', 'r') as arquivo:
                resultado_gravado = arquivo.read()
            self.assertIn("Vitória", resultado_gravado)

    def test_guardar_resultados_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            jogo.guardar_resultado()
            with open('historico.txt', 'r') as arquivo:
                resultado_gravado = arquivo.read()
            self.assertIn("Vitória", resultado_gravado)

    def test_guardar_resultado_mensagem_saida(self):
        self.jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.jogo.guardar_resultado()
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_guardar_resultado_mensagem_saida_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            jogo.guardar_resultado()
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_guardar_resultado_mensagem_saida_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            jogo.guardar_resultado()
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_guardar_resultado_derrota(self):
        self.jogo.jogo_encerrado = True
        with patch('sys.stdout', new_callable=io.StringIO):
            self.jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Derrota", resultado_gravado)

    def test_guardar_resultado_derrota_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_encerrado = True
        with patch('sys.stdout', new_callable=io.StringIO):
            jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Derrota", resultado_gravado)

    def test_guardar_resultado_derrota_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_encerrado = True
        with patch('sys.stdout', new_callable=io.StringIO):
            jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Derrota", resultado_gravado)

    def test_guardar_resultado_jogo_nao_encerrado(self):
        self.jogo.jogo_vencido = False
        self.jogo.jogo_encerrado = False
        with patch('sys.stdout', new_callable=io.StringIO):
            self.jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Jogo não encerrado", resultado_gravado)

    def test_guardar_resultado_jogo_nao_encerrado_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = False
        jogo.jogo_encerrado = False
        with patch('sys.stdout', new_callable=io.StringIO):
            jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Jogo não encerrado", resultado_gravado)

    def test_guardar_resultado_jogo_nao_encerrado_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = False
        jogo.jogo_encerrado = False
        with patch('sys.stdout', new_callable=io.StringIO):
            jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Jogo não encerrado", resultado_gravado)

    def test_guardar_resultado_mensagem_saida_nao_vazia(self):
        self.jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print("Isso é um teste")
            self.jogo.guardar_resultado()
        self.assertEqual(mock_stdout.getvalue().strip(), "Isso é um teste")
    
    def test_guardar_resultado_mensagem_saida_nao_vazia_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print("Isso é um teste")
            jogo.guardar_resultado()
        self.assertEqual(mock_stdout.getvalue().strip(), "Isso é um teste")

    def test_guardar_resultado_mensagem_saida_nao_vazia_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print("Isso é um teste")
            jogo.guardar_resultado()
        self.assertEqual(mock_stdout.getvalue().strip(), "Isso é um teste")

    def test_guardar_resultado(self):
        self.jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO):
            self.jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Nível: 1", resultado_gravado)

    def test_guardar_resultado_nivel2(self):
        campo_minado = CampoMinado(2)
        campo_minado.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO):
            campo_minado.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Nível: 2", resultado_gravado)

    def test_guardar_resultado_nivel3(self):
        campo_minado = CampoMinado(3)
        campo_minado.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO):
            campo_minado.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Nível: 3", resultado_gravado)

    def test_guardar_resultado_vitoria_outra_data(self):
        self.jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO):
           self.jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Data e Hora:", resultado_gravado)

    def test_guardar_resultado_vitoria_outra_data_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO):
           jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Data e Hora:", resultado_gravado)

    def test_guardar_resultado_vitoria_outra_data_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        with patch('sys.stdout', new_callable=io.StringIO):
           jogo.guardar_resultado()
        with open('historico.txt', 'r') as arquivo:
            resultado_gravado = arquivo.read()
        self.assertIn("Data e Hora:", resultado_gravado)

    def test_obter_resultados(self):
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        self.jogo.resultados = [resultado1, resultado2, resultado3]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

    def test_obter_resultados_nivel2(self):
        jogo = CampoMinado(2)
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        self.jogo.resultados = [resultado1, resultado2, resultado3]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

    def test_obter_resultados_nivel3(self):
        jogo = CampoMinado(3)
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        self.jogo.resultados = [resultado1, resultado2, resultado3]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

    def test_obter_resultados_vitoria(self):
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        self.jogo.resultados = [resultado]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_vitoria_nivel2(self):
        jogo = CampoMinado(2)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        jogo.resultados = [resultado]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])
    
    def test_obter_resultados_vitoria_nivel3(self):
        jogo = CampoMinado(3)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        jogo.resultados = [resultado]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_derrota_nivel1(self):
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Derrota\n"
        self.jogo.resultados = [resultado]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_derrota_nivel2(self):
        jogo = CampoMinado(2)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Derrota\n"
        jogo.resultados = [resultado]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_derrota_nivel3(self):
        jogo = CampoMinado(3)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Derrota\n"
        self.jogo.resultados = [resultado]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_jogo_nao_encerrado(self):
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        self.jogo.resultados = [resultado]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_jogo_nao_encerrado_nivel2(self):
        jogo = CampoMinado(2)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        jogo.resultados = [resultado]

        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    
    def test_obter_resultados_jogo_nao_encerrado_nivel3(self):
        jogo = CampoMinado(3)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        jogo.resultados = [resultado]

        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_multiple_results(self):
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        self.jogo.resultados = [resultado1, resultado2, resultado3]
        results = self.jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

    def test_obter_resultados_multiple_results_nivel2(self):
        jogo = CampoMinado(2)
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        jogo.resultados = [resultado1, resultado2, resultado3]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

    def test_obter_resultados_multiple_results_nivel3(self):
        jogo = CampoMinado(3)
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        jogo.resultados = [resultado1, resultado2, resultado3]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

if __name__ == '__main__':
    unittest.main()
