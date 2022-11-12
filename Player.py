import pygame
from Setting import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=PlayerImage
        self.rect=self.image.get_rect(topleft=(x,y))

    def update(self):
        pass