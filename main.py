import pygame

from gerenciadora import Gerenciadora

def inicia_jogo():
    pygame.init()
    return Gerenciadora()

def encerra_jogo():
    print("Fechando o jogo!")
    pygame.quit()

def main():
    jogo = inicia_jogo()
    jogo.roda_loop()
    encerra_jogo()

main()
