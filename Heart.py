import pygame
from Setting import *
class Heart(pygame.sprite.Sprite):
    def __init__(self,x,y,playerGroup,health):
        super().__init__()
        self.health=health
        self.playerGroup=playerGroup
        self.heartImages=HeartImages
        self.image=HeartImages[0]
        self.rect=self.image.get_rect(topleft=(x+32,y+32))
        self.currentImgeNum=0
        self.animationSpeed=0.2
    def animate(self):
        if self.currentImgeNum<=5:
            self.currentImgeNum+=self.animationSpeed

        else:
            self.currentImgeNum=0
        self.image=self.heartImages[int(self.currentImgeNum)]
    def update(self):
        self.animate()
    def kill(self):
        self.playerGroup.sprite.health+=self.health
        if self.playerGroup.sprite.health>100:
            self.playerGroup.sprite.health=100
        super().kill()