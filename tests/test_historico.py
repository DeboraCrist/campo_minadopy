import unittest
from campo_minado import CampoMinado  
class TesteHistoricoCampoMinado(unittest.TestCase):
    
    def setUp(self):
        self.jogo = CampoMinado(1) 
    
    def test_historico_apos_vitoria(self):
        jogo = CampoMinado(1)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_apos_vitoria_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)
    
    def test_historico_apos_vitoria_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_apos_derrota(self):
        jogo = CampoMinado(1)
        jogo.jogo_encerrado = True
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_apos_derrota_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_encerrado = True
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_apos_derrota_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_encerrado = True
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_apos_jogo_nao_encerrado(self):
        jogo = CampoMinado(1)
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_apos_jogo_nao_encerrado_nivel2(self):
        jogo = CampoMinado(2)
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_apos_jogo_nao_encerrado_nivel3(self):
        jogo = CampoMinado(3)
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)

    def test_historico_conteudo_vitoria(self):
        jogo = CampoMinado(1)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()
        resultado_esperado = "Vitória"
        self.assertIn(resultado_esperado, jogo.resultados[0])

    def test_historico_conteudo_vitoria_nivel2(self):
        jogo = CampoMinado(2)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()
        resultado_esperado = "Vitória"
        self.assertIn(resultado_esperado, jogo.resultados[0])

    def test_historico_conteudo_vitoria_nivel3(self):
        jogo = CampoMinado(3)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()
        resultado_esperado = "Vitória"
        self.assertIn(resultado_esperado, jogo.resultados[0])

    def test_historico_conteudo_derrota(self):
        jogo = CampoMinado(1)
        jogo.reiniciar_jogo()
        jogo.jogo_encerrado = True
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)
        resultado_esperado = "Derrota"
        self.assertIn(resultado_esperado, jogo.resultados[0])

    def test_historico_apos_jogo_nao_encerrado(self):
        jogo = CampoMinado(1)
        jogo.guardar_resultado()
        self.assertEqual(len(jogo.resultados), 1)
        resultado_esperado = "Jogo não encerrado"
        self.assertIn(resultado_esperado, jogo.resultados[0])

    def test_historico_multiplas_partidas(self):
        self.jogo.jogo_vencido = True
        self.jogo.guardar_resultado()

        self.jogo.reiniciar_jogo()
        self.jogo.jogo_encerrado = True
        self.jogo.guardar_resultado()

        self.jogo.reiniciar_jogo()
        self.jogo.jogo_vencido = True
        self.jogo.guardar_resultado()

        self.assertEqual(len(self.jogo.resultados), 3)

    def test_historico_multiplas_partidas_DerrotaouVitoria(self):
        jogo = CampoMinado(1)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()

        jogo.reiniciar_jogo()
        jogo.jogo_encerrado = True
        jogo.guardar_resultado()

        jogo.reiniciar_jogo()
        jogo.jogo_vencido = True
        jogo.guardar_resultado()

        resultados_esperados = ["Vitória", "Derrota", "Vitória"]
        for resultado in resultados_esperados:
            encontrado = False
            for registro in jogo.resultados:
                if resultado in registro:
                    encontrado = True
                    break
            self.assertTrue(encontrado, f"Resultado '{resultado}' não encontrado nos registros.")

    def test_historico_apos_reiniciar(self):
        jogo = CampoMinado(1)
        jogo.jogo_vencido = True
        jogo.guardar_resultado()
        jogo.reiniciar_jogo()
        self.assertEqual(len(jogo.resultados), 1, "O histórico não foi limpo após reiniciar o jogo.")

    def test_historico_inicial_vazio(self):
        jogo = CampoMinado(1)
        self.assertEqual(len(jogo.resultados), 0)

    def test_historico_nao_limpo_apos_sair(self):
        jogo = CampoMinado(1)
        jogo.guardar_resultado()
        jogo.sair()
        self.assertEqual(len(jogo.resultados), 1)

    def test_obter_resultados(self):
        jogo = CampoMinado(nivel=1)
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        jogo.resultados = [resultado1, resultado2, resultado3]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

    def test_obter_resultados_vitoria(self):
        jogo = CampoMinado(nivel=1)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        jogo.resultados = [resultado]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_derrota(self):
        jogo = CampoMinado(nivel=1)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Derrota\n"
        jogo.resultados = [resultado]
        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_jogo_nao_encerrado(self):
        jogo = CampoMinado(nivel=1)
        resultado = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        jogo.resultados = [resultado]

        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado])

    def test_obter_resultados_multiple_results(self):
        jogo = CampoMinado(nivel=1)
        resultado1 = "Data e Hora: 2023-10-15 12:00:00\nNível: 1\nResultado: Vitória\n"
        resultado2 = "Data e Hora: 2023-10-15 13:00:00\nNível: 1\nResultado: Derrota\n"
        resultado3 = "Data e Hora: 2023-10-15 14:00:00\nNível: 1\nResultado: Jogo não encerrado\n"
        jogo.resultados = [resultado1, resultado2, resultado3]

        results = jogo.obter_resultados()
        self.assertEqual(results, [resultado1, resultado2, resultado3])

    def test_verificar_resultados_no_results(self):
        expected_output = "Nenhum resultado disponível."
        with self.subTest():
            self.assertEqual(self.jogo.verificar_resultados(), expected_output)

    def test_verificar_resultados_with_results(self):
        self.jogo.guardar_resultado()
        self.jogo.guardar_resultado()
        expected_output = "Resultados obtidos:\nResultado 1:\n"
        expected_output += "Resultado 2:\n"

        with self.subTest():
            actual_output = self.jogo.verificar_resultados()
            for substring in expected_output.split('\n'):
                self.assertIn(substring, actual_output)


if __name__ == '__main__':
    unittest.main()
