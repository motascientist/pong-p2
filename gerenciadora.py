import time
import pygame

from paleta import Paleta
from bola import Bola
from tela import Tela
from placar import Placar

class Gerenciadora:
    def __init__(self):
        self.tela = Tela()
        self.placar = Placar()
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
            if self.placar.atualiza(self.paletas, self.bola):
                self.inicia_partida()
            
            self.tela.renderiza(self.paletas, self.bola, self.placar)
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

        return False