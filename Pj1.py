import pygame
import random
from pygame.locals import *
from sys import exit
pygame.init()


#Variaveis
cobra_tam = 25
maca_tam = 15

largura = 700
altura = 700

paredeX = largura - cobra_tam
paredeY = altura - cobra_tam

CobraX = int(largura/2 - cobra_tam/2)
CobraY = int(altura/2 - cobra_tam/2)

macaX = random.randint(0,(largura - maca_tam))
macaY = random.randint(0,(altura - maca_tam))

ControleX = 0
ControleY = 0

Vel = 4

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('snake')
fundo = pygame.image.load('solo.png')

relogio = pygame.time.Clock()

#Abrir o Jogo:
while True:
    
    relogio.tick(60)
    tela.fill((0,0,0))
    tela.blit(fundo, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #Movimentação:
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if ControleY == Vel:
                    pass
                else:
                    ControleX = 0
                    ControleY = -Vel
            if event.key == K_DOWN:
                if ControleY == -Vel:
                    pass
                else:
                    ControleX = 0
                    ControleY = Vel
            if event.key == K_RIGHT:
                if ControleX == -Vel:
                    pass
                else:
                    ControleX = Vel
                    ControleY = 0
            if event.key == K_LEFT:
                if ControleX == Vel:
                    pass
                else:
                    ControleX = -Vel
                    ControleY = 0

    #Movimentação infinita:
    CobraX += ControleX
    CobraY += ControleY

    #Colisões com paredes:   
    if CobraX >= paredeX:
        CobraX = paredeX
    
    if CobraX <= 0:
        CobraX = 0
    
    if CobraY >= paredeY:
        CobraY = paredeY
    
    if CobraY <= 0:
        CobraY = 0       

    #Cobra   
    cobra = pygame.draw.rect(tela, (0,0,255), (CobraX,CobraY,cobra_tam,cobra_tam))

    #maçã
    maca = pygame.draw.rect(tela, (255,0,0),(macaX,macaY,maca_tam,maca_tam))
    pygame.display.update()