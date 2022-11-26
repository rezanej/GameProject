import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self,images,x,y,playerGroup):
        super().__init__()
        self.playerGroup=playerGroup
        self.images=images
        self.image=self.images[0]
        self.rect=self.image.get_rect(midleft=(x,y))
        self.animationSpeed=0.5
        self.imageNum=0
        self.timer=20
        self.once=True
    def animate(self):
        if self.imageNum>=63:
            self.imageNum=0
        else:
            self.imageNum+=self.animationSpeed
            self.image=self.images[int(self.imageNum)]

    def update(self):
        self.animate()
        self.colide()
    def colide(self):
        if pygame.sprite.spritecollide(self,self.playerGroup,False):
            self.timer-=1
        if self.timer<0 and self.once:
            print("Done")
            self.once=False
