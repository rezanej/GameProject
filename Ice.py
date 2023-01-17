import pygame
from Setting import *
class Ice(pygame.sprite.Sprite):
    def __init__(self,x,y,iceImages,enemy):
        super().__init__()
        self.coinImages=iceImages
        self.image=iceImages[0]
        self.rect=self.image.get_rect(bottomleft=(x+10,y+80))
        self.currentImgeNum=0
        self.animationSpeed=0.1
        self.time=200
        self.enemy=enemy
    def animate(self):
        if self.currentImgeNum<=3:
            self.currentImgeNum+=self.animationSpeed

        self.image=self.coinImages[int(self.currentImgeNum)]
    def update(self):
        self.animate()
        self.time-=1
        if self.time==0:
            self.kill()
            self.enemy.freeze=False
            self.enemy.freezeOnce=False
