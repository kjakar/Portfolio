__author__ = 'Alex Jones'

import math
import pygame

class bullet(object):

    def __init__(self):
        self.bulletsList = []

    def create(self, x ,y ,rotation):
        bullet = [x, y, rotation]
        self.bulletsList.append(bullet)

    def update(self, deltaTime, surf):


        # moves the bullets
        for bullet in self.bulletsList:
            rad = math.radians(bullet[2])
            bullet[0] += 1000 * math.cos(rad) * deltaTime
            bullet[1] -= 1000 * math.sin(rad) * deltaTime

        # renders the bullet
            if len(self.bulletsList) >= 1:
                pygame.draw.circle(surf, (255,0,0), (int(bullet[0]),int(bullet[1])), 15)
            if (bullet[0] > 1400 or bullet[0] < 0) or (bullet[1] < 0 or bullet[1] > 800):
                self.bulletsList.remove(bullet)


    def thingsToHit(self, objectController = None):

        if objectController != None:
            for b in self.bulletsList:
                if objectController.checkForHit(b[0] + 7, b[1] + 7) == True:
                    self.bulletsList.remove(b)

