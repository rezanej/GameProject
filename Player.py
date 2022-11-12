import pygame
from Setting import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=PlayerImage
        self.rect=self.image.get_rect()

    def update(self):
        pass