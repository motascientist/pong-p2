import pygame

from cores import CORES

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Pong!")

    def renderiza(self, paletas, bola, placar):
        self.display.fill(CORES.preto)

        for paleta in paletas:
            paleta.desenha(self.display)

        bola.desenha(self.display)

        pygame.draw.line(
            self.display,        # superfície
            CORES.branco,        # cor
            [200, 20],           # coord_a
            [200, 280],          # coord_b
            1                    # espessura
        )

        placar.desenha(self.display)
        pygame.display.update()
