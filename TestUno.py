import unittest
from unittest import mock
from Gerenciador import Gerenciador
from Jogador import Jogador
from Baralho import Carta
from Baralho import Monte
from unittest.mock import patch

class TestUno(unittest.TestCase):
  def setUp(self):
    jogadores = [Jogador([Carta('preto', 'escolhacor'), Carta('verde', 'reverso'), Carta('amarelo', 'pula'), Carta('vermelho', '4')]),
      Jogador([Carta('verde', '+2'), Carta('preto', '+4'), Carta('preto', 'escolhacor')]),
      Jogador([Carta('verde', '8'), Carta('amarelo', 'pula'), Carta('verde', '7')])
    ]
    self.gerenciador = Gerenciador(True, jogadores, 
                                  [Carta('vermelho', '5'), Carta('verde', '6'), Carta('azul', '5'),Carta('azul', '8'),
                                  Carta('preto', 'escolhacor'), Carta('amarelo', '4'), Carta('vermelho', '2'), Carta('azul', '1'),
                                  Carta('preto', '+4'), Carta('verde', '5'), Carta('azul', '3'), Carta('verde', '+2'),
                                  Carta('vermelho', '5'), Carta('verde', '6'), Carta('azul', '5'),Carta('azul', '8')], 
                                  [Carta('vermelho', '4')])

  @patch('builtins.input', side_effect = ['1', 'verde', '1', '1', '1', '1', 'amarelo', '1', '3', '1', 'verde', 'fim'])
  def test_case1(self, mock_input):
    #given 
    initial_hands = [len(j.cartas) for j in self.gerenciador.jogadores]
    
    #when
    res = self.gerenciador.gerenciarJogo()
    
    #then
    self.assertEqual(mock_input(), 'fim')
    self.assertTrue(self.gerenciador.TERMINAROJOGO)
    self.assertEqual(res, 'Jogador 1 ganhou!!! Parabéns!')
    self.assertEqual(self.gerenciador.orientacao_jogo, self.gerenciador.ESQUERDA)
    self.assertEqual(len(self.gerenciador.jogadores[0].cartas), initial_hands[0]+1)
    self.assertEqual(len(self.gerenciador.jogadores[1].cartas), 0)
    self.assertEqual(len(self.gerenciador.jogadores[2].cartas), initial_hands[2]+1)

  @patch('builtins.input', side_effect = ['1', '1', '1', '1', 'azul', '1', '1', 'amarelo', '1', 'amarelo', '1', 'fim'])
  def test_case2(self, mock_input):
    #given
    self.gerenciador.jogadores = [Jogador([Carta('vermelho', '+2'), Carta('vermelho', 'pula'), Carta('azul', 'reverso'), Carta('preto', 'escolhacor'), Carta('verde', '4')]),
                                 Jogador([Carta('azul', '1'), Carta('preto', '+4'), Carta('azul', '7')]),
                                  Jogador([Carta('vermelho', '7'), Carta('preto', 'escolhacor'), Carta('preto', '+4'), Carta('amarelo', '+2')])]
    initial_hands = [len(j.cartas) for j in self.gerenciador.jogadores]

    #when
    res = self.gerenciador.gerenciarJogo()
    
    #then
    self.assertEqual(mock_input(), 'fim')
    self.assertTrue(self.gerenciador.TERMINAROJOGO)
    self.assertEqual(res, 'Jogador 2 ganhou!!! Parabéns!')
    self.assertEqual(self.gerenciador.orientacao_jogo, self.gerenciador.ESQUERDA)
    self.assertEqual(len(self.gerenciador.jogadores[0].cartas), initial_hands[0]-4)
    self.assertEqual(len(self.gerenciador.jogadores[1].cartas), initial_hands[1]+8)
    self.assertEqual(len(self.gerenciador.jogadores[2].cartas), 0)

  @patch('builtins.input', side_effect = ['1', '1', '1', '1', 'verde', '1', 'vermelho', '1', '1', '1', '1', 'fim'])
  def test_case3(self, mock_input):
    #given
    self.gerenciador.pilha_mesa = [Carta('azul', '4')]
    self.gerenciador.jogadores = [Jogador([Carta('azul', 'reverso'), Carta('azul', '+2'), Carta('vermelho', '6')]),
                                 Jogador([Carta('preto', '+4'), Carta('vermelho', '3'), Carta('amarelo', 'reverso')]),
                                  Jogador([Carta('azul', 'pula'), Carta('preto', 'escolhacor'), Carta('amarelo', '6')])]
    initial_hands = [len(j.cartas) for j in self.gerenciador.jogadores]

    #when
    res = self.gerenciador.gerenciarJogo()
    
    #then
    self.assertEqual(mock_input(), 'fim')
    self.assertTrue(self.gerenciador.TERMINAROJOGO)
    self.assertEqual(res, 'Jogador 1 ganhou!!! Parabéns!')
    self.assertEqual(self.gerenciador.orientacao_jogo, self.gerenciador.DIREITA)
    self.assertEqual(len(self.gerenciador.jogadores[0].cartas), initial_hands[0]-3+4)
    self.assertEqual(len(self.gerenciador.jogadores[1].cartas), 0)
    self.assertEqual(len(self.gerenciador.jogadores[2].cartas), initial_hands[2]-3+2)

  @patch('builtins.input', side_effect = ['1', '1', '1', '1', '1', 'amarelo', '1', '1', 'azul', '1', 'vermelho', '1', '1', 'fim'])
  def test_case4(self, mock_input):
    #given
    self.gerenciador.pilha_mesa = [Carta('azul', '4')]
    self.gerenciador.jogadores = [Jogador([Carta('azul', '9'), Carta('azul', 'pula'), Carta('preto', '+4'), Carta('preto', '+4'), Carta('amarelo', '7')]),
                                 Jogador([Carta('azul', '+2'), Carta('preto', 'escolhacor'), Carta('vermelho', '7')]),
                                  Jogador([Carta('azul', '2'), Carta('amarelo', 'reverso')])]
    initial_hands = [len(j.cartas) for j in self.gerenciador.jogadores]

    #when
    res = self.gerenciador.gerenciarJogo()
    
    #then
    self.assertEqual(mock_input(), 'fim')
    self.assertTrue(self.gerenciador.TERMINAROJOGO)
    self.assertEqual(res, 'Jogador 0 ganhou!!! Parabéns!')
    self.assertEqual(self.gerenciador.orientacao_jogo, self.gerenciador.ESQUERDA)
    self.assertEqual(len(self.gerenciador.jogadores[0].cartas), 0)
    self.assertEqual(len(self.gerenciador.jogadores[1].cartas), initial_hands[1]-3+4)
    self.assertEqual(len(self.gerenciador.jogadores[2].cartas), initial_hands[2]-2+6)

  @patch('builtins.input', side_effect = ['1', 'amarelo', '1', '1', '1', '1', 'vermelho', '1', '1', 'azul', 'fim'])
  def test_case5(self, mock_input):
    #given
    self.gerenciador.pilha_mesa = [Carta('amarelo', '2')]
    self.gerenciador.jogadores = [Jogador([Carta('preto', '+4'), Carta('amarelo', 'reverso'), Carta('preto', 'escolhacor'), Carta('preto', '+4')]),
                                 Jogador([Carta('vermelho', '7')]),
                                  Jogador([Carta('amarelo', '4'), Carta('amarelo', '+2'), Carta('vermelho', 'pula'), Carta('vermelho', '8')])]
    initial_hands = [len(j.cartas) for j in self.gerenciador.jogadores]

    #when
    res = self.gerenciador.gerenciarJogo()
    
    #then
    self.assertEqual(mock_input(), 'fim')
    self.assertTrue(self.gerenciador.TERMINAROJOGO)
    self.assertEqual(res, 'Jogador 0 ganhou!!! Parabéns!')
    self.assertEqual(self.gerenciador.orientacao_jogo, self.gerenciador.ESQUERDA)
    self.assertEqual(len(self.gerenciador.jogadores[0].cartas), 0)
    self.assertEqual(len(self.gerenciador.jogadores[1].cartas), initial_hands[1]+6)
    self.assertEqual(len(self.gerenciador.jogadores[2].cartas), initial_hands[2]-3+4)

  @patch('builtins.input', side_effect = ['1', '1', '1', 'azul', '1', 'vermelho', '1', 'verde', '1', 'amarelo', '1', '1', '1', '1', '1', '1', '1', 'vermelho', 
                                          '1', '1', '1', '1', '1', '1', '1', 'verde', '2', '2', '1', '1', 'vermelho', '1', '1', 'fim'])
  def test_case6(self, mock_input):
    #given
    self.gerenciador.pilha_mesa = [Carta('verde', '9')]
    self.gerenciador.jogadores = [Jogador([Carta('verde', 'pula'), Carta('preto', '+4'), Carta('amarelo', '+2'), Carta('verde', '6'), Carta('vermelho', 'pula'), Carta('vermelho', 'pula')]),
                                  Jogador([Carta('preto', 'escolhacor'), Carta('amarelo', '+2'), Carta('amarelo', 'reverso'), Carta('preto', 'escolhacor'), Carta('vermelho', 'reverso'), Carta('vermelho', '1')]),
                                  Jogador([Carta('verde', 'pula'), Carta('preto', 'escolhacor'), Carta('preto', '+4'), Carta('amarelo', 'reverso'), Carta('amarelo', '6'), Carta('vermelho', 'pula'), Carta('vermelho', 'pula')])]
    initial_hands = [len(j.cartas) for j in self.gerenciador.jogadores]

    #when
    res = self.gerenciador.gerenciarJogo()
    
    #then
    self.assertEqual(mock_input(), 'fim')
    self.assertTrue(self.gerenciador.TERMINAROJOGO)
    self.assertEqual(res, 'Jogador 2 ganhou!!! Parabéns!')
    self.assertEqual(self.gerenciador.orientacao_jogo, self.gerenciador.ESQUERDA)
    self.assertEqual(len(self.gerenciador.jogadores[0].cartas), initial_hands[0]-9+4)
    self.assertEqual(len(self.gerenciador.jogadores[1].cartas), initial_hands[1]-8+10)
    self.assertEqual(len(self.gerenciador.jogadores[2].cartas), 0)

suite = unittest.TestLoader().loadTestsFromTestCase(TestUno)
unittest.TextTestRunner().run(suite)