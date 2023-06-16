import pygame

from paleta import Paleta
from bola import Bola
from tela import Tela
from placar import Placar

class Gerenciadora:
    def __init__(self):
        self.tela = Tela()
        self.placar = Placar()
        self.fim_de_jogo = False # criar uma variável booleana chamada fim_de_jogo e inicializá-la como False
        self.inicia_partida()

    def inicia_partida(self):
        # time.sleep(0.5)
        self.paletas = [
            Paleta([10, 100], (pygame.K_w, pygame.K_s)),
            Paleta([380, 100], (pygame.K_UP, pygame.K_DOWN))
        ]
        self.bola = Bola()

    def roda_loop(self):
        while True:
            if self.clique_saida():
                break
            self.trata_teclas_pressionadas()
            self.bola.movimenta()
            if self.placar.atualiza(self.paletas, self.bola, self): # passar a gerenciadora como argumento para a função atualiza do placar
                self.inicia_partida()
            
            self.tela.renderiza(self.paletas, self.bola, self.placar, self) # passar a gerenciadora como argumento para a função renderiza da tela
            pygame.time.Clock().tick(60)

    def trata_teclas_pressionadas(self):
        """
        Obtém as teclas pressionadas no loop,
        e aciona o movimento das paletas se necessário.
        """
        teclas = pygame.key.get_pressed()
        for paleta in self.paletas:
            paleta.movimenta(teclas)
  
    def clique_saida(self):
        """Retornar True se usuário clicou para sair do jogo."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            if evento.type == pygame.MOUSEBUTTONDOWN: # verificar se o evento é do tipo pygame.MOUSEBUTTONDOWN
                if self.fim_de_jogo: # verificar se a variável fim_de_jogo é True
                    self.reinicia_jogo() # chamar a função reinicia_jogo

        return False

    def reinicia_jogo(self): # criar uma função que reinicia o jogo
        self.placar.zera_pontuacao() # chamar a função zera_pontuacao do placar
        self.fim_de_jogo = False # atribuir False à variável fim_de_jogo
        self.inicia_partida() # chamar a função inicia_partida
