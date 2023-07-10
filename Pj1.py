import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()



#Variaveis e funções

loop = True
loop_game = True
def aumento(x):
    for i in x:
        pygame.draw.rect(tela, (255,255,255), (i[0],i[1],cobra_tam,cobra_tam))
def reset():
    global loop, loop_game, pontos, comp_cobra, corpo_cobra, cobra_tam, maca_tam, largura, altura, paredeX, paredeY, CobraX, CobraY, macaX, macaY, ControleX, ControleY, Vel
    corpo_cobra = []

    CobraX = int(largura/2 - cobra_tam/2)
    CobraY = int(altura/2 - cobra_tam/2)

    macaX = random.randint(0,(largura - maca_tam))
    macaY = random.randint(0,(altura - maca_tam))

    ControleX = 0
    ControleY = 0

    Vel = 4
    pontos = 0
    comp_cobra = 1
    loop = True

Vel = 4
pontos = 0
comp_cobra = 1

corpo_cobra = []

ControleX = 0
ControleY = 0

largura = 700
altura = 700

cobra_tam = 25
maca_tam = 20

CobraX = int(largura/2 - cobra_tam/2)
CobraY = int(altura/2 - cobra_tam/2)

macaX = random.randint(0,(largura - maca_tam))
macaY = random.randint(0,(altura - maca_tam))

pontos = 0

paredeX = largura - cobra_tam
paredeY = altura - cobra_tam 

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('snake')
pygame.surface.Surface((largura, altura))

fundo = pygame.image.load('solo.jpg')

relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('Press Start', 55, False, False)

vfx = pygame.mixer.Sound('barulho pegar maçã.wav')

#Abrir o Jogo:
while loop_game:
    msg = f'Pontos: {pontos}'
    perdeu = 'Game Over.'
    dnv = 'R = Tentar novamente / ESC = Sair'
    txt_dnv = fonte.render(dnv, False, (255,0,0))
    txt_perdeu = fonte.render(perdeu, False, (255, 0, 0))
    txt_tela = fonte.render(msg, False, (0, 0, 0))
    relogio.tick(60)
    tela.fill((0,0,0))
    tela.blit(fundo, (0,0))
    tela.blit(txt_tela, (475, 30))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #Movimentação:
        if loop == True:
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

    
    #Cobra
    cobra = pygame.draw.rect(tela, (255,255,255), (CobraX,CobraY,cobra_tam,cobra_tam))
    #maçã
    maca = pygame.draw.rect(tela, (255,0,0),(macaX,macaY,maca_tam,maca_tam))

    #Aumento da cobra:
    cbç_cobra = []
    cbç_cobra.append(CobraX)
    cbç_cobra.append(CobraY)
    corpo_cobra.append(cbç_cobra)
    aumento(corpo_cobra)
    if len(corpo_cobra) > comp_cobra:
            del corpo_cobra[0]    

    #Colisões com paredes:   
    if CobraX >= paredeX:
        CobraX = paredeX
        tela.blit(txt_perdeu, (250, 300))
        loop = False

    if CobraX <= 0:
        CobraX = 0
        tela.blit(txt_perdeu, (250, 300))    
        loop = False

    if CobraY >= paredeY:
        CobraY = paredeY
        tela.blit(txt_perdeu, (250, 300))
        loop = False

    if CobraY <= 0:
        CobraY = 0       
        tela.blit(txt_perdeu, (250, 300))
        loop = False

    #Colisões com a cobra:
    if corpo_cobra.count(cbç_cobra) > 1:
        ControleX = 0
        ControleY = 0
        tela.blit(txt_perdeu,(250,300))
        loop = False

    #Comer maçã:
    if cobra.colliderect(maca):
        pontos += 1
        comp_cobra += pontos + 1
        macaX = random.randint(0,(largura - maca_tam))
        macaY = random.randint(0,(altura - maca_tam))
        vfx.set_volume(0.1)
        vfx.play()
 
    #Reset Jogo
    while loop == False:
        tela.blit(txt_dnv, (30, 400))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == K_r:
                    reset()
        pygame.display.flip()

    pygame.display.flip()
