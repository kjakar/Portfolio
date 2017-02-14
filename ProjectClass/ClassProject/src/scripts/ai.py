__author__ = 'Alex'

#Robert Begley

import pygame

playerSprite = pygame.image.load("..\\assets\\images\\Shark.png") # this is 63X35 pixels and is size 1
# add 27 pixels to the width for every health up to 5
# add 15 pixels to the height for every health up to 5
#playerSprite = pygame.transform.scale(playerSprite,(200,111)) # this is the biggest size : size 5

class AI(object):
    def __init__(self, pos, speed):
        #super(Actor,self).__init__(wall = 30, att = 10, damage = 10)
        self.x, self.y = pos
        self.frame = 0
        self.timer = 0
        self.health = 1
        self.distance = 0 # this is in percent so that we can scale the level length
        self.speed = speed # this is how fast the player moves through world space
        self.rect = [0,0,0,0]


    def update(self,dt):
        self.x += 300 * dt


    def render(self, surf, dt):
        global playerSprite

        # this deals with the number of frames per second we use for the player sprite
        self.timer += dt
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

        # this handles the players rect for hit detection
        # we will handle all hit detection outside of the player class by passing other classes the players rect
        self.rect[0] = self.x
        self.rect[1] = self.y
        self.rect[2] = self.x + 65 + (self.health * 27)
        self.rect[3] = self.y + 35 + (self.health * 15)


    def hitDetect(self,other): # this checks all 4 corners of the player object
        # the rect of the player and AI work the same way, in range format (i.e. 220-306, not 220+86)
        if other.rect[0] >= self.rect[0] and other.rect[0] <= self.rect[2]: # top left check
            if other.rect[1] >= self.rect[1] and other.rect[1] <= self.rect[3] + self.rect[1]:
                return True
        elif other.rect[2] >= self.rect[0] and other.rect[2] <= self.rect[2]: # top right check
            if other.rect[1] >= self.rect[1] and other.rect[1] <= self.rect[3]:
                return True
        elif other.rect[0] >= self.rect[0] and other.rect[0] <= self.rect[2]: # bottom left check
            if other.rect[3] >= self.rect[1] and other.rect[3] <= self.rect[3]:
                return True
        elif other.rect[2] >= self.rect[0] and other.rect[2] <= self.rect[2]: # bottom right check
            if other.rect[3] >= self.rect[1] and other.rect[3] <= self.rect[3]:
                return True
        else:
            return False






