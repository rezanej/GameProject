import pygame
from Setting import *
class GrassTile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=grassimages[CurrentLevel-1]
        self.rect=self.image.get_rect(topleft=(x,y))
