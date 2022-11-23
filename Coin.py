import pygame
from Setting import *
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y,playerGroup,score,coinImages):
        super().__init__()
        self.score=score
        self.playerGroup=playerGroup
        self.coinImages=coinImages
        self.image=coinImages[0]
        self.rect=self.image.get_rect(topleft=(x+32,y+32))
        self.currentImgeNum=0
        self.animationSpeed=0.2
    def animate(self):
        if self.currentImgeNum<=7:
            self.currentImgeNum+=self.animationSpeed

        else:
            self.currentImgeNum=0
        self.image=self.coinImages[int(self.currentImgeNum)]
    def update(self):
        self.animate()
    def kill(self,addScore=1):
        self.playerGroup.sprite.score+=self.score*addScore #for not adding score when loading save
        super().kill()