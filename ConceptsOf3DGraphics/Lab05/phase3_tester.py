import pygame
import math3d      # You'll need your math3d file to run this...
import objects3d   # You'll need your math3d file to run this...




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


def drawShape(surf, s):
    # You might *not* want to comment anything here -- these are the attributes / class names I'd like
    # you to use in this lab.
    pygameColor = None
    if hasattr(s, "mColor"):
        pygameColor = (s.mColor * 255).int()
    if isinstance(s, objects3d.Ray):
        pygame.draw.circle(surf, (255,255,255), s.mOrigin.int()[0:2], 4)
        pygame.draw.line(surf, (255,255,255), s.mOrigin.int()[0:2], s.getPoint(2000).int()[0:2])
    elif isinstance(s, objects3d.Sphere):
        pygame.draw.circle(surf, pygameColor, s.mCenter.int()[0:2], s.mRadius, 2)
    elif isinstance(s, objects3d.Plane):
        # This is an iteresting one.  We first have to determine if this plane is more horizontal (the normal
        # will be more closely-aligned with an up vector) than vice-versa.  Note: the normal is perpendicular to the
        # plane.  So to test for vertical-ish-ness, you actually look for a horizontal normal.  Then, solve the plane
        # equation for the points on the sides (for horizontal planes) or top / bottom
        # (for vertical planes) of the screen.
        vertAlign = abs(math3d.VectorN(1, 0, 0).dot(s.mNormal))
        horzAlign = abs(math3d.VectorN(0, 1, 0).dot(s.mNormal))
        if vertAlign > horzAlign:
            h = surf.get_height() - 1
            pt1 = math3d.VectorN((s.mDistance - s.mNormal[1]) / s.mNormal[0], 0)
            pt2 = math3d.VectorN((s.mDistance - h * s.mNormal[1]) / s.mNormal[0], h)
        else:
            w = surf.get_width() - 1
            pt1 = math3d.VectorN(0, (s.mDistance - s.mNormal[0]) / s.mNormal[1])
            pt2 = math3d.VectorN(w, (s.mDistance - w * s.mNormal[0]) / s.mNormal[1])
        pygame.draw.line(surf, pygameColor, pt1.int(), pt2.int(), 2)
        # Draw the normal vector
        midPt = (pt1 + pt2) * 0.5
        normal2D = math3d.VectorN(s.mNormal[0], s.mNormal[1])
        pygame.draw.line(surf, pygameColor, midPt.int(), (midPt + 10 * normal2D))
    elif isinstance(s, objects3d.AABB):
        pygame.draw.rect(surf, pygameColor, (s.mMinPoint[0], s.mMinPoint[1], \
                                          s.mMaxPoint[0] - s.mMinPoint[0], s.mMaxPoint[1] - s.mMinPoint[1]), 2)



# Pygame setup
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Courier New", 15)
done = False

# "Scene" setup -- feel free to modify this and / or comment out sections as you test.
allShapes = []
mainRay = objects3d.Ray(math3d.VectorN(400, 300, 0), math3d.VectorN(1, 0, 0))
allShapes.append(mainRay)
allShapes.append(objects3d.Sphere(math3d.VectorN(200, 200, 0), 50, math3d.VectorN(1, 1, 0)))
allShapes.append(objects3d.Plane(math3d.VectorN(0,1,0), 10, math3d.VectorN(0,1,0)))
allShapes.append(objects3d.Plane(math3d.VectorN(20,1,0), 60, math3d.VectorN(0,1,1)))
allShapes.append(objects3d.Plane(math3d.VectorN(-2, -7, 0), -600, math3d.VectorN(1,0.5,0)))
#allShapes.append(objects3d.AABB(math3d.VectorN(500,450,0), math3d.VectorN(660,420,0), math3d.VectorN(0,0,1)))


# Main Loop
while not done:
    ##############################
    # UPDATES                    #
    ##############################
    # ... for everything but Ray's, call the rayIntersection method of each shape and collect any hit-points
    hitPoints = []
    hitColors = []
    for s in allShapes:
        if hasattr(s, "rayIntersection"):
            t = s.rayIntersection(mainRay)
            if t != None:
                hitPoints.append(mainRay.getPoint(t))
                hitColors.append((s.mColor * 255).int())


    ##############################
    # INPUT-HANDLING             #
    ##############################
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        done = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    # ... device-polling
    mx, my = pygame.mouse.get_pos()
    mouseButtons = pygame.mouse.get_pressed()
    if mouseButtons[2]:
        # Right-clicking.  Update the ray direction.
        mousePos = math3d.VectorN(mx, my, 0)
        mouseDir = mousePos - mainRay.mOrigin
        if not mouseDir.isZero():
            mainRay.mDirection = mouseDir.normalized()
    elif mouseButtons[0]:
        # Left-clicking.  Update the ray origin
        mainRay.mOrigin = math3d.VectorN(mx, my, 0)


    ##############################
    # DRAWING                    #
    ##############################


    screen.fill((0,0,0))
    # ... draw all the shapes using the helper function above
    for curShape in allShapes:
        drawShape(screen, curShape)
    # ... draw any intersection points
    for i in range(len(hitPoints)):
        # Occasionally, we could get a point that's *really* far away (probably from the plane) -- this could give
        # you a "OverflowError".  Just ignore it (the point's off-screen anyhow)
        try:
            hitPt = hitPoints[i].int()[0:2]
            pygame.draw.circle(screen, hitColors[i], hitPt, 5)
            pygame.draw.circle(screen, (255,0,0), hitPt, 5, 2)
        except OverflowError:
            pass
    screen.blit(font.render("Left click to set ray origin, Right-click to set ray direction", False, (128,128,128)), (0,580))





    pygame.display.flip()

pygame.font.quit()
pygame.display.quit()