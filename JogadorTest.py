import unittest
from unittest.mock import patch
from Jogador import Jogador


class JogadorTest(unittest.TestCase):
    
    def setUp(self):
      self.monte_descarte = []
      self.monte_compra = []
    


    def test_selecionar(self):
        pass

#####################################################################

    def test_comprar_ct1(self):
      jogador = Jogador(cartas = [])
      jogador.comprar()

    def test_comprar_ct2(self):
      jogador = Jogador(cartas = [])
      jogador.comprar()        

    def test_comprar_ct3(self):
      jogador = Jogador(cartas = [])
      jogador.comprar()        

    def test_comprar_ct4(self):
      jogador = Jogador(cartas = [])
      jogador.comprar()        

    def test_comprar_ct5(self):
      jogador = Jogador(cartas = [])
      jogador.comprar()        

    def test_comprar_ct6(self):
      jogador = Jogador(cartas = [])
      jogador.comprar()        

#####################################################################

    @patch('builtins.input', side_effect=[])
    def test_escolher_carta_possivel(self, mock_inputs):
        pass

#####################################################################

    def test_jogar(self):
      jogador = Jogador(cartas = [])
      jogador.jogar()
      # checa monte de carta
      self.assertEqual()
      # checa mao do jogador
      self.assertEqual()

      

#####################################################################
    @patch('builtins.input', side_effect=['amarelo'])
    def test_escolher_cor_de_coringa1(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'amarelo')

    @patch('builtins.input', side_effect=['321', '45', 'verde'])
    def test_escolher_cor_de_coringa2(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'verde')
    
    @patch('builtins.input', side_effect=['', 'vermelho'])
    def test_escolher_cor_de_coringa3(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'vermelho')
    
    @patch('builtins.input', side_effect=['llllll', 'azul'])
    def test_escolher_cor_de_coringa4(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'azul')

#####################################################################




if __name__ == '__main__':
    unittest.main()