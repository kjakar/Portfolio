__author__ = 'Alex'

import pygame

playerSprite = pygame.image.load("..\\assets\\images\\Shark.png")

class Bot(object):

    def __init__(self, pos, speed, health, rank, name):
        #super(Actor,self).__init__(wall = 30, att = 10, damage = 10)
        self.x, self.y = pos
        self.frame = 0
        self.timer = 0
        self.health = health
        self.distance = 0 # this is in percent so that we can scale the level length
        self.speed = speed # I don't think this does anything, but im not going to remove it because It'll break something
        self.worldSpeed = 0 # this is how fast the player moves through world space
        self.rect = [0,0,0,0]
        self.invincible = 0.0
        self.inFront = 0
        self.rank = rank # this should be first second or third numerically of course
        self.name = name

    def update(self, dt, RealPlayer):
        self.x += RealPlayer.worldSpeed * dt
        self.x -= self.worldSpeed * dt


    def render(self, surf, dt):
        global playerSprite
        if self.health > 0:
            # this deals with the number of frames per second we use for the player sprite
            self.timer += dt
            self.invincible -= dt
            if self.timer >= 0.1:
                self.timer = 0
                self.frame += 1
                if self.frame > 5:
                    self.frame = 0

            # this does the image scaling.
            sprite = pygame.transform.scale(playerSprite, (65 + (self.health * 27),35 + (self.health * 15)))

            # this code does the blitting
            sprite.set_colorkey((188,71,154))
            surf.blit(sprite, (self.x, self.y))

            # this is the colored triangle for the fakePlayer

            colorList = [(125,0,125),(255,0,0),(255,255,20),(0,0,0)]


            point1 = [self.x, self.y]
            point2 = [20 + self.x, self.y]
            point3 = [10 + self.x, self.y + 20]
            triangle = [tuple(point1),tuple(point2),tuple(point3)]
            pygame.draw.polygon(surf, colorList[self.rank - 1], triangle)



            # this handles the players rect for hit detection
            # we will handle all hit detection outside of the player class by passing other classes the players rect
            # hit detection for obstacles is done by the obstacles class, and hit detection for AI is done in the AI class
            self.rect[0] = self.x
            self.rect[1] = self.y
            self.rect[2] = self.x + 65 + (self.health * 27)
            self.rect[3] = self.y + 35 + (self.health * 15)

            # this deals with health and world speed

            if self.health > 5: self.health = 5

            self.worldSpeed = 415 - 35 * self.health # the test speed before the changes in how we move through world space was 200 but this can be changed
