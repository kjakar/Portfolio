#Ashton Boland

import random
import entity

class Actor(entity.Entity):
    def __init__(self, wall = 30, att = 10, damage = 10):
        super(Entity,self).__init__(name = name, x = 300, y = 300, color = color, vel = 0, health = 0, speed = 0, angle = 0, alpha = 0, surface = pygame.Surface((int(radius*2),int(radius*2))))

        #TODO: CALL HITBOX CLASS

        #height = health 
        #width = health * 2
        #pos = ((x-(width/2)),(y-(width/2)))

        #self.hitbox = (pos,height,width)
        
        self.damage_taken = damage
        self.attack = att
        self.wall_damage = wall

        self.pos = (x,y)

        #bigger = slower
        self.max_speed = (50 - health)
        
        if self.max_speed < 0:
            self.max_speed = 0
        self.max_speed += 10

        #distance down lap
        self.distance = 0
        
    def updateDir(self,move = 0):
        """Updates player direction and velocity"""
        
        if move == "up":
            vel += speed
            if angle < 90:
                angle += ((90 - angle) * 0.1)
            if angle > 90:
                angle -= ((angle - 90) * 0.1)

        if move == "down":
            vel += speed
            if angle < 90:
                angle += ((270 - angle) * 0.1)
            if angle > 90:
                angle -= ((angle - 270) * 0.1)

        if move == "left":
            vel += speed
            if angle < 90:
                angle += ((180 - angle) * 0.1)
            if angle > 90:
                angle -= ((angle - 90) * 0.1)

        if move == "right":
            vel += speed
            if angle < 90:
                angle += ((angle) * 0.1)
            if angle > 90:
                angle -= ((angle) * 0.1)
            
        else:
            vel = 0

    def move(self,dt):
        """Moves the player based on the update function"""

        #keep speed limited
        if vel >= self.max_speed:
            vel = self.max_speed

        #apply changes to pos
        dx = self.speed * math.cos(math.radians(self.angle)) * dt
        dy = -self.speed * math.sin(math.radians(self.angle)) * dt

        self.x += dx
        self.y += dy
        self.pos = (self.x,self.y)

    def update(self):
        """Inherits Entity's update function"""
        
        super(Entity,self).update(dt)

    def render(self,screen,dt):
        """Inherits Entity's render function and displays on screen."""
        
        super(Entity,self).render(screen,dt)
        pygame.draw.circle(screen,(255,255,255),(pos),30,0)

    def onCollide(self,other):
        """Calculates damage from collision"""
        
    # Get Eaten 
        if other.health > self.health:
            self.health -= self.damage_taken
    # Eat       
        if other.health < self.health:
            self.health += self.attack
    # Collide with wall        
        if other.health == wall:
            self.health -= self.wall_damage

   
           
        
    
