import unittest
from unittest.mock import patch
from Jogador import Jogador
from Baralho import Carta

class JogadorTest(unittest.TestCase):

    def test_selecionar_ct1(self):
        topo_descarte = Carta('vermelho', '7')
        jogador = Jogador(cartas = [
            Carta('verde', '2'), 
            Carta('azul', '9'), 
            Carta('vermelho', '5'),
            Carta('azul', '1')
        ])

        selecionadas = jogador.selecionar(topo_descarte)
    
        self.assertEqual(
            selecionadas, 
            [Carta('vermelho', '5')]
        )
        
    def test_selecionar_ct2(self):
        topo_descarte = Carta('amarelo', '2')
        jogador = Jogador(cartas = [
            Carta('verde', '2'), 
            Carta('azul', '0'), 
            Carta('vermelho', '1'),
            Carta('azul', '6')
        ])
        selecionadas = jogador.selecionar(topo_descarte)

        self.assertEqual(
            selecionadas, 
            [Carta('verde', '2')]
        )
    
    def test_selecionar_ct3(self):
        topo_descarte = Carta('amarelo', '3')
        jogador = Jogador(cartas = [Carta('verde', '5'), 
            Carta('azul', '1'), 
            Carta('verde', '4'),
            Carta('preto', 'escolhacor')
        ])
        selecionadas = jogador.selecionar(topo_descarte)

        self.assertEqual(
            selecionadas, 
            [Carta('preto', 'escolhacor')]
        )
        
    def test_selecionar_ct4(self):
        topo_descarte = Carta('vermelho', '9')
        jogador = Jogador(cartas = [])
        selecionadas = jogador.selecionar(topo_descarte)

        self.assertEqual(selecionadas, [])

##################################################################

    def test_comprar_ct1(self):
        jogador = Jogador(cartas = [])
        monte_de_compra = []
        mao_jogador = jogador.cartas
        
        monte_de_compra = jogador.comprar(0, monte_de_compra)
        
        # Resultado esperado
        monte_de_compra_posterior = []

        mao_jogador_posterior = []
      
        self.assertEqual(mao_jogador, mao_jogador_posterior)
        self.assertEqual(monte_de_compra_posterior, monte_de_compra)

    def test_comprar_ct2(self):
        jogador = Jogador(cartas = [Carta('amarelo', '7'), Carta('verde', 'inverter'), Carta('azul','3')])
        mao_jogador = jogador.cartas
        
        monte_de_compra = [Carta('vermelho', '9'), Carta('amarelo', 'inverter')]

        monte_de_compra = jogador.comprar(0, monte_de_compra)
        
        # Resultado esperado
        monte_de_compra_posterior = [
            Carta('vermelho', '9'), 
            Carta('amarelo', 'inverter')
        ]

        mao_jogador_posterior = [
            Carta('amarelo', '7'), 
            Carta('verde', 'inverter'), 
            Carta('azul','3')
        ]

        self.assertEqual(monte_de_compra, monte_de_compra_posterior)
        self.assertEqual(mao_jogador, mao_jogador_posterior)

    def test_comprar_ct3(self):
        jogador = Jogador(cartas = [])
        monte_compras = []
        with self.assertRaises(IndexError):
            jogador.comprar(1, monte_compras)        

    def test_comprar_ct4(self):
        monte_compras = [
            Carta('amarelo', '+2'), 
            Carta('verde', '3'), 
            Carta('vermelho', '4')
        ]
        
        jogador = Jogador(cartas = [
            Carta('azul', '+2'), 
            Carta('verde', '0'), 
            Carta('verde', 'pula')
        ])

        mao_jogador = jogador.cartas
        monte_compras = jogador.comprar(1, monte_compras)
        
        # Resultado esperado
        mao_jogador_posterior = [
            Carta('azul', '+2'), 
            Carta('verde', '0'), 
            Carta('verde', 'pula'),
            Carta('amarelo', '+2')
        ]

        monte_compras_posterior = [
            Carta('verde', '3'),
            Carta('vermelho', '4')
        ]
        
        self.assertEqual(mao_jogador, mao_jogador_posterior)
        self.assertEqual(monte_compras, monte_compras_posterior)

    def test_comprar_ct5(self):
        monte_compras = []
        jogador = Jogador(cartas = [
            Carta('amarelo', '7'), 
            Carta('vermelho', '1')
        ])
        mao_jogador = jogador.cartas
        monte_compras = jogador.comprar(0, monte_compras)

        # Resultado esperado
        mao_jogador_posterior = [
            Carta('amarelo', '7'), 
            Carta('vermelho', '1')
        ]
        
        monte_compras_posterior =[]

        self.assertEqual(monte_compras_posterior, monte_compras)
        self.assertEqual(mao_jogador, mao_jogador_posterior)

    def test_comprar_ct6(self):
        monte_compras = [
            Carta('azul', '+2'),
            Carta('verde', '3'),
            Carta('amarelo', '8'),
            Carta('vermelho','4')
        ]

        jogador = Jogador(cartas = [])
        mao_jogador = jogador.cartas
        monte_compras = jogador.comprar(3, monte_compras) 

        # Resultado esperado
        monte_compras_posterior = [
            Carta('vermelho','4')
        ]
        
        mao_jogador_posterior = [
            Carta('azul', '+2'),
            Carta('verde', '3'),
            Carta('amarelo', '8')
        ]
        
        self.assertEqual(monte_compras, monte_compras_posterior)
        self.assertEqual(mao_jogador, mao_jogador_posterior)

