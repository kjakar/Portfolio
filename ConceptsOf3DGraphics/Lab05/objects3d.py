__author__ = 'Alex Jones'
import math
import math3d
import pygame

# Functions =======================================================================================
def dis(x1, y1, x2, y2):
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis

def disVect(vector1, vector2):
    x1 = vector1[0]
    x2 = vector2[0]
    y1 = vector1[1]
    y2 = vector2[1]
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis

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

        newVector = (v.dot(w) / w.dot(w)) * w
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

# classes =========================================================================================

class Ray(object):
    """ An n-dimensional ray [by definition a ray is an origin point and a direction """

    def __init__(self, origin, direction):
        """
        :param origin: the origin POSITION of the ray (a copy of the passed vector is created)
        :param direction: the DIRECTION of the ray (the vector passed in is normalized)
        :return: N/A
        """
        if not isinstance(origin, math3d.VectorN) or not isinstance(direction, math3d.VectorN) or len(origin) != len(direction):
            raise ValueError("You must pass two equal-dimension VectorN's for the origin and direction.")
        self.mOrigin = origin.copy()
        self.mDirection = direction.normalized()

    def getPoint(self, t):
        """
        :param t: A scalar distance along the ray
        :return: The point which is t units along the ray.
        """
        if not isinstance(t, int) and not isinstance(t, float):
            raise ValueError("t must be a scalar.")
        return self.mOrigin + t * self.mDirection

    def drawPygame(self, surf, color = (255,255,255), originRadius = None, endDistance = 1000, thickness=1):
        """
        Draws a 2d representation of this ray to the given pygame surface
        :param surf: a pygame surface
        :param color: a pygame color [defaults to white]
        :param originRadius: the radius of the "ball" to draw at the origin [defaults to None => don't draw the ball]
        :param endDistance: a true Ray doesn't have an end; but in pygame we are actually drawing a line segment.  This
                            value represents how far away from the origin the end point should be.
        :param thickness: the thickness (in pixels) of the line.
        :return: None
        """
        endPt = self.mOrigin + endDistance * self.mDirection
        pygame.draw.line(surf, color, self.mOrigin.int()[0:2], endPt.int()[0:2], thickness)
        if originRadius != None:
            pygame.draw.circle(surf, color, self.mOrigin.int()[0:2], originRadius)

    def getDistanceToPoint(self, p, returnParaPerp = False):
        """
        Returns the minimal distance from point p (which must be of the same dimension as this ray's origin and
           direction.
        :param p: a VectorN POSITION.
        :param returnParaPerp: if True, also return the (unit-length) parallel and perpendicular components created
                                  during this projection operation.  Otherwise, just return the distance.
        :return: If p is on the "front" side of the ray, this method returns the minimal distance to the point from
                 the ray (if you imagine a vector which is perpendicular to the ray, the minimal distance will be the
                 distance from the ray to the point along this perpendicular
        """
        if not isinstance(p, VectorN) or len(p) != len(self.mOrigin):
            raise ValueError("p must be a point of dimension " + str(len(self.mOrigin)))
        dirToP = p - self.mOrigin
        if dirToP.dot(self.mDirection) < 0:
            return None
        paraPart = dirToP.dot(self.mDirection) * self.mDirection
        perpPart = dirToP - paraPart
        if returnParaPerp:
            return (perpPart.magnitude(), paraPart, perpPart)
        else:
            return perpPart.magnitude()

class Camera(object):

    def __init__(self, pos, coi, up, fov , near, surf):

        self.surf = surf
        self.near = near                               # the distance from the view plane to the camera
        self.fov = fov                                 # field of view
        self.fovRad = math.radians(self.fov)           #fov in radians
        self.up = up
        self.coi = coi
        self.mPos = pos
        self.pos = pos
        self.AR = surf.get_width() / surf.get_height()  #aspect ratio

        z = coi - pos
        self.zAxis = z.normalized()
        x = up.crossProduct(self.zAxis)
        self.xAxis = x.normalized()
        y = self.zAxis.crossProduct(self.xAxis)
        self.yAxis = y.normalized()


        self.vph = 2 * (near * math.tan(self.fovRad / 2))  #veiw plane height
        self.vpw = self.vph * self.AR                    #veiw plane width

        a = near * self.zAxis.normalized()
        b = (self.vph / 2) * self.yAxis.normalized()
        c = - ((self.vpw / 2) * self.xAxis.normalized())
        self.VPO = self.pos + (a + b + c)                #veiw plane origin.
        #this is the same output as below self.VPD = (c.magnitude() * 2, b.magnitude() * 2)
        self.VPD = (self.vpw, self.vph)

        #commented lines work

        print(self.xAxis, "x")
        print(self.yAxis, "y")
        print(self.zAxis, "z")
        print(self.AR, "aspect ratio")
        print(self.VPD, "dimensions")
        print(self.VPO, "origin")

    def getPixelPos(self, pixelPos): # this should work but I can't test it till the init is working
        ix = pixelPos[0]
        iy = pixelPos[1]



        #c = - ((self.vpw / 2) * self.xAxis.normalized())
        #d = (c * 2 / self.surf.get_width()) * ix
        #b = (self.vph / 2) * self.yAxis.normalized()
        #e = (b * 2 / self.surf.get_height()) * iy
        s = (ix / (self.surf.get_width()-1)) * self.vpw
        t = (iy / (self.surf.get_height()-1)) * self.vph


        #d = (self.vpw * self.xAxis) / (self.surf.get_width() - 1) * ix # mine
        #e = (self.vph * self.yAxis) / (self.surf.get_height() - 1) * iy #mine
        #d = ((ix / self.surf.get_width() -1 * self.vpw) * self.xAxis)/ 3    #jasons
        #e = ((-(iy / self.surf.get_height() - 1 * self.vph)) * self.yAxis) / 3  #jasons
        p = self.VPO + (s * self.xAxis) - (t * self.yAxis)

        return p

