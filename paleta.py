import pygame

from cores import CORES

class Paleta:
    velocidade = 5

    def __init__(self, posicao, acoes):
        self.posicao = posicao
        self.botao_subir = acoes[0]
        self.botao_descer = acoes[1]

    def desenha(self, display):
        pygame.draw.rect(
            display,                    # tela
            CORES.branco,               # cor
            self.posicao + [10, 100]    # pos + tam
        )

    def movimenta(self, teclas):
        if teclas[self.botao_subir] and self.posicao[1] > 0:
            self.posicao[1] -= self.velocidade

        if teclas[self.botao_descer] and self.posicao[1] < 200:
            self.posicao[1] += self.velocidade
