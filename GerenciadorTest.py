import unittest
from unittest.mock import patch
from Baralho import Carta
from Jogador import Jogador
from Gerenciador import Gerenciador

"""
TR: 
(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 1, 7), (1, 2, 1), (1, 3, 1), (1, 4, 1), (1, 5, 1), (1, 6, 1), (1, 7, 1), (1, 2, 8), (1, 3, 8), (1, 4, 8), (1, 5, 8), (1, 6 ,8), (1, 7, 8), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 1, 5), (2, 1, 6), (2, 1, 7), (3, 1, 3), (3, 1, 2), (3, 1, 4), (3, 1, 5), (3, 1, 6), (3, 1, 7), (4, 1, 4), (4, 1, 2), (4, 1, 3), (4, 1, 5), (4, 1, 6), (4, 1, 7), (5, 1, 5), (5, 1, 2), (5, 1, 3), (5, 1, 4), (5, 1, 6), (5, 1, 7), (6, 1, 6), (6, 1, 2), (6, 1, 3), (6, 1, 4), (6, 1, 5), (6, 1, 7), (7, 1, 7), (7, 1, 2), (7, 1, 3), (7, 1, 4), (7, 1, 5), (7, 1, 6)
"""


class TestUno(unittest.TestCase):
    def setUp(self):
        self.pilha_compra = [
            Carta('vermelho', '7'),
            Carta('azul', '2'), 
            Carta('verde', '8'),
            Carta('amarelo', '9'), 
            Carta('vermelho', '2'), 
            Carta('verde', '5'), 
            Carta('azul', '+2'), 
            Carta('preto', 'escolhacor')
        ]

    def test_CT01(self):
        """
        CT01 = {0,1,4,1,5,8}: satisfaz [4,1,5];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('vermelho', '+2'), Carta('azul', '1')]
        cartas_jogador1 = [Carta('azul', '8'), Carta('amarelo', '+2')]
        cartas_jogador2 = [Carta('preto', '+4'), Carta('verde', '2')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('vermelho', '7')]
        gerenciador.pilha_compra = self.pilha_compra
        
        #ação Jogador 0
        # Dizer para o prox jogador que ele precisa comprar
        prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', '+2'))
        gerenciador.jogadores[0].jogar(Carta('vermelho', '+2'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        
        #ação jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)
        
        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 2)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', '+4'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('vermelho', '+2'))
    
    @patch('builtins.input', side_effect=['azul'])
    def test_CT02(self, mock_inputs):
        """
        CT02 = {0,1,4,1,2,1,4,8}: satisfaz [2,1,4], [4,1,2];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []

        cartas_jogador0 = [Carta('vermelho', '+2'), Carta('azul', '+2')]
        cartas_jogador1 = [Carta('preto', 'escolhacor'), Carta('amarelo', '4')] # escolhe azul
        cartas_jogador2 = [Carta('preto', 'escolhacor'), Carta('azul', '1')]
        
        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)
        
        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('vermelho', '7')]
        gerenciador.pilha_compra = self.pilha_compra
        
        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', '+2'))
        gerenciador.jogadores[0].jogar(Carta('vermelho', '+2'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        
        #ação jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        prox_jogador = gerenciador.acaoJogada(2, Carta('preto', 'escolhacor'))
        gerenciador.jogadores[2].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)
        
        #ação do jogador 0
        gerenciador.jogadores[0].jogar(Carta('azul', '+2'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 2)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('azul', '+2'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', 'escolhacor'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('vermelho', '+2'))
        self.assertTrue(gerenciador.verificarVencedor(gerenciador.jogadores[0]))
        self.assertFalse(gerenciador.verificarVencedor(gerenciador.jogadores[1]))
        self.assertFalse(gerenciador.verificarVencedor(gerenciador.jogadores[2]))

    @patch('builtins.input', side_effect=['azul'])
    def test_CT03(self, mock_inputs):
        """
        CT03 = {0,1,3,1,2,8}: satisfaz [3,1,2];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('vermelho', 'pula'), Carta('azul', '9'), Carta('azul', '5')]
        cartas_jogador1 = [Carta('preto', '+4'), Carta('amarelo', '2'), Carta('verde', '3')]
        cartas_jogador2 = [Carta('preto', 'escolhacor'), Carta('verde', '1'), Carta('amarelo', '5')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('vermelho', '7')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', 'pula'))
        gerenciador.jogadores[0].jogar(Carta('vermelho', 'pula'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        #ação jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        prox_jogador = gerenciador.acaoJogada(2, Carta('preto', 'escolhacor'))
        gerenciador.jogadores[2].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)
        
        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', 'escolhacor'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('vermelho', 'pula'))

    def test_CT04(self):
        """
        CT04 = {0,1,3,1,3,8}: satisfaz [0,1,3], [1,3,8], [3,1,3];
        jogador1 - inicia, aguarda, skip
        jogador2 - aguarda, skip, termina
        jogador3 - skip, aguarda, skip
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('vermelho', '6'), Carta('azul', '1'), Carta('azul','0'), Carta('preto', 'pula')]
        cartas_jogador1 = [Carta('azul', '2'), Carta('verde', '5'), Carta('verde', '3'), Carta('amarelo','')]
        cartas_jogador2 = [Carta('vermelho', '4'), Carta('amarelo', '2'), Carta('preto', 'pula')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('amarelo', '3')]
        gerenciador.pilha_compra = self.pilha_compra

        prox_jogador = gerenciador.acaoJogada(0, Carta('preto', 'pular'))
        gerenciador.jogadores[0].jogar(Carta('preto', 'pula'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        prox_jogador = gerenciador.acaoJogada(2, Carta('preto', 'pular'))
        gerenciador.jogadores[2].jogar(Carta('preto', 'pula'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)
        
        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)

    @patch('builtins.input', side_effect=['azul'])
    def test_CT05(self, mock_inputs):
        """
        CT05 = {0,1,5,1,3,1,5,8}: satisfaz [3,1,5], [5,1,3];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto', '+4'), Carta('verde', '7'), Carta('amarelo', '+2')]
        cartas_jogador1 = [Carta('preto', '+4'), Carta('azul', '9'), Carta('vermelho', '4')]
        cartas_jogador2 = [Carta('azul', 'pula'), Carta('amarelo', '1'), Carta('verde', '3')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('azul', '3')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('preto', '+4'))
        gerenciador.jogadores[0].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        #ação jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        prox_jogador = gerenciador.acaoJogada(2, Carta('azul', 'pula'))
        gerenciador.jogadores[2].jogar(Carta('azul', 'pula'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        #ação jogador 1
        gerenciador.jogadores[1].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 3)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', '+4'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('azul', 'pula'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('preto', '+4'))
    
    @patch('builtins.input', side_effect=['verde'])
    def test_CT06(self, mock_inputs):
        """
        CT06 = {0,1,7,1,5,1,7,8}: satisfaz [1,5,1], [5,1,7], [7,1,5];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('vermelho', '7'), Carta('azul', '9'), Carta('verde', '3')]
        cartas_jogador1 = [Carta('preto', '+4'), Carta('amarelo', '+2'), Carta('azul', '2')]
        cartas_jogador2 = [Carta('azul', 'pula'), Carta('amarelo', '1'), Carta('verde', '3')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('azul', '7')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', '7'))
        gerenciador.jogadores[0].jogar(Carta('vermelho', '7'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('preto', '+4'))
        gerenciador.jogadores[1].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        #ação jogador 0
        gerenciador.jogadores[0].jogar(Carta('verde', '3'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 + 4)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('verde', '3'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', '+4'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('vermelho', '7'))
        
    def test_CT07(self):
        """
        CT07 = {0,1,4,1,4,8}: satisfaz [0,1,4], [1,4,8], [4,1,4];
        jogador0 = joga +2
        jogador1 = compra duas carta, não joga nenhuma
        jogador2 = joga +2
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto', '+4'), Carta('verde', '7'), Carta('amarelo', '+2')]
        cartas_jogador1 = [Carta('verde', '4'), Carta('vermelho', '1'), Carta('vermelho', '0')]
        cartas_jogador2 = [Carta('azul', '+2'), Carta('amarelo', '5'), Carta('verde', '3')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('amarelo', '5')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação Joagdor 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('amarelo', '+2'))
        gerenciador.jogadores[0].jogar(Carta('amarelo', '+2'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        
        #ação Jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação Jogador 2
        gerenciador.jogadores[2].jogar(Carta('azul', '+2'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador0 + 2)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('azul', '+2'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('amarelo', '+2'))
    
    @patch('builtins.input', side_effect=['verde'])
    def test_CT08(self, mock_inputs):
        """
        CT08 = {0,1,6,1,2,1,6,8}: satisfaz [2,1,6], [6,1,2];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('amarelo', 'reverso'), Carta('preto', 'escolhacor'), Carta('verde', '7')]
        cartas_jogador1 = [Carta('amarelo', 'reverso'), Carta('azul', '7'), Carta('vermelho', '9')]
        cartas_jogador2 = [Carta('preto', 'escolhacor'), Carta('vermelho', '6'), Carta('azul', '8')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('amarelo', '1')]
        gerenciador.pilha_compra = self.pilha_compra
        
        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('amarelo', 'reverso'))
        gerenciador.jogadores[0].jogar(Carta('amarelo', 'reverso'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        #ação jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        prox_jogador = gerenciador.acaoJogada(2, Carta('preto', 'escolhacor'))
        gerenciador.jogadores[2].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        #ação jogador 1
        gerenciador.jogadores[1].jogar(Carta('amarelo', 'reverso'), gerenciador.pilha_mesa)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        
        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('amarelo', 'reverso'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', 'escolhacor'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('amarelo', 'reverso'))

    @patch('builtins.input', side_effect=['vermelho', 'azul'])
    def test_CT09(self, mock_inputs):
        """
        CT09 = {0,1,2,1,2,8}: satisfaz [0,1,2], [1,2,8], [2,1,2];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto', 'escolhacor'), Carta('verde', '1'), Carta('azul', '5')]
        cartas_jogador1 = [Carta('preto', 'escolhacor'), Carta('azul', '7'), Carta('vermelho', '9')]
        cartas_jogador2 = [Carta('amarelo', '+2'), Carta('vermelho', '6'), Carta('azul', '8')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('amarelo', '+2')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('preto', 'escolhecor'))
        gerenciador.jogadores[0].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('preto', 'escolhecor'))
        gerenciador.jogadores[1].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', 'escolhacor'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', 'escolhacor'))
    
    @patch('builtins.input', side_effect=['azul', 'amarelo', 'azul'])
    def test_CT010(self, mock_inputs):
        """
        CT10 = {0,1,5,1,2,1,5,8}: satisfaz [2,1,5], [5,1,2];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto', '+4'), Carta('preto', '+4'), Carta('azul', '1')]
        cartas_jogador1 = [Carta('preto', 'escolhacor'), Carta('azul', '7'), Carta('vermelho', '9')]
        cartas_jogador2 = [Carta('preto', 'escolhacor'), Carta('amarelo', '8'), Carta('vermelho', '1')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('verde', 'reverso')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('preto', '+4'))
        gerenciador.jogadores[0].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        #ação jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2
        prox_jogador = gerenciador.acaoJogada(2, Carta('preto', 'escolhacor'))
        gerenciador.jogadores[2].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)      
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        #ação jogador 0
        gerenciador.jogadores[0].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        
        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 4)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2  -1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', '+4'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', 'escolhacor'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('preto', '+4'))

    def test_CT11(self):
        """
        CT11 = {0,1,7,1,6,1,6,1,7,8}: satisfaz [0,1,7], [1,6,1], [1,7,1], [1,7,8], [6,1,6], [6,1,7], [7,1,6];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('vermelho','7'),Carta('amarelo',  'reverso'),Carta('verde', '8')]
        cartas_jogador1 = [Carta('vermelho','reverso'),Carta('amarelo','8'),Carta('verde','2')]
        cartas_jogador2 = [Carta('azul','3'),Carta('amarelo','reverso'),Carta('vermelho','0')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('vermelho','2')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', '7'))
        gerenciador.jogadores[0].jogar(Carta('vermelho', '7'), gerenciador.pilha_mesa)

        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('vermelho', 'reverso'))
        gerenciador.jogadores[1].jogar(Carta('vermelho', 'reverso'), gerenciador.pilha_mesa)

         #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('amarelo', 'reverso'))
        gerenciador.jogadores[0].jogar(Carta('amarelo', 'reverso'), gerenciador.pilha_mesa)

        #ação jogador 1
        gerenciador.jogadores[1].jogar(Carta('amarelo', '8'), gerenciador.pilha_mesa)
        
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)
        
        
        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 2)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('amarelo', '8'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('amarelo', 'reverso'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('vermelho', 'reverso'))

    def test_CT12(self):
        """
        CT12 = {0,1,7,1,7,1,7,8}: satisfaz [7,1,7];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('azul','3'),Carta('azul',  'reverso'),Carta('preto', 'escolhacor')]
        cartas_jogador1 = [Carta('amarelo','3'),Carta('amarelo','pula'),Carta('verde','2')]
        cartas_jogador2 = [Carta('amarelo','0'),Carta('verde','2'),Carta('preto','+4')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('azul','8')]
        gerenciador.pilha_compra = self.pilha_compra
        
         #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('azul', '3'))
        gerenciador.jogadores[0].jogar(Carta('azul', '3'), gerenciador.pilha_mesa)

        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('amarelo', '3'))
        gerenciador.jogadores[1].jogar(Carta('amarelo', '3'), gerenciador.pilha_mesa)

         #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('amarelo', '0'), gerenciador.pilha_mesa)
        
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('amarelo', '0'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('amarelo', '3'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('azul', '3'))

    def test_CT13(self):
        """
        CT13 = {0,1,7,1,3,1,7,8}: satisfaz [1,3,1], [3,1,7], [7,1,3];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('verde','3'),Carta('verde','2'),Carta('preto', 'escolhacor')]
        cartas_jogador1 = [Carta('verde','pula'),Carta('amarelo','pula'),Carta('verde','0')]
        cartas_jogador2 = [Carta('amarelo','4'),Carta('vermelho','9'),Carta('preto','+4')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('verde','pula')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('verde', '3'))
        gerenciador.jogadores[0].jogar(Carta('verde', '3'), gerenciador.pilha_mesa)

        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('verde', 'pula'))
        gerenciador.jogadores[1].jogar(Carta('verde', 'pula'), gerenciador.pilha_mesa)

         #ação jogador 0
        gerenciador.jogadores[0].jogar(Carta('verde', '2'), gerenciador.pilha_mesa)
        
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('verde', '2'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('verde', 'pula'))
        self.assertEqual(gerenciador.pilha_mesa[2], Carta('verde', '3'))

    @patch('builtins.input', side_effect=['verde'])
    def test_CT14(self, mock_inputs):
        """
        CT14 = {0,1,5,1,6,8}: satisfaz [5,1,6];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto','+4'),Carta('verde','2'),Carta('preto', 'escolhacor')]
        cartas_jogador1 = [Carta('verde','reverso'),Carta('vermelho','reverso'),Carta('verde','3')]
        cartas_jogador2 = [Carta('verde','reverso'),Carta('azul','1'),Carta('preto','+4')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('azul','3')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('preto', '+4'))
        gerenciador.jogadores[0].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)

        #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('verde', 'reverso'), gerenciador.pilha_mesa)

        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 4)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('verde', 'reverso'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', '+4'))
        
    def test_CT15(self):
        """
        CT15 = {0,1,3,1,4,8}: satisfaz [3,1,4];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('azul','pula'),Carta('verde','2'),Carta('vermelho', '2')]
        cartas_jogador1 = [Carta('verde','reverso'),Carta('vermelho','reverso'),Carta('verde','3')]
        cartas_jogador2 = [Carta('azul','+2'),Carta('verde',''),Carta('preto','+4')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('azul','0')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('azul', 'pula'))
        gerenciador.jogadores[0].jogar(Carta('azul', 'pula'), gerenciador.pilha_mesa)

        #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('azul', '+2'), gerenciador.pilha_mesa)

        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('azul', '+2'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('azul', 'pula'))

    def test_CT16(self):
        """
        CT16 = {0,1,6,1,3,1,6,8}: satisfaz [3,1,6], [6,1,3];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('verde','reverso'),Carta('azul','reverso'),Carta('vermelho', '2')]
        cartas_jogador1 = [Carta('verde','reverso'),Carta('vermelho','reverso'),Carta('vermelho','0')]
        cartas_jogador2 = [Carta('verde','pula'),Carta('verde','2'),Carta('preto','+4')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('verde','2')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('verde','reverso'))
        gerenciador.jogadores[0].jogar(Carta('verde','reverso'), gerenciador.pilha_mesa)

        #ação jogador 2
        prox_jogador = gerenciador.acaoJogada(2, Carta('verde','pula'))
        gerenciador.jogadores[2].jogar(Carta('verde', 'pula'), gerenciador.pilha_mesa)

        #ação jogador 0
        gerenciador.jogadores[0].jogar(Carta('azul','reverso'), gerenciador.pilha_mesa)



        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('azul', 'reverso'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('verde', 'pula'))

    def test_CT17(self):
        """
        CT17 = {0,1,4,1,3,8}: satisfaz [4,1,3];
        jogador1: joga +2
        jogador2: 
        jogador3: 
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('amarelo', '5'), Carta('vermelho', '+2')]
        cartas_jogador1 = [Carta('azul', '7'), Carta('vermelho', '2')]
        cartas_jogador2 = [Carta('vermelho', 'pula'), Carta('verde', '+2'), Carta('amarelo','1'), Carta('azul','9')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('preto', '+4')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', '+2'))
        gerenciador.jogadores[0].jogar(Carta('vermelho','+2'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        
        #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('vermelho','pula'), gerenciador.pilha_mesa)    
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 2)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('vermelho', 'pula'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('vermelho', '+2'))

        
    def test_CT18(self):
        """
        CT18 = {0,1,6,1,5,8}: satisfaz [6,1,5];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('azul','reverso'),Carta('amarelo','0'),Carta('preto', '+4')]
        cartas_jogador1 = [Carta('verde','2'),Carta('vermelho','1'),Carta('verde','pula')]
        cartas_jogador2 = [Carta('preto','+4'),Carta('azul','7'),Carta('preto','+4')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('vermelho','reverso')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('azul','reverso'))
        gerenciador.jogadores[0].jogar(Carta('azul','reverso'), gerenciador.pilha_mesa)

        #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)

        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', '+4'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('azul', 'reverso'))

    def test_CT19(self):
        """
        CT19 = {0,1,6,1,4,1,6,8}: satisfaz [0,1,6], [1,6,8], [4,1,6], [6,1,4];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('azul','reverso'),Carta('azul','reverso'),Carta('preto', '+4')]
        cartas_jogador1 = [Carta('verde','2'),Carta('vermelho','6'),Carta('azul','pula')]
        cartas_jogador2 = [Carta('azul','+2'),Carta('verde','2'),Carta('amarelo','1')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('amarelo','reverso')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('azul','reverso'))
        gerenciador.jogadores[0].jogar(Carta('azul','reverso'), gerenciador.pilha_mesa)

        #ação jogador 2
        prox_jogador = gerenciador.acaoJogada(2, Carta('azul','+2'))
        gerenciador.jogadores[2].jogar(Carta('azul', '+2'), gerenciador.pilha_mesa)

         #ação jogador 0
        gerenciador.jogadores[0].jogar(Carta('azul','reverso'), gerenciador.pilha_mesa)

        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 2)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('azul', 'reverso'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('azul', '+2'))
        
    @patch('builtins.input', side_effect=['azul'])
    def test_CT20(self, mock_inputs):
        """
        CT20 = {0,1,5,1,4,8}: satisfaz [5,1,4];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto','+4'),Carta('verde','reverso'),Carta('preto', '+4')]
        cartas_jogador1 = [Carta('amarelo','1'),Carta('vermelho','6'),Carta('azul','reverso')]
        cartas_jogador2 = [Carta('azul','+2'),Carta('verde','0'),Carta('vermelho','pula')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('verde','reverso')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('preto','+4'))
        gerenciador.jogadores[0].jogar(Carta('preto','+4'), gerenciador.pilha_mesa)

        #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('azul', '+2'), gerenciador.pilha_mesa)

        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 4)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('azul', '+2'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', '+4'))

    @patch('builtins.input', side_effect=['amarelo'])
    def test_CT21(self, mock_inputs):
        """
        CT21 = {0,1,2,1,3,8}: satisfaz [2,1,3];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto', 'escolhacor'), Carta('verde','reverso'),Carta('preto', '+4')]
        cartas_jogador1 = [Carta('amarelo', 'pula'), Carta('amarelo','1'),Carta('vermelho','6')]
        cartas_jogador2 = [Carta('azul','+2'),Carta('verde','0'),Carta('vermelho','pula')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        
        gerenciador.pilha_mesa = [Carta('verde', '1')]
        gerenciador.pilha_compra = self.pilha_compra
        gerenciador.n_de_jogadores = 3

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('preto', 'escolhacor'))
        gerenciador.jogadores[0].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        
        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('amarelo', 'pula'))
        gerenciador.jogadores[1].jogar(Carta('amarelo', 'pula'), gerenciador.pilha_mesa)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2     
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 -1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('amarelo', 'pula'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', 'escolhacor'))
        self.assertEqual(prox_jogador, 0)

    def test_CT22(self):
        """
        CT22 = {0,1,7,1,4,1,7,8}: satisfaz [1,4,1], [4,1,7], [7,1,4]
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('azul','0'),Carta('azul','7'),Carta('preto', '+4')]
        cartas_jogador1 = [Carta('azul','+2'),Carta('vermelho','1'),Carta('verde','reverso')]
        cartas_jogador2 = [Carta('azul','+2'),Carta('amarelo','6'),Carta('azul','pula')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('verde','0')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('azul','0'))
        gerenciador.jogadores[0].jogar(Carta('azul','0'), gerenciador.pilha_mesa)

        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('azul','+2'))
        gerenciador.jogadores[1].jogar(Carta('azul', '+2'), gerenciador.pilha_mesa)

        #ação jogador 0
        gerenciador.jogadores[0].jogar(Carta('azul','7'), gerenciador.pilha_mesa)

      
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 2)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 + 2)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('azul', '7'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('azul', '+2'))

    @patch('builtins.input', side_effect=['vermelho'])
    def test_CT23(self, mock_inputs):
        """
        CT23 = {0,1,7,1,2,1,7,8}: satisfaz [1,2,1], [2,1,7], [7,1,2]
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('verde','2'),Carta('azul','7'),Carta('preto', '+4')]
        cartas_jogador1 = [Carta('preto','escolhacor'),Carta('vermelho','1'),Carta('verde','reverso')]
        cartas_jogador2 = [Carta('vermelho','0'),Carta('amarelo','6'),Carta('azul','pula')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)


        gerenciador.pilha_mesa = [Carta('azul','2')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('verde','2'))
        gerenciador.jogadores[0].jogar(Carta('verde','2'), gerenciador.pilha_mesa)

        #ação jogador 1
        prox_jogador = gerenciador.acaoJogada(1, Carta('preto','escolhacor'))
        gerenciador.jogadores[1].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)

        #ação jogador 2
        gerenciador.jogadores[2].jogar(Carta('vermelho','0'), gerenciador.pilha_mesa)

      
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)
        
        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 - 1)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('vermelho', '0'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', 'escolhacor'))

    @patch('builtins.input', side_effect=['vermelho'])
    def test_CT24(self, mock_inputs):    
        """
        CT24 = {0,1,5,1,5,8}: satisfaz [0,1,5], [1,5,8], [5,1,5];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('preto', '+4'), Carta('amarelo', 'pula'), Carta('verde', '9')]
        cartas_jogador1 = [Carta('preto','escolhacor'),Carta('vermelho','1'),Carta('verde','reverso')]
        cartas_jogador2 = [Carta('preto', '+4'), Carta('vermelho', '9'), Carta('vermelho', '8')]

        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        jogador2 = Jogador(cartas_jogador2)

        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)
        gerenciador.jogadores.append(jogador2)

        tamanho_mao_antigo_jogador0 = len(cartas_jogador0)
        tamanho_mao_antigo_jogador1 = len(cartas_jogador1)
        tamanho_mao_antigo_jogador2 = len(cartas_jogador2)

        gerenciador.pilha_mesa = [Carta('vermelho', '7')]
        gerenciador.pilha_compra = self.pilha_compra

        #ação jogador 0
        prox_jogador = gerenciador.acaoJogada(0, Carta('preto', '+4'))
        gerenciador.jogadores[0].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador0 = len(gerenciador.jogadores[0].cartas)

        #ação jogador 1
        tamanho_mao_jogador1 = len(gerenciador.jogadores[1].cartas)

        #ação jogador 2     
        gerenciador.jogadores[2].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        tamanho_mao_jogador2 = len(gerenciador.jogadores[2].cartas)

        self.assertEqual(tamanho_mao_jogador0, tamanho_mao_antigo_jogador0 - 1)
        self.assertEqual(tamanho_mao_jogador1, tamanho_mao_antigo_jogador1 + 4)
        self.assertEqual(tamanho_mao_jogador2, tamanho_mao_antigo_jogador2 - 1)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', '+4'))
        self.assertEqual(gerenciador.pilha_mesa[1], Carta('preto', '+4'))
  
if __name__ == '__main__':
    unittest.main()
