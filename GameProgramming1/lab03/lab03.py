#lab03
#Alexander Jones
import pygame
import time

pygame.display.init()
screen = pygame.display.set_mode((800, 600), 0, 0)
pygame.display.set_caption("Lab03")

#backGround
pygame.draw.rect(screen, (0, 50, 250), (0, 0, 800, 400), 0)
pygame.draw.rect(screen, (0, 250, 50), (0, 299, 800, 400), 0)

#Flower
pygame.draw.rect(screen, (42, 122, 20), (399, 400, 20, 150), 0)
pygame.draw.circle(screen, (232, 240, 17), (409, 355), 35, 0)
pygame.draw.circle(screen, (232, 240, 17), (434, 385), 35, 0)
pygame.draw.circle(screen, (232, 240, 17), (379, 385), 35, 0)
pygame.draw.circle(screen, (232, 240, 17), (434, 420), 35, 0)
pygame.draw.circle(screen, (232, 240, 17), (385, 420), 35, 0)
pygame.draw.circle(screen, (120, 50, 20), (409, 400), 25, 0)

#Bee
pygame.draw.circle(screen, (204, 204, 204), (95, 225), 18, 0)
pygame.draw.line(screen, (0, 0, 0), (95, 260), (65, 240), 2)
pygame.draw.circle(screen, (203, 209, 33), (100, 250), 25, 0)
pygame.draw.circle(screen, (174, 179, 34), (122, 250), 15, 0)
pygame.draw.circle(screen, (0, 0, 0), (125, 250), 3, 0)
pygame.draw.circle(screen, (0, 0, 0), (120, 250), 3, 0)
pygame.draw.line(screen, (0, 0, 0), (100, 225), (100, 275), 5)


#===================END STUFF===================================================
pygame.display.update()
time.sleep(15)
pygame.display.quit()
