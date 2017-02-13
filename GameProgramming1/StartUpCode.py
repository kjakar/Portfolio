__author__ = 'Alex Jones'


import pygame
import time
import random

#set-up================================================================
pygame.mixer.init()
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Album Title Goes Here")
font = pygame.font.SysFont("Times New Roman", 24)

#Global-Vars===========================================================

gameOver = False
mpos = pygame.mouse.get_pos()
#Functions=============================================================


#Game-vars=============================================================


#Game-Code=============================================================

while gameOver == False:

    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        print(mpos)

    elif event.type == pygame.QUIT:
        gameOver = True
        continue

    mpos = pygame.mouse.get_pos()

    pygame.draw.circle(screen, (255,255,255), (100,100), 20)

    pygame.display.flip()

#Quit==================================================================

pygame.display.quit()
pygame.mixer.quit()