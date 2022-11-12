import pygame
from Setting import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=PlayerImage
        self.rect=self.image.get_rect(topleft=(x,y))

        self.direction=pygame.math.Vector2()
        print(self.direction)

        self.speed=PlayerSpeed
    def setDirection(self):

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x=-1
            print(self.direction.x)
        elif keys[pygame.K_RIGHT]:
            self.direction.x=1
            print(self.direction.x)
        else:
            self.direction.x=0

    def update(self):
        self.setDirection()
        self.rect.x+= self.direction.x * self.speed
