import math
import random
import pygame

from cores import CORES

class Bola:
    velocidade = 5
    posicao = [200, 150]
    speed_factor = 1.1

    def __init__(self):
        self.direcao = self.cria_vetor_unitario()
    
    def desenha(self, display):
        pygame.draw.circle(
            display,                    # tela
            CORES.branco,               # cor
            self.posicao,               # pos
            5                           # raio
        )

    def cria_vetor_unitario(self):
        while True:
            dir_x = random.uniform(-1, 1)
            dir_y = math.sqrt(1 - dir_x ** 2)
            if int(dir_x * self.velocidade) and int(dir_y * self.velocidade):
                break

        return [dir_x, random.choice([-1, 1]) * dir_y]
        
    def movimenta(self):
        self.posicao = [
            int(self.posicao[0] + self.velocidade * self.direcao[0]),
            int(self.posicao[1] + self.velocidade * self.direcao[1])
        ]

        self.processa_colisoes()

    def processa_colisoes(self):
        if self.posicao[1] <= 5:
            self.direcao[1] *= -1
            self.posicao[1] = 5
            # self.velocidade *= self.speed_factor → Aumenta Superior

        if self.posicao[1] >= 295:
            self.direcao[1] *= -1         
            self.posicao[1] = 295          
            # self.velocidade *= self.speed_factor → Aumenta inferior

        if self.posicao[0] <= 25:
            self.direcao[0] *= -1
            self.posicao[0] = 25
            self.velocidade *= self.speed_factor # Aumenta Vm na paleta esquerda

        if self.posicao[0] >= 375:
            self.direcao[0] *= -1
            self.posicao[0] = 375
            self.velocidade *= self.speed_factor # Aumenta Vm na paleta direita