import pygame
from pygame.locals import*
pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Kemi Fældningsreaktioner")

ag = pygame.image.load("AgNO3.png").convert()


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (0, 0, 20, 40))

    window.blit(ag, (0,0))


pygame.quit()
