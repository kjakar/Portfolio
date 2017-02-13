

class VectorN(object):
    """
    This class represents a general-purpose vector class.  We'll
    add more to this in later labs.  For now, it represents a
    position and/or offset in n-dimensonal space.
    """

    def __init__(self, *args):
        """
        The constructor
        :param args: This is a variable-length argument-list.  In reality, you create a VectorN like this:
               v = VectorN(1, 2, 3)
        :return: N/A for constructors
        """
        self.__mData = []
        for value in args:
            self.__mData.append(float(value))
        self.__mDim = len(self.__mData)

    def __str__(self):
        """
        Note: You don't normally call this directly.  It is called indirectly when you do something like:
            v = VectorN(1, 2, 3)
            x = str(v)               # Same as x = v.__str__()
            print(v)                 # print calls str internally
        :return: The string-representation of this VectorN
        """
        s = "<Vector" + str(self.__mDim) + ": "
        for i in range(len(self.__mData)):
            s += str(self.__mData[i])
            if i < self.__mDim - 1:
                s += ", "
        s += ">"
        return s

    def __len__(self):
        """
        Note: You don't normally call this method directly.  It's called by the built-in len function
            v = VectorN(1, 2, 4)
            print(len(v))           # 3
        :return: An integer indicating the dimension of this vector
        """
        return self.__mDim

    def __getitem__(self, index):
        """
        Note: You don't normally call this method directly.  It's called by using [] on a VectorN
            v = VectorN(1, 2, 3)
            print(v[0])                 # 1
            print(v[-1])                # 3
        :param index: An integer.  A python exception will be thrown if it's not a valid position in self.__mData
        :return: The float value at position index.
        """
        return self.__mData[index]

    def __setitem__(self, index, newval):
        """
        This method is similar to __getitem__, but it is called when we assign something to an index
           v = VectorN(1, 2, 3)
           v[0] = 99
           print(v)                 # <Vector3: 1.0, 2.0, 99.0>
        :param index: An integer.  A python exception will be thrown if it's not a valid position in self.__mData
        :param newval: A value that can be converted to a float using the float function
        :return: None
        """
        self.__mData[index] = float(newval)

    def __eq__(self, other):
        """
        Note: This method isn't normally called directly.  Instead, it is called indirectly when a VectorN
              is on the left-hand side of an ==.  It returns True if the values within the other vector
              are the same as those in this vector.
        :param other: any value
        :return: a boolean.  True if the other thing is a VectorN *and* has the same values as this VectorN.
        """
        if isinstance(other, VectorN) and len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        else:
            return False


    def copy(self):
        """
        Creates a 'deep' copy of this VectorN and returns it
        :return: a new VectorN copy of this VectorN
        """
        return VectorN(*self.__mData)

    def int(self):
        """
        :return: A tuple containing integer copies of the values in this VectorN.
        """
        L = []
        for i in range(self.__mDim):
            L.append(int(self[i]))
        return tuple(L)
#======================================== lab02 item (uncompleted) ===================================================#
    def __add__(self, other): #working ===============================================
        """
        this will add two VectorN's if they are of the same dimensions
        :param other: this needs to be another ZectorN value
        """
        if isinstance(other, VectorN):
            if self.__mDim == other.__mDim:
                c = self.copy()
                for i in range(other.__mDim):
                    c.__mData[i] += other.__mData[i]
                return c

            else:
                raise ValueError("Cannot add two vectors with different dimensions")
        else:
            raise ValueError("Cannot add VectorN with non-VectorN object")

    def __neg__(self): # working =====================================================
        """
        this is the inverse of the vectorN ([1,1,1] will turn into [-1,-1,-1])
        """
        c = self.copy()
        for i in range(self.__mDim):
            c.__mData[i] = self.__mData[i] * -1
        return c

    def __mul__(self, number): # working =============================================
        """
        this will multiply two vectors with the same dimnsions
        :param number: this needs to be a scalar value (int or float)
        """
        if isinstance(number, float) == True or isinstance(number, int):
            c = self.copy()
            for i in range(self.__mDim):
                c.__mData[i] = c.__mData[i] * number
            return c
        else:
            raise ValueError("You can only multiply a VectorN with a float or int object")

    def __rmul__(self, number): # working ============================================
        """
        this will multiply two vectors with the same dimnsions
        :param number: this needs to be a scalar value (int or float)
        """
        if isinstance(number, float) == True or isinstance(number, int):
            c = self.copy()
            for i in range(self.__mDim):
                c.__mData[i] = c.__mData[i] * number
            return c
        else:
            raise ValueError("You can only multiply a VectorN with a float or int object")

    def __sub__(self, other): # working =============================================
        """
        this will subtract two VectorN's if they are of the same dimensions
        :param other : this needs to be another VectorN value
        """
        if isinstance(other, VectorN):
            if self.__mDim == other.__mDim:
                c = self.copy()
                for i in range(other.__mDim):
                    c.__mData[i] -= other.__mData[i]
                return c

            else:
                raise ValueError("Cannot add two vectors with different dimensions")
        else:
            raise ValueError("Cannot add VectorN with non-VectorN object")

    def __truediv__(self, other):
        """
        this will divide  VectorN by a scalar value
        :param other: this needs to be a scalar value (int or float)
        """
        if isinstance(other, float) == True or isinstance(other, int):
            c = self.copy()
            for i in range(self.__mDim):
                c.__mData[i] = c.__mData[i] / other
            return c
        else:
            raise ValueError("You can only devide a VectorN with a float or int object")

    def magnitudeSquared(self):
        """
        this will give the value of the VectorN (using the pythagorean theorem) only not under the square root
        """
        number = 0
        for i in range (self.__mDim):
            number += self.__mData[i] ** 2

        return number

    def magnitude(self):
        """
        this will give the value of the VectorN (using the pythagorean theorem) under the square root
        """
        number = self.magnitudeSquared() ** 0.5

        return number

    def isZero(self):
        """
        This will check if the magnitude of the VectorN is zero.
        """
        number = self.magnitude()

        if number == 0.0:
            return True
        else:
            return False

    def normalized(self):
        """
        This returns a unit vector based on this VectorN
        """
        divide = self.magnitude()

        if divide != 0 or divide != 1:
            c = self.copy()
            for i in range(self.__mDim):
                if c.__mData[i] != 0:
                    c.__mData[i] = c.__mData[i] / divide

            return c
        elif divide == 1:
            return self
        else:
            raise ValueError("Magnitued of this vector is 0")


    def dot(self, other):
        """
        this returns the dot product of two VectorN's with the same dimentions
        :param other: another VectorN with the same dimensions
        """

        if isinstance(other, VectorN) and self.__mDim == other.__mDim:
            number = 0
            for i in range(self.__mDim):
                number += (self.__mData[i] * other.__mData[i])
            return number
        else:
            raise ValueError("You must use two VectorN's(of the same dimension) to get the dot product")

    def crossProduct(self, other):
        """
        this returns a NEW VectorN(a vector 3) that is the cross product of the VectorN's with the same dimensions(that are greater than 2)
        :param other: another VectorN with the same dimensions
        """

        if isinstance(other, VectorN)and self.__mDim == other.__mDim and self.__mDim == 3:
            x1 = self.__mData[0]
            y1 = self.__mData[1]
            z1 = self.__mData[2]
            x2 = other.__mData[0]
            y2 = other.__mData[1]
            z2 = other.__mData[2]
            cx = (y1 * z2) - (z1 * y2)
            cy = (z1 * x2) - (x1 * z2)
            cz = (x1 * y2) - (y1 * x2)
            c = VectorN(cx,cy,cz)
            return c
        else:
            raise ValueError("You can only fine the cross product of two VectorN's with 3 dimensions")




