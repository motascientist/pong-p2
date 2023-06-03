import pygame

from cores import CORES

class Placar:
    def __init__(self):
        self.p1 = 0
        self.p2 = 0

    def atualiza(self, paletas, bola):
        if self.chama_var(paletas[0], bola, 25): # paleta da esquerda
            self.p2 += 1
            return True

        if self.chama_var(paletas[1], bola, 375): # paleta da direita
            self.p1 += 1
            return True

        return False

    def chama_var(self, paleta, bola, limite):
        if bola.posicao[0] == limite:
            if paleta.posicao[1] <= bola.posicao[1] <= paleta.posicao[1] + 100:
                return False

            return True

        return False

    def desenha(self, display):
        # definir fonte
        fonte = pygame.font.SysFont(None, 30)

        # renderizar o texto
        p1_texto = fonte.render(str(self.p1), True, CORES.vermelho)
        p2_texto = fonte.render(str(self.p2), True, CORES.vermelho)

        # desenhar na tela
        display.blit(p1_texto, (30, 30))
        display.blit(p2_texto, (350, 30))
