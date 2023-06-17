import pygame

from gerenciadora import Gerenciadora

def inicia_jogo():
    pygame.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play(-1)
    som = pygame.mixer.Sound("efeito.wav")

    return Gerenciadora(),som

def encerra_jogo():
    print("Fechando o jogo!")
    pygame.quit()

def main():
    jogo, som = inicia_jogo()
    jogo.roda_loop()
    encerra_jogo()

main()