if __name__ == "__main__":
    # Note: By adding this if statement, we'll only execute the following code
    # if running this module directly (F5 in Idle, or the play button in
    # pyscripter).  But...if we import this module from somewhere else (like our
    # raytracer), it won't execute this code.  Neat trick, huh?
    import pygame

    v = VectorN(5, 5, 5)
    print(v)                                    # <Vector5: 0.0, 0.0, 0.0, 0.0, 0.0>
    w = VectorN(1.2, "7", 5)
    # q = VectorN(pygame.Surface((10,10)))      # Should raise an exception
    # q = VectorN(1.2, "abc", 5)                # Should raise an exception
    print(w)                                    # <Vector3: 1.2, 7.0, 5.0>
    z = w.copy()
    z[0] = 9.9
    z[-1] = "6"
    # z["abc"] = 9.9					 	    # Should raise an exception
    print(z)                                    # <Vector3: 9.9, 7.0, 6.0>
    print(w)                                    # <Vector3: 1.2, 7.0, 5.0>
    print(z == w)                               # False    [same as print(z.__eq__(w))]
    print(z == VectorN(9.9, "7", 6))            # True
    print(z == 5)                               # False
    print(z[0])                                 # 9.9
    print(len(v))                               # 5
    print(w.int())        	                    # (1, 7, 5)

    print("===================================================================================")
    print(v)
    print(w + v + v)
    print(2 * w, "hello")
    print(w, v)
    print(w.crossProduct(v))
    print("hi")
    g = VectorN(3,2,1)

    print(g.magnitudeSquared())
    print(g.magnitude())
    print(g.isZero())
    print(g.normalized().magnitude())






    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")#==========================================

    v = VectorN(4,7,-3)
    w = VectorN(2,0,6)
    q = VectorN(5,9,-12)
    p = VectorN(0,0,0,0,0,0)
    print(v + w)                        # <Vector3: 6.0, 7.0, 3.0>
    print(v + w + q)                    # <Vector3: 11.0, 16.0,-9.0>
    #print(v + 7)                       #ValueError: Youcan only add another Vector3 to this Vector3   (you passed '7').
    print(v-w)                          # <Vector3: 2.0, 7.0,-9.0>
    #print(v-"abc")                     #ValueError: You can only subtract another Vector3 from this Vector3 (you passed 'abc').
    print(v * 2)                        # <Vector3: 8.0, 14.0, -6.0>
    print(3 * v)                        # <Vector3: 12.0, 21.0, -9.0>
    print(v / 2)                        # <Vector3: 2.0, 3., -1.5>
    #print(v / w)                       # ValueError: You can only divide this Vector3 by a scalar.
    # You attempted to divide by '<Vector3: 2.0, 0.0, 6.0>'.
    #print(2 / v)                       # TypeError: unsupported operand type(s) for /: 'int' and 'VectorN'
    # Note: We'll do something like multiplication between two vectors, but there are many types of vector-vector
    #    "multiplication" (dot-product, cross-product, etc.).  To avoid confusion, I'll dis-allow vector * vector
    #print(v * w)                       # ValueError: You can only multiply this Vector3 and a scalar.
    #You attempted to multiply by '<Vector3: 2.0, 0.0, 6.0>'.
    print(-v)                          # <Vector3: -4.0, 7.0, 3.0>
    print(v.magnitude())                # 8.602325267042627
    print(v.magnitudeSquared())         # 74.0
    print(v.normalized())               # <Vector3: 0.46499055497527714, 0.813733471206735, -0.34874291623145787>
    print(v.normalized().magnitude())   # 1.0
    print(q.isZero())                   # False
    print(p.isZero())                   # True