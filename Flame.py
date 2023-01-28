import pygame
import random
class Particle():
    color=2
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.radius=4
        self.originalR=4

        self.alphaLayers=2
        self.alphaGlow=2
        surfaceMaxSize=2*self.radius*self.alphaLayers*self.alphaLayers*self.alphaGlow
        self.Surface=pygame.Surface((surfaceMaxSize,surfaceMaxSize),pygame.SRCALPHA)
        self.burnRate=0.1*random.randint(1,4) # having diffrent burn rate for making it smooth

    def update(self):
        self.y-=self.radius
        self.x+=random.randint(-self.radius,self.radius)
        self.originalR-=self.burnRate
        self.radius=int(self.originalR)
        if self.radius<=0:
            self.radius =1

    def draw(self,display):
        surfaceMaxSize=2*self.radius*self.alphaLayers*self.alphaLayers*self.alphaGlow
        self.Surface=pygame.Surface((surfaceMaxSize,surfaceMaxSize),pygame.SRCALPHA)

        for i in range(self.alphaLayers,-1,-1):
            alpha=255-i*(255//self.alphaLayers-5)
            if alpha<=0:
                alpha=0
            radius=self.radius*i*i*self.alphaGlow
            if Particle.color==2:
                if self.radius==4 or self.radius==3:
                    color=(255, 0, 0,alpha)
                elif self.radius==2:
                    color=(255, 155,0,alpha)
                else:
                    color=(50, 50, 50,alpha)

            elif Particle.color==3:
                if self.radius==4 or self.radius==3:
                    color=(0,0,255,alpha)
                elif self.radius==2:

                    color=(0,155,255,alpha)
                else:
                    color=(50,50,50,alpha)
            pygame.draw.circle(self.Surface,color,(self.Surface.get_width()//2,self.Surface.get_height()//2),radius)
        display.blit(self.Surface, self.Surface.get_rect(center=(self.x, self.y)))
class Flame():
    def __init__(self,x,y):
        super().__init__()
        self.x,self.y=x,y
        self.speed=0
        self.particleGroup=[]

        for i in range(2*25):
            self.particleGroup.append(Particle(self.x+random.randint(-2,2),self.y+random.randint(-2,2)))

    def draw(self,display,mode):
            Particle.color=mode
            self.speed += 1
            for particle in self.particleGroup:
                if particle.originalR<=0:
                    self.particleGroup.append(Particle(self.x+random.randint(-2,2),self.y+random.randint(-2,2)))
                    self.particleGroup.remove(particle)

                particle.update()
                particle.draw(display)