class Plane(object):
    def __init__(self, normal, Dvalue, color):
        self.mNormal = normal.normalized()
        self.mDistance = Dvalue
        self.mColor = color

    def rayIntersection(self, ray):

        """
O> = origin of ray
D^ is the distance of the ray
n^ is the normal of the plane


(p-p0) DOT n = 0 : how we define a plane

l0 + l * t = p : how we define a ray

(l0 + l*t - p0) DOT n = 0 : this inserts equation 2 into equation 1

l * t DOT n + (l0 - p0) DOT n = 0

        (l0 - p0 DOT n       (p0-l0) DOT n
T = -------------------- =  ----------------
            l DOT n             l DOT n

p0 is the planes distance from the world origin : Dvalue
n is the plane normal
P is a vector that can be computed from any point on the plane by subtracting p0: this vector lays in the plane and is perpendicular to the normal of the plane

l0 is the origin of the ray
l is the direction of the ray

"""
        #t = "what we are trying to find"
        l = -ray.mDirection
        l0 = ray.mOrigin
        n = self.mNormal
        p0 = self.mDistance * n
        #p = l0 + l * t

        if l.dot(n) > 0:
            v = p0 - l0
            t = -(v.dot(n) / l.dot(n))
            return t

        else:
            return None


class Sphere(object):
    def __init__(self, centerPos, radius, color):
        self.mCenter = centerPos
        self.mRadius = radius
        self.mSRadius = radius ** 2
        self.mColor = color

    def rayIntersection(self, ray):
        """
         t = Qpara - B
         B = R^2 - Qperp^2
         O = ray.mOrigin
         D = ray.direction
        """

        rotVect = ray.mDirection  #math3d.VectorN(math.cos(num), - math.sin(num), 0)

        # this give all the lines (red green and blue at the moment)
        tankPos = math3d.VectorN(ray.mOrigin[0], ray.mOrigin[1], 0)
        linkPos = math3d.VectorN(200,200,0)
        v = linkPos - tankPos
        added = (tankPos + getPara(v, rotVect) + getPerp(v, rotVect))
        added2 = tankPos + getPara(v, rotVect) #If the magnitude of this is minus the sphere origin is less than the radius you're in the sphere
        added3 = tankPos + getPerp(v, rotVect)
        added4 = tankPos + rotVect.normalized() * 200 #this is get point only change 200 to dist


        test = added2 - self.mCenter #checks if in center


        if test.magnitude() <= self.mRadius:
            green = added2 - ray.mOrigin #this is Qpara
            thing = (self.mSRadius - test.magnitude()**2) ** 0.5
            t = (green.magnitude() - thing)
            print(green.magnitude() - thing)
            return t
        else:
            return None

        #print(test.magnitude(), self.mRadius)
        #print(green.magnitude(), "green")






pygame.display.init()
screen = pygame.display.set_mode((700,150))
camPos = math3d.VectorN(0,0,-20)
coi = math3d.VectorN(0,0,0)
up = math3d.VectorN(0.0, 1, 0.0)
fov = 45.0
near = 3.2

cam = Camera(camPos, coi, up, fov, near, screen)

print(cam.getPixelPos((0,0)), "screenToVP")
print(cam.getPixelPos((699,149)), "screenToVP")
print(cam.getPixelPos((350,75)), "screenToVP")
print(cam.getPixelPos((113,23)), "screenToVP")
print(cam.getPixelPos((623,83)), "screenToVP")
