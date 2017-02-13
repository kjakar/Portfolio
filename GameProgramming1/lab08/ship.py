__author__ = 'Alex Jones'
import pygame
import math
import emitter



def rot_center(rot_image, angle):
    """rotate a Surface, maintaining position."""

    loc = rot_image.get_rect().center
    rot_sprite = pygame.transform.rotate(rot_image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite


class ship(object):
    """This is a ship dummy, can't you read"""

    def __init__(self, x, y):
        self.mX = x
        self.mY = y
        self.angle = 0
        self.initship = pygame.image.load("$100 dollar Bill.png")
        self.rotShip = self.initship
        self.speed = 0

    def speedUp(self, true, dt):
        yes = true
        if yes == True:
            self.speed += 300 * dt
            if self.speed >= 300:
                self.speed = 300
        else:
            self.speed -= 150 * dt
            if self.speed <= 0:
                self.speed = 0

    def move(self, deltaTime, emitter = None):
        rad = math.radians(self.angle)
        self.mX += self.speed * math.cos(rad) * deltaTime # ships X cord
        self.mY += self.speed * math.sin(rad) * deltaTime # ships Y cord

        a = self.rotShip.get_width() / 2
        b = self.rotShip.get_height() / 2
        if emitter != None:
            emitter.updateAngle(self.angle - 180)
            emitter.mX = a + self.mX
            emitter.mY = b + self.mY

    def turn(self, deltaTime, direction, emitter = None):
        """" direction: -1 = left 1 = right"""
        if direction == 1:
            self.angle -= 200 * deltaTime
        if direction == -1:
            self.angle += 200 * deltaTime
        if self.angle >= 360:
            self.angle = 0
        self.rotShip = pygame.transform.rotate(self.initship, (-self.angle))

        a = self.rotShip.get_width() / 2
        b = self.rotShip.get_height() / 2
        if emitter != None:
            emitter.updateAngle(self.angle - 180)
            emitter.mX = a + self.mX
            emitter.mY = b + self.mY


    def render(self, surf):

        surf.blit(self.rotShip, (self.mX, self.mY))

    def fire(self, bulletController):
        a = self.rotShip.get_width() / 2
        b = self.rotShip.get_height() / 2
        bX = a + self.mX
        bY = b + self.mY
        bulletController.create(bX,bY, -self.angle)
