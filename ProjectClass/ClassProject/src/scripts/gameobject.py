
import random
import pygame

class GameObject(object):
    def __init__(self,name=None,x=300,y=300):
        self.x = x
        self.y = y
        self.name = name
        

    def update(self):
        pass

    def render(self):
        pass

    def onCollide(self):
        pass
        
