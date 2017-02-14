

def distance(x1,x2,y1,y2):
    return ((((y2-y1)**2)+((x2-x1)**2))**0.5)

class Hitbox:
    def __init__(self,pos,width,height,type):
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos,(width,height))
        self.type = hitType

    def update(self,movement,size):
        pass
        # instead of updating, we can re create the hitbox after movement
        # after update functions put  " self.hitbox = Hitbox(pos,w,h)
        #self.rect.move(pos[0]+movement[0],pos[1]+movement[1])
        #self.rect.inflate(self.width+size[0],self.height+size[1])

    def collide(self,objList):
        #When this hitbox hits another in the list return type
        #self.collideList = collidelistall(objList)
        #return collideList

class HitboxList:
    def __init__(self,hitboxtype):
        self.hitboxtype = hitboxtype
        self.list = []

    def add(self,hitbox):
        self.list.append(hitbox)

    def checkList(self,hitbox):
        #returns type of collisions hitbox is in
        #how many
        hitList = []
        for hit in self.list:
            if hitbox.colliderect(hit) = True:
                hitList.append(hit)
        
        for hit in hitList:
            if hitbox.type = "shark":
                if hit.pos[0] < hitbox.pos[0]:
                    gotbit = True
                if hit.pos[0] > hitbox.pos[0]:
                    bite = True   
                
        for hit in hitList:
            if hitbox.type = "obsticle":
                hitwall = True
    
                    

                
            
            
            
    
