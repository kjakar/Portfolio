__author__ = 'Alex Jones'

import math
import math3d
import pygame


class Tank(object):

    def __init__(self, posistion):
        self.pos = posistion
        self.angle = 90
        num = math.radians(self.angle)
        self.angleVector = math3d.VectorN(math.cos(num), - math.sin(num),0)

    def rotate(self, target, speed, deltaTime): # will pick the best direction to rot, but will not rotate?
        if self.angle >= 360:
            self.angle = 0
        elif self.angle < 0:
            self.angle = 359

        """if self.angleVector.crossProduct(target)[2] < 0:
            self.angle += speed * deltaTime
        elif not self.angleVector.crossProduct(target)[2] < 0:
            self.angle -= speed * deltaTime"""

        #self.angle += speed * deltaTime # this rotates clock wise
        num = math.radians(self.angle)
        self.angleVector = math3d.VectorN(math.cos(num), - math.sin(num),0)

        v = target - self.pos
        vHat = v.normalized()
        g = self.angleVector - vHat
        gHat = g.normalized()
        rot = math.atan2(vHat[1], vHat[0])
        rot2 = math.atan2(gHat[1], gHat[0])
        print(rot2, gHat)
        #print(math.degrees(rot), "=======================================")
        #print(self.angle)
