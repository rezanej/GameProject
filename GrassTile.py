import pygame
from Setting import *
class GrassTile(pygame.sprite.Sprite):
    def __init__(self,x,y,level):
        super().__init__()
        self.image=Grassimages[level]
        self.rect=self.image.get_rect(topleft=(x,y))
