__author__ = 'Alex Jones'

__author__ = 'Alex Jones'


import pygame
import time
import random
import math3d
import math
import Ray
import Tank

#set-up================================================================
pygame.mixer.init()
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((711,400))
pygame.display.set_caption("Album Title Goes Here")
font = pygame.font.SysFont("Times New Roman", 24)
clock = pygame.time.Clock()

#Global-Vars===========================================================

gameOver = False
mpos = pygame.mouse.get_pos()
#Functions=============================================================
def dis(x1, y1, x2, y2):
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis

def disVect(vector1, vector2):
    x1 = vector1[0]
    x2 = vector2[0]
    y1 = vector1[1]
    y2 = vector2[1]
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis

def getPara(vector1, vector2):
    """
    :param vector1: This is the vector you are projecting on.
    :param vector2: this is the secondary vector.
    :return: a new vector parallel to vector 1 but the length it would need to be to make a right triangle with vector2
    """
    if isinstance(vector1, math3d.VectorN) and isinstance(vector2, math3d.VectorN):
        #if vector2.__mDim == 3 and vector1.__mDim == vector2.__mDim:
        v = vector1
        w = vector2

        newVector = (v.dotProduct(w) / w.dotProduct(w)) * w
        return newVector
    else:
        return ValueError("getPara can only use two vectors of the same dimensions.")

def getPerp(vector1, vector2):
    """
    :param vector1: This is the vector you are projecting on.
    :param vector2: this is the secondary vector.
    :return: a new vector perpendicular  to vector 1 but the length it would need to be to make a right triangle with vector2
    """
    if isinstance(vector1, math3d.VectorN) and isinstance(vector2, math3d.VectorN):
        vPara = getPara(vector1, vector2)
        v = vector1
        newVector = v - vPara

        return newVector
    else:
        return ValueError("getPerp can only use two vectors of the same dimensions.")


#Game-vars=============================================================

tankPos = math3d.VectorN(100,100,0)
linkPos = math3d.VectorN(60,130,0)
tank = Tank.Tank(tankPos)

#Game-Code=============================================================

while gameOver == False:

# Updates ========================================================================================
    dt = clock.tick() / 1000
    mpos = pygame.mouse.get_pos()

    linkPos = math3d.VectorN(mpos[0], mpos[1], 0) # this makes the mopos a vector

    tank.rotate(linkPos, 10, dt)

    added4 = tankPos + tank.angleVector.normalized() * 200 #this is get point only change 200 to dist


# user Input =====================================================================================
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        print(mpos)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameOver = True
    elif event.type == pygame.QUIT:
        gameOver = True
        continue


# Drawing Code ===================================================================================
    screen.fill((255,255,255))

    pygame.draw.circle(screen, (155,0,155), (mpos[0], mpos[1]), 20)
    pygame.draw.circle(screen, (155,0,0), (int(tankPos[0]), int(tankPos[1])), 20)

    pygame.draw.line(screen, (0,0,0), (int(tankPos[0]), int(tankPos[1])),(int(added4[0]), int(added4[1])), 3) #This is the rotation direction


    pygame.display.flip()

#Quit==================================================================

pygame.display.quit()
pygame.mixer.quit()