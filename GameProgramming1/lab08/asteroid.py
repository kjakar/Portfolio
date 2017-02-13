__author__ = 'Alex Jones'


import pygame
import math
import random
import emitter

large = pygame.image.load("LargeCoin.png") #1500 wide 150 tall
med = pygame.image.load("MedCoin.png") # 100 wide 100 tall
small = pygame.image.load("smallCoin.png") #500 wide 50 tall

E = emitter.emitter(0,0,0)

def dis(x1, y1, x2, y2):
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis

class asteroid(object):

    def __init__(self, timer):
        self.mInitTimer = timer
        self.timer = 0
        self.astroidsList = []
        print("inited")


    def create(self, x , y, state, direction):
            asteroid = [x,y,state, -direction, 0, 0.0]
            self.astroidsList.append(asteroid)

    def render(self, deltaTime, surface):
        self.timer += deltaTime
        for a in self.astroidsList:
            a[5] += deltaTime
            rad = math.radians(a[3])

            if a[2] == 3 and a[5] >= 0.13:
                a[4] += 1
                a[5] = 0
                if a[4] > 9: a[4] = 0

            if a[2] == 3:
                a[0] += 100 * math.cos(rad) * deltaTime
                a[1] += 100 * math.sin(rad) * deltaTime
                column = 150 * a[4]
                surface.blit(large, (a[0],a[1]), (column, 0, 150, 150))

            if a[2] == 2 and a[5] >= 0.1:
                a[4] += 1
                a[5] = 0
                if a[4] > 9: a[4] = 0

            if a[2] == 2:
                a[0] += 150 * math.cos(rad) * deltaTime
                a[1] += 150 * math.sin(rad) * deltaTime
                column = 100 * a[4]
                surface.blit(med, (a[0],a[1]), (column, 0, 100, 100))

            if a[2] == 1 and a[5] >= 0.07:
                a[4] += 1
                a [5] = 0
                if a[4] > 9: a[4] = 0

            if a[2] == 1:
                a[0] += 200 * math.cos(rad) * deltaTime
                a[1] += 200 * math.sin(rad) * deltaTime
                column = 50 * a[4]
                surface.blit(small, (a[0],a[1]), (column, 0, 50, 50))

            if (a[0] > 1700 or a[0] < -400) or (a[1] < -400 or a[1] > 1200):
                self.astroidsList.remove(a)

    def checkForHit(self, objectsX, objectsY):

        hit = True
        normal = False
        for a in self.astroidsList:
            if a[2] == 3:
                if dis(objectsX, objectsY, a[0] + 75, a[1] + 75) < 55:
                    E.createExplosion(objectsX, objectsY)
                    self.astroidsList.remove(a)
                    random1 = random.randint(0,360)
                    random2 = random.randint(0,360)
                    self.create(a[0],a[1], 2, random1)
                    self.create(a[0],a[1], 2, random2)
                    return hit
            if a[2] == 2:
                if dis(objectsX, objectsY, a[0] + 50, a[1] + 50) < 33:
                    E.createExplosion(objectsX, objectsY)
                    self.astroidsList.remove(a)
                    random1 = random.randint(0,360)
                    random2 = random.randint(0,360)
                    self.create(a[0],a[1], 1, random1)
                    self.create(a[0],a[1], 1, random2)
                    return hit
            if a[2] == 1:
                if dis(objectsX, objectsY, a[0] + 25, a[1] + 25) < 25:
                    E.createExplosion(objectsX, objectsY)
                    self.astroidsList.remove(a)
                    return hit

        return normal


