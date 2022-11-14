import pygame
from Setting import *

class Kunai(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        super().__init__()
        if player.left:
            self.direction=-1
            self.image = KunaiImgaeLeft

        else:
            self.direction=1
            self.image=KunaiImgae
        self.rect = self.image.get_rect(center=(x, y))
        self.player=player
        self.speed=KunaiSpeed

    def update(self):
        if self.direction>0:
            self.rect.x+=KunaiSpeed
        elif self.direction<0:
            self.rect.x-=KunaiSpeed