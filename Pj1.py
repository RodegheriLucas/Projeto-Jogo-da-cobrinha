import pygame
import random
from pygame.locals import *
from sys import exit
pygame.init()


#Variaveis
cobra_tam = 25

largura = 700
altura = 700

paredeX = largura - cobra_tam
paredeY = altura - cobra_tam

CobraX = int(largura/2 - cobra_tam/2)
CobraY = int(altura/2 - cobra_tam/2)

ControleX = 0
ControleY = 0

Vel = 10

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('fundo')
fundo = pygame.image.load((r'C:\Users\lucas\.vscode\Projetos Python\Projeto-Jogo-da-cobrinha\solo.png'))

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
    cobra = pygame.draw.rect(tela, (200,100,0), (CobraX,CobraY,cobra_tam,cobra_tam))

    pygame.display.update()