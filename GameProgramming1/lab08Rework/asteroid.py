__author__ = 'Alex Jones'

import math
import pygame

small = pygame.image.load("images//smallCoin.png")
med = pygame.image.load("images//MedCoin.png")
large = pygame.image.load("images//LargeCoin.png")

class Asteroid(object):

    def __init__(self, x, y, angle, speed, asteroidImage, explosionImage, color, state = 0):
        self.mX = x
        self.mY = y
        self.mAngle = int(math.degrees(angle))
        self.mSpeed = speed
        self.image = asteroidImage
        self.explosionImage = explosionImage
        self.color = color
        self.mDead = False
        self.state = state
        self.size = state
        self.timer = 0

    def update(self, deltaTime, areaOfMovement):
        rad = math.radians(self.mAngle)
        self.mX += self.mSpeed * math.cos(rad) * deltaTime
        self.mY += self.mSpeed * math.sin(rad) * deltaTime

        maxX = areaOfMovement[2]
        minX = areaOfMovement[0]
        maxY = areaOfMovement[3]
        minY = areaOfMovement[1]

        if self.mX > maxX:
            self.mX = minX + 1
        if self.mX < minX:
            self.mX = maxX - 1
        if self.mY > maxY:
            self.mY = minY + 1
        if self.mY < minY:
            self.mY = maxY - 1

        self.timer += deltaTime
        if self.timer >= 0.1:
            self.timer = 0
            self.state += 1
            if self.state > 9:
                self.state = 0


    def render(self, surface):

        if self.size == 3:
            surface.blit(large, (self.mX, self.mY), (self.state*150,0,150,150))
        if self.size == 2:
            surface.blit(med, (self.mX, self.mY), (self.state*100,0,100,100))
        if self.size == 1:
            surface.blit(small, (self.mX, self.mY), (self.state*50,0,50,50))
