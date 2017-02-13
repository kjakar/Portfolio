__author__ = 'Alex Jones'

import pygame
import random
import math

blast = pygame.image.load("thruster_gradient.png")
boom = pygame.image.load("explosion_gradient.png")
class emitter(object):

    def __init__(self, x, y, angle):
        self.mAngle = angle # in degrees
        self.mX = x
        self.mY = y
        self.mParticleList = []
        self.mExplosionsList = []

    def updateAngle(self, newAngle):
        self.mAngle = newAngle

    def createExplosion(self, x, y):
        for i in range(200):
            X = x
            Y = y
            number = random.randint(-180,180)
            angle = math.radians(self.mAngle + number)
            size = random.randint(3,11)

            boom = [X,Y,angle,255,size]
            self.mExplosionsList.append(boom)

    def renderExplosion(self, dt, surface):
        for p in self.mExplosionsList:
            # adjust color
            color = boom.get_at((int(p[3]), 0))
            p[3] -= 300 * dt

            # make the particle move
            p[0] += 500 * math.cos(p[2]) * dt # particles X cord
            p[1] += 500 * math.sin(p[2]) * dt # particles Y cord

            # draw the particle
            pygame.draw.circle(surface, color, (int(p[0]),int(p[1])), p[4])
            if p[3] <= 1:
                self.mExplosionsList.remove(p)


    def create(self):
        x = self.mX
        y = self.mY
        number = random.randint(-20,20)
        angle = math.radians(self.mAngle + number)
        size = random.randint(3,7)

        particle = [x,y,angle,255,size]
        self.mParticleList.append(particle)

    def render(self, dt, surface):
        for p in self.mParticleList:
            # adjust color
            color = blast.get_at((int(p[3]), 0))
            p[3] -= 300 * dt

            # make the particle move
            p[0] += 500 * math.cos(p[2]) * dt # particles X cord
            p[1] += 500 * math.sin(p[2]) * dt # particles Y cord

            # draw the particle
            pygame.draw.circle(surface, color, (int(p[0]),int(p[1])), p[4])
            if p[3] <= 1:
                self.mParticleList.remove(p)