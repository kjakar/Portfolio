__author__ = 'Alex'

import pygame

scuba = pygame.image.load("..\\assets\\images\\scuba.png")


class obstacle(object):

    def __init__(self, size, location, pos):
        self.size = size
        self.y = 0
        self.x = pos
        self.rect = []
        self.center = 0
        for i in range(20):
            self.rect.append(0)
        # this sets up the position of the obstacle
        if size == "small":
            if location == "top":
                self.y = 68
            if location == "middle":
                self.y = 335
            if location == "bottom":
                self.y = 620
        if size == "medium":
            if location == "top":
                self.y = 68
            if location == "middle":
                self.y = 310
            if location == "bottom":
                self.y = 585
        if size == "large":
            if location == "top":
                self.y = 68
            if location == "middle":
                self.y = 260
            if location == "bottom":
                self.y = 485
        if size == "elarge":
            if location == "top":
                self.y = 68
            if location == "middle":
                self.y = 200
            if location == "bottom":
                self.y = 365

    def update(self, dt, speed):
        # this updates the obstacles rect every frame
        self.rect[0] = self.x
        self.rect[1] = self.y

        if self.size == "small":
            self.rect[3] = 50
        if self.size == "medium":
            self.rect[3] = 100
        if self.size == "large":
            self.rect[3] = 200
        if self.size == "elarge":
            self.rect[3] = 300
        self.rect[2] = 50 #self.x + 75

        self.center = self.rect[0] + (self.rect[2] / 2)

        #this moves the obstacle
        """
        # this is from the level calls just as an example
    def update(self, deltaTime, speed):
        if self.playersList[0].distance < 100:
            self.pos[0] += deltaTime * speed
            self.goalPos[0] += deltaTime * speed * 2
            self.imagePos[0] += deltaTime * speed
            for player in self.playersList:
                player.distance += 1 * deltaTime * player.worldSpeed / 100
                if player.distance > 100:
                    player.distance = 100
        """
        self.x += dt * speed * 2

    def hitDetect(self, other): # this checks all 4 corners of the player object
        # note : the player rect and the obstacle rect do not work the same way,
        # the players is like 100-200 and the obstacle is like 100+100
        # just to keep in mind when testing hit detection between different objects

        if other.rect[0] >= self.rect[0] and other.rect[0] <= self.rect[2] + self.rect[0]: # top left check
            if other.rect[1] >= self.rect[1] and other.rect[1] <= self.rect[3] + self.rect[1]:
                return True
        elif other.rect[2] >= self.rect[0] and other.rect[2] <= self.rect[2] + self.rect[0]: # top right check
            if other.rect[1] >= self.rect[1] and other.rect[1] <= self.rect[3] + self.rect[1]:
                return True
        elif other.rect[0] >= self.rect[0] and other.rect[0] <= self.rect[2] + self.rect[0]: # bottom left check
            if other.rect[3] >= self.rect[1] and other.rect[3] <= self.rect[3] + self.rect[1]:
                return True
        elif other.rect[2] >= self.rect[0] and other.rect[2] <= self.rect[2] + self.rect[0]: # bottom right check
            if other.rect[3] >= self.rect[1] and other.rect[3] <= self.rect[3] + self.rect[1]:
                return True
        else:
            return False

    def render(self, surf):
        if self.size == "small":
            scuba1 = pygame.transform.scale(scuba,(int(50),int(50)))
        if self.size == "medium":
            scuba1 = pygame.transform.scale(scuba,(int(50),int(100)))
        if self.size == "large":
            scuba1 = pygame.transform.scale(scuba,(int(50),int(200)))
        surf.blit(scuba1, (self.rect[0],self.rect[1],self.rect[2],self.rect[3]))
        #pygame.draw.rect(surf, (144,0,144), (self.rect[0],self.rect[1],self.rect[2],self.rect[3]))
