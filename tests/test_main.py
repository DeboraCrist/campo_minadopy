# import unittest
# from unittest.mock import patch
# from io import StringIO
# from main import main

# class TestMain(unittest.TestCase):

#     @patch('builtins.input', side_effect=['1', 'D', 'Q'])
#     def test_main_game_quit(self, mock_input):
#         output_buffer = StringIO()
#         with patch('sys.stdout', new=output_buffer):
#             main()
#         output_text = output_buffer.getvalue().strip()
#         self.assertEqual(output_text, "Bem-vindo ao Campo Minado!\nSaindo do jogo.")



#     @patch('builtins.input', side_effect=['1', 'D', 'N', 'Q'])
#     def test_main_game_restart_quit(self, mock_input):
#         output_buffer = StringIO()
#         with patch('sys.stdout', new=output_buffer):
#             main()
#         output_text = output_buffer.getvalue().strip()
#         self.assertIn("Reiniciando o jogo.", output_text)
#         self.assertIn("Saindo do jogo.", output_text)

# if __name__ == '__main__':
#     unittest.main()
