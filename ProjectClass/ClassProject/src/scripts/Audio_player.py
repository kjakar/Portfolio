import pygame

"""notes for later"""
##pygame.mixer.music.load()
##pygame.mixer.music.play()
##pygame.mixer.music.stop()
##pygame.mixer.music.pause()
##pygame.mixer.music.unpause()
##pygame.mixer.music.fadeout()
##pygame.mixer.music.set_volume()
##pygame.mixer.music.queue()

class singleton():
    def __init__(self,cls):
        self.cls=cls
        self.instance=0
        

    def Instance(self):
        if self.instance == 0:
            self.instance = self.cls()     
        return self.instance


@singleton
class AM:
    def __init__(self):
        self.s={} #sound dictionary
        self.m={} #music dictionary
        pygame.mixer.pre_init()

    def load_sfx(self, name, sndfile):
        self.s[name]=pygame.mixer.Sound(sndfile)
        
    def play_sfx(self,name):
        if name in self.s:
            self.s[name].play()

        

    def load_music(self,fName,track): #set-up like load_sound efffect;        
        self.m[track]=pygame.mixer.music.load(fName)



    def play_music(self,track):
##        pygame.mixer.music.load(self.m[track])
##        pygame.mixer.music.queue()# may need to put in its own def
##        self.m[track]
        pygame.mixer.music.play(2,0.0)
        """will loop the track twice starting from the beginning of the track"""


    

if __name__ == "__main__":
    pygame.init()
    screen=pygame.display.set_mode((600,400))

    
    AM.Instance().load_sfx('bite','..\\assets\\sound effects\\attack.wav')
    AM.Instance().load_sfx('spawn','..\\assets\\sound effects\\spawn.wav')


    AM.Instance().load_music("..\\assets\\music\\Cosmos (base #279).wav","cosmos")
    AM.Instance().play_music("cosmos")
    
    
    done=False
    while not done:
        pygame.event.pump()
        evntlst=pygame.event.get()
        
        for evnt in evntlst:
            if evnt.type==pygame.KEYDOWN:
                if evnt.key==pygame.K_SPACE:
                    print("space-bite")
                    AM.Instance().play_sfx("bite")
            if evnt.type==pygame.KEYDOWN:
                if evnt.key==pygame.K_z:
                    print("z-spawn")
                    AM.Instance().play_sfx("spawn")
            if evnt.type==pygame.KEYDOWN:
                if evnt.key==pygame.K_ESCAPE:
                    print("esc-quit")
                    done=True
    pygame.quit()
                    
        

        
#plcay_sound(s,2)
        
