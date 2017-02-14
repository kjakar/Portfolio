#Robert Begley

import pygame

playerSprite = pygame.image.load("..\\assets\\images\\Leg Shark.png") # this is 63X35 pixels and is size 1
deadScreen = pygame.image.load("..\\assets\\images\\YouLose.jpg")
# add 27 pixels to the width for every health up to 5
# add 15 pixels to the height for every health up to 5
#playerSprite = pygame.transform.scale(playerSprite,(200,111)) # this is the biggest size : size 5

class Player(object):
    def __init__(self, pos, speed):
        #super(Actor,self).__init__(wall = 30, att = 10, damage = 10)
        self.x, self.y = pos
        self.frame = 0
        self.timer = 0
        self.health = 3
        self.distance = 0 # this is in percent so that we can scale the level length
        self.speed = speed # I don't think this does anything, but im not going to remove it because It'll break something
        self.worldSpeed = 0 # this is how fast the player moves through world space
        self.rect = [0,0,0,0]
        self.invincible = 0.0
        self.name = "You!"
        self.isBoost = False
        self.hardMode = 0

    def changeSprite(self, name):
        global playerSprite
        playerSprite = name

    def update(self,dt,move = 0):
        if move == "up":
            if self.y > 70: # these if's lock the player in the screen bounds, the math isn't quite done though
                self.moveUp(dt)

        if move == "down":  # the bottom pink strip is 48 pixels high
            if self.y < 600:
                self.moveDown(dt)

        if move == "left":
            if self.x > 0:
                self.moveLeft(dt)

        if move == "right":
            if self.x < 1180:
                self.moveRight(dt)

    def moveLeft(self, dt):
        self.x -= 300 * dt

    def moveRight(self, dt):
        self.x += 300 * dt

    def moveUp(self, dt):
        self.y -= 300 * dt

    def moveDown(self, dt):
        self.y += 300 * dt

    def boost(self, dt, boost, move = 0):
        self.isBoost = True
        if move == "boost":
            self.worldSpeed = boost + (415 - 35 * self.health)
            if self.x <= 0:
                self.x = 0
            elif self.x >= 1280:
                self.x = 1280

    def render(self, surf, dt):
        global playerSprite
        global deadScreen
        # this deals with the number of frames per second we use for the player sprite
        self.timer += dt
        self.invincible -= dt
        if self.timer >= 0.1:
            self.timer = 0
            self.frame += 1
            if self.frame > 5:
                self.frame = 0

        # this does the image scaling.
        sprite = pygame.transform.scale(playerSprite, (65,35 ))
        if self.health >= 0:
            sprite = pygame.transform.scale(playerSprite, (65 + (self.health * 27),35 + (self.health * 15)))
        surf.set_colorkey((0,0,255))
        # this code does the blitting
        sprite.set_colorkey((188,71,154))
        surf.blit(sprite, (self.x, self.y))

        # this handles the players rect for hit detection
        # we will handle all hit detection outside of the player class by passing other classes the players rect
        # hit detection for obstacles is done by the obstacles class, and hit detection for AI is done in the AI class
        self.rect[0] = self.x
        self.rect[1] = self.y
        self.rect[2] = self.x + 65 + (self.health * 27)
        self.rect[3] = self.y + 35 + (self.health * 15)

        # this deals with health and world speed

        if self.health > 5: self.health = 5

        if self.health <= 0:
            self.worldSpeed = 0
            surf.blit(deadScreen, (0,0))
        else:
            if not self.isBoost:
                self.worldSpeed = 415 - 35 * self.health + self.hardMode # the test speed before the changes in how we move through world space was 200 but this can be changed







