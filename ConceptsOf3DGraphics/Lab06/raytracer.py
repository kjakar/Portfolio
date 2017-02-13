import objects3d
import math3d

class Raytracer(object):
    def __init__(self, camera):
        self.mCamera = camera
        self.mRenderSurf = self.mCamera.mRenderSurf
        self.mBackgroundColor = math3d.VectorN(0.3, 0.3, 0.3)
        self.mObjects = []
        self.mLights = []


    def addObject(self, o):
        self.mObjects.append(o)

    def addLight(self, light):
        self.mLights.append(light)

    def castRay(self, R):
        # set up =======================================================================================================
        closestObject = None
        closestDist = 0
        normal = None
        final = math3d.VectorN(0,0,0) # this is the final color that will be returned
        p =  math3d.VectorN(0,0,0)
        inShadow = False

        for o in self.mObjects:
            result = o.rayIntersection(R)
            if result != None and (closestObject == None or result < closestDist):
                closestObject = o
                closestDist = result

        p = R.getPoint(closestDist)

        # Test for shadows =============================================================================================
        for light in self.mLights:
            newRayDirection = light.mPos - p
            newRay = objects3d.Ray(p,newRayDirection)
            for o in self.mObjects:
                result = o.rayIntersection(newRay)
                if o != closestObject and result != None and result >= 0.1:
                    if result < newRayDirection.magnitude() - 1:
                        #pass
                        inShadow = True


        if closestObject == None:
            return self.mBackgroundColor

        if inShadow == True:
            return closestObject.mAmbient
        # lighting equations ===========================================================================================
        elif isinstance(closestObject, objects3d.Sphere): # Spheres
            final += closestObject.mAmbient
            center = closestObject.mCenter
            r = p - center
            normal = r.normalized()

            # diffuse math ============================
            for light in self.mLights:
                L = light.mPos - p
                Lhat = L.normalized()
                cos = normal.dot(Lhat)
                if cos <= 0:
                    pass
                elif cos > 0:
                    dStr = cos #Lhat.dot(normal)
                    cDiff = dStr * (light.mDiffuse.pairWise(closestObject.mDiffuse))
                    final += cDiff

            # specular math ============================
                    #we have L and L hat
                    hardness = closestObject.mHardness
                    R = 2*(Lhat.dot(normal)* normal - Lhat)
                    V = self.mCamera.mPos - p # I don't know what C is # it's the camera pos
                    Vhat = V.normalized()
                    sStr = Vhat.dot(R)
                    if sStr < 0:
                        pass
                    else:
                        cSpec = sStr**hardness * (light.mSpecular.pairWise(closestObject.mSpecular))
                        final +=cSpec

        elif isinstance(closestObject, objects3d.Plane): # Planes
            final += closestObject.mAmbient
            normal = closestObject.mNormal

            for light in self.mLights:
            # diffuse math =============================
                L = light.mPos - p
                Lhat = L.normalized()
                cos = normal.dot(Lhat)
                if cos <= 0:
                    pass
                elif cos > 0:
                    dStr = cos #Lhat.dot(normal)
                    cDiff = dStr * (light.mDiffuse.pairWise(closestObject.mDiffuse))
                    final += cDiff
            # specular math ============================
                    #we have L and Lhat
                    hardness = closestObject.mHardness
                    R = 2*(Lhat.dot(normal)* normal - Lhat)
                    V = self.mCamera.mPos - p # I don't know what C is # it's the camera pos
                    Vhat = V.normalized()
                    sStr = Vhat.dot(R)
                    if sStr < 0:
                        pass
                    else:
                        cSpec = sStr**hardness * (light.mSpecular.pairWise(closestObject.mSpecular))
                        final +=cSpec

        final.clamp(1,0)
        return final

    def renderOneLine(self, y):
        for x in range(self.mRenderSurf.get_width()):
            if x == self.mRenderSurf.get_width() // 2 and y == self.mRenderSurf.get_height() // 2:
                foo = 5
            rayOrigin = self.mCamera.getViewplanePosition(x, y)
            rayDirection = rayOrigin - self.mCamera.mPos
            #print(rayOrigin, rayDirection)
            ray = objects3d.Ray(rayOrigin, rayDirection)
            color = self.castRay(ray)
            self.mRenderSurf.set_at((x, y), (255 * color).int())