__author__ = 'Alex Jones'

import math3d
import pygame

# functions ============================================================================================================

def getPara(vector1, vector2):
    """
    :param vector1: This is the vector you are projecting on.
    :param vector2: this is the secondary vector.
    :return: a new vector parallel to vector 1 but the length it would need to be to make a right triangle with vector2
    """
    if isinstance(vector1, math3d.VectorN) and isinstance(vector2, math3d.VectorN):
        #if vector2.__mDim == 3 and vector1.__mDim == vector2.__mDim:
        v = vector1
        w = vector2

        newVector = (v.dotProduct(w) / w.dotProduct(w)) * w
        return newVector
    else:
        return ValueError("getPara can only use two vectors of the same dimensions.")

def getPerp(vector1, vector2):
    """
    :param vector1: This is the vector you are projecting on.
    :param vector2: this is the secondary vector.
    :return: a new vector perpendicular  to vector 1 but the length it would need to be to make a right triangle with vector2
    """
    if isinstance(vector1, math3d.VectorN) and isinstance(vector2, math3d.VectorN):
        vPara = getPara(vector1, vector2)
        v = vector1
        newVector = v - vPara

        return newVector
    else:
        return ValueError("getPerp can only use two vectors of the same dimensions.")

def disVect(vector1, vector2):
    x1 = vector1[0]
    x2 = vector2[0]
    y1 = vector1[1]
    y2 = vector2[1]
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis


# Classes ==============================================================================================================

class Ray(object):

    def __init__(self, vector1, vector2):
        self.pos = vector1
        self.angle = vector2

    def getPt(self, distance):
        num = self.pos + self.angle.normalized() * distance
        return num

    def drawPygame(self, surfface):
        num = self.angle.normalized() * 2000
        pygame.draw.line(surfface, (0,0,0), (int(self.pos[0]), int(self.pos[1])),(int(num[0]), int(num[1])), 3)

    def getDistanceToPoint(self, vector):
        v = vector - self.pos
        added2 = self.pos + getPara(v, self.angle)
        dist = disVect(vector, added2)
        return dist

v1 = math3d.VectorN(10,10,0)
v2 = math3d.VectorN(30,20,0)
rotVect = math3d.VectorN(0,-1,0)

ray = Ray(v1, rotVect)



