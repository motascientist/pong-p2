import pygame

from cores import CORES

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Pong")

    def renderiza(self, paletas, bola, placar, gerenciadora): # receber a gerenciadora como argumento
        self.display.fill(CORES.preto)
        for paleta in paletas:
            paleta.desenha(self.display)
        bola.desenha(self.display)
        placar.desenha(self.display)
        if gerenciadora.fim_de_jogo: # verificar se a variável fim_de_jogo da gerenciadora é True
            self.desenha_fim_de_jogo() # desenhar a mensagem de fim de jogo na tela
        pygame.display.update()

    def desenha_fim_de_jogo(self):
        # definir fonte e cor
        fonte = pygame.font.SysFont(None, 50)
        cor = CORES.branco

        # renderizar o texto
        texto = fonte.render("FIM DE JOGO", True, cor)

        # obter o retângulo que contém o texto
        texto_rect = texto.get_rect()

        # centralizar o retângulo na tela
        texto_rect.center = (200, 150)

        # desenhar o texto na tela
        self.display.blit(texto, texto_rect)