__author__ = 'Alex Jones'


import pygame
import time
import random
import math3d
import math

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
angle = 90
num = math.radians(angle)

rotVect = math3d.VectorN(math.cos(num), - math.sin(num), 0)

tankPos = math3d.VectorN(100,100,0)
linkPos = math3d.VectorN(60,130,0)

v = linkPos - tankPos


n = 1
g = 1
#Game-Code=============================================================

while gameOver == False:
# Updates ========================================================================================
    dt = clock.tick() / 1000
    mpos = pygame.mouse.get_pos()

# this controls tank rotation

    angle += 10 * dt
    num = math.radians(angle)

    rotVect = math3d.VectorN(math.cos(num), - math.sin(num), 0)

# this give all the lines (red green and blue at the moment)
    v = linkPos - tankPos
    added = (tankPos + getPara(v, rotVect) + getPerp(v, rotVect))
    added2 = tankPos + getPara(v, rotVect)
    added3 = tankPos + getPerp(v, rotVect)
    added4 = tankPos + rotVect.normalized() * 200 #this is get point only change 200 to dist

    linkPos = math3d.VectorN(mpos[0], mpos[1], 0)

    #perpVector = math3d.VectorN(-v2[1], v2[0], 0).normalized()
    #sidePt = v1 + (300 * perpVector)
    #pygame.draw.circle(screen, (255,0,0), (int(sidePt[0]), int(sidePt[1])), 10)

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
    #pygame.draw.line(screen, (255,0,0), (int(v1[0]), int(v1[1])),(int(sidePt[0]), int(sidePt[1])), 10)
    pygame.draw.line(screen, (255,0,0), (int(tankPos[0]), int(tankPos[1])),(int(added[0]), int(added[1])), 3)
    pygame.draw.line(screen, (0,255,0), (int(tankPos[0]), int(tankPos[1])),(int(added2[0]), int(added2[1])), 3) #draw from link to this one
    pygame.draw.line(screen, (0,0,255), (int(tankPos[0]), int(tankPos[1])),(int(added3[0]), int(added3[1])), 3)
    pygame.draw.line(screen, (155,0,155), (int(linkPos[0]), int(linkPos[1])),(int(added2[0]), int(added2[1])), 3) #this is the hit detection (if dis of these points is less than hit circle
    pygame.draw.line(screen, (0,155,155), (int(linkPos[0]), int(linkPos[1])),(int(added3[0]), int(added3[1])), 3)
    pygame.draw.line(screen, (0,0,0), (int(tankPos[0]), int(tankPos[1])),(int(added4[0]), int(added4[1])), 3) #This is the rotation direction




    pygame.display.flip()

#Quit==================================================================

pygame.display.quit()
pygame.mixer.quit()