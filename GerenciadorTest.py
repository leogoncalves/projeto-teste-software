import unittest
from Baralho import Carta
from Jogador import Jogador
from Gerenciador import Gerenciador
"""
TR: 
(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 1, 7), (1, 2, 1), (1, 3, 1), (1, 4, 1), (1, 5, 1), (1, 6, 1), (1, 7, 1), (1, 2, 8), (1, 3, 8), (1, 4, 8), (1, 5, 8), (1, 6 ,8), (1, 7, 8), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 1, 5), (2, 1, 6), (2, 1, 7), (3, 1, 3), (3, 1, 2), (3, 1, 4), (3, 1, 5), (3, 1, 6), (3, 1, 7), (4, 1, 4), (4, 1, 2), (4, 1, 3), (4, 1, 5), (4, 1, 6), (4, 1, 7), (5, 1, 5), (5, 1, 2), (5, 1, 3), (5, 1, 4), (5, 1, 6), (5, 1, 7), (6, 1, 6), (6, 1, 2), (6, 1, 3), (6, 1, 4), (6, 1, 5), (6, 1, 7), (7, 1, 7), (7, 1, 2), (7, 1, 3), (7, 1, 4), (7, 1, 5), (7, 1, 6)
"""

class TestUno(unittest.TestCase):

    def test_CT01(self):
        #CT1
        """
        CT01 = {0,1,4,1,5,8}: satisfaz [4,1,5];
        """
        gerenciador = Gerenciador()
        gerenciador.jogadores = []
        
        cartas_jogador0 = [Carta('vermelho', '+2'), Carta('azul', '1')]
        cartas_jogador1 = [Carta('preto', '+4'), Carta('amarelo', '4')]
        jogador0 = Jogador(cartas_jogador0)
        jogador1 = Jogador(cartas_jogador1)
        gerenciador.jogadores.append(jogador0)
        gerenciador.jogadores.append(jogador1)

        tam_antigo = len(cartas_jogador1)
        gerenciador.pilha_mesa = [Carta('vermelho', '7')]
        #topo_descarte = descarte[-1]
        gerenciador.pilha_compra = [Carta('vermelho', '7'), Carta('vermelho', '7'), Carta('vermelho', '7')]
        
        #ação Jogador 0
        # Dizer para o prox jogador que ele precisa comprar
        prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', '+2'))
        gerenciador.jogadores[0].jogar(Carta('vermelho', '+2'), gerenciador.pilha_mesa)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('vermelho', '+2'))

        #essa linha não deu certo para os teste, prox_jogador retorna 0
        #tamanho_mao = len(gerenciador.jogadores[prox_jogador].cartas)
        
        #ação jogador 1
        tamanho_mao = len(gerenciador.jogadores[1].cartas)
        self.assertEqual(tamanho_mao, tam_antigo+2)
        gerenciador.jogadores[1].jogar(Carta('preto', '+4'), gerenciador.pilha_mesa)
        self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', '+4'))
    

    def test_CT02(self):
      print('TESTE 2')
      #CT02
      """
      CT02 = {0,1,4,1,2,1,4,8}: satisfaz [2,1,4], [4,1,2];
      """
      gerenciador = Gerenciador()
      gerenciador.jogadores = []

      cartas_jogador0 = [Carta('vermelho', '+2'), Carta('azul', '1')]
      cartas_jogador1 = [Carta('preto', 'escolhacor'), Carta('amarelo', '4')] # verde
      cartas_jogador2 = [Carta('verde', '+2'), Carta('azul', '1')]
      jogador0 = Jogador(cartas_jogador0)
      jogador1 = Jogador(cartas_jogador1)
      tam_antigo = len(cartas_jogador1)
      jogador2 = Jogador(cartas_jogador2)
      gerenciador.jogadores.append(jogador0)
      gerenciador.jogadores.append(jogador1)
      gerenciador.jogadores.append(jogador2)

      gerenciador.pilha_mesa = [Carta('vermelho', '7')]
      gerenciador.pilha_compra = [Carta('vermelho', '7'), Carta('vermelho', '7'), Carta('vermelho', '7'), Carta('vermelho', '7'), Carta('vermelho', '7')]
      
      #ação jogador 0
      prox_jogador = gerenciador.acaoJogada(0, Carta('vermelho', '+2'))
      gerenciador.jogadores[0].jogar(Carta('vermelho', '+2'), gerenciador.pilha_mesa)
      self.assertEqual(gerenciador.pilha_mesa[0], Carta('vermelho', '+2'))

      #ação jogador 1
      tamanho_mao = len(gerenciador.jogadores[1].cartas)
      self.assertEqual(tamanho_mao, tam_antigo+2)
      prox_jogador = gerenciador.acaoJogada(1, Carta('preto', 'escolhacor'))
      print("Troca: ",cartas_jogador1[0].cor)
      gerenciador.jogadores[1].jogar(Carta('preto', 'escolhacor'), gerenciador.pilha_mesa)
      #deveria ter passado?
      self.assertEqual(gerenciador.pilha_mesa[0], Carta('preto', 'escolhacor'))

      #ação jogador 2
      gerenciador.jogadores[2].jogar(Carta('verde', '+2'), gerenciador.pilha_mesa)
      self.assertEqual(gerenciador.pilha_mesa[0], Carta('verde', '+2'))
        

if __name__ == '__main__':
    unittest.main()

"""
-> Devemos chamar a função selecionar, ao invés de colocar o jogar na mão?
-> A questão do wild ter passado, estamos errando algo do lado dos testes?
-> Deveriamos testar se depois que o Jogador 1 escolheu verde, a carta do Jogador 2 deveria ser verde? 
"""