import pygame
from Setting import *
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=CoinImages[0]
        self.rect=self.image.get_rect(topleft=(x+32,y+32))
        self.currentImgeNum=0
        self.animationSpeed=0.2
    def animate(self):
        if self.currentImgeNum<=7:
            self.currentImgeNum+=self.animationSpeed

        else:
            self.currentImgeNum=0
        self.image=CoinImages[int(self.currentImgeNum)]
    def update(self):
        self.animate()