##################################################################

    def test_jogar_ct1(self):
        jogador = Jogador(cartas=[])
        monte_descarte = []
        carta_jogada = Carta('preto', 'escolhacor')
        
        with self.assertRaises(ValueError):
            monte_descarte = jogador.jogar(
                carta_jogada,
                monte_descarte
            )

    def test_jogar_ct2(self):
        jogador = Jogador(cartas=[])

        monte_descarte = [
            Carta('amarelo', '+2'),
            Carta('preto', 'escolhacor')
        ]
        
        carta_jogada = Carta('preto', '4')
        with self.assertRaises(ValueError):
            jogador.jogar(carta_jogada, monte_descarte)
          
    def test_jogar_ct3(self):
        jogador = Jogador(
            cartas=[
                Carta('azul', '4'),
                Carta('verde', 'inverter')
            ]
        )
        mao_jogador = jogador.cartas

        monte_descarte = []
        carta_jogada = Carta('azul', '4')
        
        monte_descarte = jogador.jogar(
            carta_jogada,
            monte_descarte
        )

        # Resultado esperado
        monte_descarte_posterior = [
            Carta('azul', '4')
        ]
        mao_jogador_posterior = [
            Carta('verde', 'inverter')
        ]
        self.assertEqual(monte_descarte, monte_descarte_posterior)
        self.assertEqual(mao_jogador, mao_jogador_posterior)        
        
    def test_jogar_ct4(self):
        jogador = Jogador(
            cartas=[
                Carta('azul', '9'),
                Carta('verde', '5')
            ]
        )

        mao_jogador = jogador.cartas

        monte_descarte = [
            Carta('vermelho', '5'),
            Carta('verde', '+2')

        ]
        carta_jogada = Carta('verde', '5')
        
        monte_descarte = jogador.jogar(
            carta_jogada,
            monte_descarte
        )

        # Resultado esperado
        monte_descarte_posterior = [
            Carta('verde', '5'),
            Carta('vermelho', '5'),
            Carta('verde', '+2')
        ]
        mao_jogador_posterior = [
            Carta('azul', '9')
        ]
    
        self.assertEqual(monte_descarte, monte_descarte_posterior)
        self.assertEqual(mao_jogador, mao_jogador_posterior)
    
##################################################################

    @patch('builtins.input', side_effect=['amarelo'])
    def test_escolher_cor_de_coringa_ct1(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'amarelo')

    @patch('builtins.input', side_effect=['321', '45', 'verde'])
    def test_escolher_cor_de_coringa_ct2(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'verde')
    
    @patch('builtins.input', side_effect=['amarelo'])
    def test_escolher_cor_de_coringa_ct3(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'amarelo')
    
    @patch('builtins.input', side_effect=['roxo', 'ghghghghg', 'azul'])
    def test_escolher_cor_de_coringa_ct4(self, mock_inputs):
        jogador = Jogador(cartas=[])
        cor_escolhida = jogador.escolher_cor_de_coringa()
        self.assertEqual(cor_escolhida, 'azul')

##################################################################

if __name__ == '__main__':
    unittest.main()