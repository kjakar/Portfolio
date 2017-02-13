#lab03c
#Alexander Jones
import pygame
import time
import random

pygame.display.init()
screen = pygame.display.set_mode((800, 600), 0, 0)
pygame.display.set_caption("Srpite animation")

sprite = pygame.image.load("bjorn.bmp")          # img is a Surface too
sprite.set_colorkey((97, 68, 43))              # Makes any black pixels
                                             #   in the link image
                                             #   transparent.
world = pygame.image.load("floor.bmp")
smallImg = pygame.transform.scale(sprite, (64, 64))  # smallImg is a 64x64
                                                  # version of img.

worldX = 200
worldY = 100

# Drawing code
# ... draw the background
#screen.blit(world, (0,0), (worldX,worldY,800,600))
# ... draw link twice on top of it.
#screen.blit(smallImg, (0,0))
#screen.blit(smallImg, (400 - smallImg.get_width() / 2, \
  #                     300 - smallImg.get_height() / 2))

screen.blit(world, (0, 0))
#screen.blit(sprite, (0,0), (0, 0, 128, 128))

def drawSprite(r, c, x, y):
    # enter the row and column to call the sprite
    # r = row, c = column, x and y = position.
    screen.blit(sprite, (x, y), ( (0 + (128 * c)), (0 + (128 * r)), 128, 128,))
    pygame.display.flip()
    time.sleep(0.2)
    screen.blit(world, (0,0))
    return


#to the right
drawSprite(0,0,100,0)

drawSprite(0,1,110,0)

drawSprite(0,2,120,0)

drawSprite(0,3,130,0)

drawSprite(0,4,140,0)

drawSprite(0,5,150,0)

drawSprite(0,6,150,0)

drawSprite(0,7,160,0)

drawSprite(0,0,170,0)

drawSprite(0,1,180,0)

drawSprite(0,2,190,0)

drawSprite(0,3,200,0)

drawSprite(0,4,210,0)

drawSprite(0,5,220,0)

drawSprite(0,6,230,0)

drawSprite(0,7,240,0)

#south east
drawSprite(7,0,240,0)

drawSprite(7,1,110,0)

drawSprite(7,2,120,0)

drawSprite(7,3,130,0)

drawSprite(7,4,140,0)

drawSprite(7,5,150,0)

drawSprite(7,6,150,0)

drawSprite(7,7,160,0)




drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)

drawSprite(0,0,0,0)





#===================END STUFF===================================================
pygame.display.flip()
time.sleep(3)
pygame.display.quit()
