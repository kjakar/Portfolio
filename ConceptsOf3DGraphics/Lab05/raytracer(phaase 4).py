import objects3d
import math3d
import pygame



# Pygame window
pygame.init()
screen = pygame.display.set_mode((300, 200))        # Look at test #3
done = False

# Create a camera (use one of the camera test values)
camPos = math3d.VectorN(0, 0, -20)
camUp = math3d.VectorN(0, 1, 0)
COI = math3d.VectorN(0,0,0)
camFOV = 45
camNear = 3.2
cam = objects3d.Camera(camPos, COI, camUp, camFOV, camNear, screen)
objects = []      # See Phase III tester and the numbers on page 4 of the lab pdf
y = 0

sphere = objects3d.Sphere(math3d.VectorN(2,5,3), 7, math3d.VectorN(1,0,0))
objects.append(sphere)
plane1 = objects3d.Plane(math3d.VectorN(0,1,0), 5, math3d.VectorN(0,1,0))
objects.append(plane1)




# Game Loop
while not done:
    # Update
    # Render one line of pixels in the screen (if we haven't rendered all of them
    #  yet).  Do it this way so we give the user a chance to press escape
    # while we're rendering.
    if y < screen.get_height():
        # Render one line
        for x in range(screen.get_width()):
            pos3d = cam.getPixelPos((x, y))     # The ray's origin
            dir3d = pos3d - cam.mPos          # The ray's direction (away from camera)
            R = objects3d.Ray(pos3d, dir3d)
            color = (64, 64, 64)
            # See what the ray hits.  Get color of **closest** hit
			# (You'll need to add some code to make this happen)

            for o in objects:
                result = o.rayIntersection(R)
                print(result)
                if result != None:
                    color = o.mColor * 255
                    print(result)

            screen.set_at((x, y), color)


        y += 1

    # Input
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True

    # Draw

    pygame.display.flip()

pygame.display.quit()