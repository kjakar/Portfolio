 #lab03c
#Alexander Jones
import pygame
import time


pygame.display.init()
screen = pygame.display.set_mode((800, 600), 0, 0)
pygame.display.set_caption("Srpite animation")

sprite = pygame.image.load("bjorn.bmp")
sprite.set_colorkey((97, 68, 43))
world = pygame.image.load("floor.bmp")

                                                

worldX = 200
worldY = 100

screen.blit(world, (0, 0))

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
drawSprite(7,0,240,10)

drawSprite(7,1,250,20)

drawSprite(7,2,260,30)

drawSprite(7,3,270,40)

drawSprite(7,4,280,50)

drawSprite(7,5,290,60)

drawSprite(7,6,300,70)

drawSprite(7,7,310,80)


#South
drawSprite(6,0,310,80)

drawSprite(6,1,310,90)

drawSprite(6,2,310,100)

drawSprite(6,3,310,110)

drawSprite(6,4,310,120)

drawSprite(6,5,310,130)

drawSprite(6,6,310,140)

drawSprite(6,7,310,150)

drawSprite(6,0,310,160)

drawSprite(6,1,310,170)

drawSprite(6,2,310,180)

drawSprite(6,3,310,190)

drawSprite(6,4,310,200)

drawSprite(6,5,310,210)

drawSprite(6,6,310,220)

drawSprite(6,7,310,230)

#===================END STUFF===================================================
pygame.display.flip()
time.sleep(3)
pygame.display.quit()
