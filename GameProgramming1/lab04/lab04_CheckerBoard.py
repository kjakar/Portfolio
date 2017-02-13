#lab04
#Alexander Jones

import pygame
import time
import random


size = 1000 #this is screen size


pygame.display.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Checkers")

firstChecker = pygame.image.load("checkers.png")#256 high 512 wide



checker = pygame.transform.scale(firstChecker, (400,200))


def drawSprite(r, c, x, y, size):
    checker = pygame.transform.scale(firstChecker, (size * 2, size))
    # enter the row and column to call the sprite
    # r = row, c = column, x and y = position.
    screen.blit(checker, (x, y), ( (0 + (size * c)), (0 + (size* r)), size, size,))
    pygame.display.flip()
    return
 
def Checkers(rand, size):
 
    z = 0
    x = 0
    yUsed = 0
    row = -1

    while z <= 289: 

        while x <= 1000:
            red = random.randint(1,3)
            if red == 1:    
                drawSprite(0, 1, x, yUsed, size)
                x += size
                z += 1
            elif red == 2:    
                drawSprite(0, 0, x, yUsed, size)
                x += size
                z += 1
            else:
                x += size
                z += 1

        while x >= 1000:
            if red == 1:
                drawSprite(0, 1, x, yUsed, size)
                pygame.display.flip() 
                x = 0
                z += 1
                row = -row
                yUsed += size
            if red == 2:
                drawSprite(0, 0, x, yUsed, size)
                pygame.display.flip()
                x = 0
                z += 1
                row = -row
                yUsed += size
            else:
                yUsed += size
                x = size
                z += 1
                row = -row

    return

def CheckerBoard(rand, size):

    y = 0
    x = 0
    yUsed = 0
    row = -1

    while y <= 289: 

        while x <= 1000:
                
            pygame.draw.rect(screen, (255,255,255), (x, yUsed, size,size), )
            pygame.display.flip()
            x += 2 * size
            y += 1

        while x >= 1000:
            if row == 1:
                yUsed += size
                pygame.draw.rect(screen, (255,255,255), (x, yUsed, size,size), )
                pygame.display.flip()
                x = 0
                y += 1
                row = -row
            else:
                yUsed += size
                pygame.draw.rect(screen, (255,255,255), (x, yUsed, size,size), )
                pygame.display.flip()
                x = size
                y += 1
                row = -row
    return

def makeItHappen():

    Random = random.randint(7,17)
    BoardSize = (1000 // Random + 1)
    screen.fill((0,0,0))
    CheckerBoard(Random, BoardSize)
    Checkers(Random,BoardSize)
    
    return

makeItHappen()
print("hello")
GameOver = False
while GameOver == False:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        makeItHappen()

    elif event.type == pygame.QUIT:
        GameOver = True
        continue
pygame.display.quit()

