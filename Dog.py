import pygame
from Setting import *
class Dog(pygame.sprite.Sprite):
    def __init__(self,x,y,playerGroup,levelTrue):
        super().__init__()
        self.Rimages=DogImagesRight
        self.Limages=DogImagesLeft
        self.image=self.Limages[0]
        self.rect=self.image.get_rect(topleft=(x,y))
        self.speed=1
        self.animationSpeed=0.1
        self.left=True
        self.currentImage=0
        self.playerGroup=playerGroup
        self.move0=True
        self.levelTrue = levelTrue
    def animate(self):
        if self.left:
            self.image=self.Limages[int(self.currentImage)]
        else:
            self.image = self.Rimages[int(self.currentImage)]
        self.currentImage+=self.animationSpeed
        if self.currentImage>4:
            self.currentImage=0
    def move(self):
        if self.rect.x-30> self.playerGroup.sprite.rect.x and abs(self.rect.x-30- self.playerGroup.sprite.rect.x)<500:
            self.rect.x-=self.speed
            self.move0=True
        else:
            self.move0=False
    def update(self):

        self.collition()
        self.move()
        if self.move0:
            self.animate()
    def collition(self):
        if self.rect.colliderect(self.playerGroup.sprite):
            self.levelTrue[8]=True
            self.playerGroup.sprite.fightBorderWork=True
            self.speed=0
            self.animationSpeed=0