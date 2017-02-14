#Ashton Boland

import random
import pygame
import gameobject
import math

class Entity(gameobject.GameObject):
    def __init__(self, health = 0, color = (255,255,0)):
        super(GameObject,self).__init__(name=name,x=300,y=300)
        self.color = color
        self.vel = 0
        self.health = health
        self.speed = 0
        self.angle = 0
        self.alpha = 255
        self.surface = pygame.Surface(health,health * 2)
        
        

    def update(self,dt):
        pass

    def render(self,screen):
        self.surface.fill((0,0,0))
        self.surface.set_colorkey((0,0,0))
        self.surface.set_alpha(self.alpha)
        pygame.draw.circle(self.surface,(color),(int(20),int(20)),int(self.radius))
        screen.blit(self.surface, (self.x,self.y))

    def onCollide(self):
        pass
