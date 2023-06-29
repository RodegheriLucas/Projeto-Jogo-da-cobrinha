import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

MovX = largura/2
MovY = altura/2


tela = pygame.display.set_mode((largura, altura))

while True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                MovY -= 20
            if event.key == K_a:
                MovX -= 20
            if event.key == K_s:
                MovY += 20
            if event.key == K_d:
                MovX += 20

    cobra = pygame.draw.rect(tela, (10,244,10), (MovX,MovY,40,40))
    if MovX >= 600:
        MovX = 600
    if MovX < 0:
        MovX = 0
    if MovY >= 440 :
        MovY = 440
    if MovY < 0:
        MovY = 0
    pygame.display.update()

