import pygame
import time
import random





pygame.display.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("You Wouldn't Lime Me When i'm Angry")




mpos = pygame.mouse.get_pos()


def dis(x1, y1, x2, y2):
    dis = (((x1 -y1)** 2) + ((y1 - y2))) ** 0.5
    return dis



def Draw(color, posX, posY):
    posX = random.randint(65, 935)
    posY = random.randint(65, 935)
    radius = random.randint(25, 60)
    pygame.draw.circle(screen, color, (posX, posY), radius)
    pygame.display.flip()

def Draw2(color, posX, posY):
    posX = random.randint(65, 935)
    posY = random.randint(65, 935)
    radius = random.randint(25, 60)
    pygame.draw.circle(screen, color, (posX, posY), radius)
    pygame.display.flip()


GameOver = False
while GameOver == False:
    X = random.randint(65, 935)
    Y = random.randint(65, 935)
    X2 = random.randint(65, 935)
    Y2 = random.randint(65, 935)
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        Draw((255,0,0), X, Y)
        Draw2((255,0,0), X2,Y2)
    elif dis(mpos[0],mpos[1], X, Y) <= 20:
        print("you did it")

    elif event.type == pygame.QUIT:
        GameOver = True
        continue
pygame.display.quit()
