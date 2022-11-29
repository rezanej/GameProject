import pygame
from Setting import *

class FireBall(pygame.sprite.Sprite):
    def __init__(self,x,y,player,enemies,speed):
        super().__init__()
        self.lifeTime=KunaiLifetime
        if player.left:
            self.direction=-1
            self.images = FireBallImagesLeft
        else:
            self.direction=1
            self.images=FireBallImagesRight
        self.rect = self.images[0].get_rect(center=(x, y))
        self.player=player
        self.speed=speed
        self.enemies=enemies
        self.lifeTime = 600
        self.currentImgNum=0
        self.animSpeed=0.5
    def update(self):
        self.animate()
        self.move()
        self.life()
        self.collition()
    def move(self):
        if self.direction>0:
            self.rect.x+=self.speed
        elif self.direction<0:
            self.rect.x-=self.speed
    def life(self):
        self.lifeTime -= 1
        if self.lifeTime < 0:
            self.kill()
    def collition(self):
        for sprite in self.enemies:
            if self.rect.colliderect(sprite):
                sprite.health-=10
                if sprite.health<=0:
                    sprite.dead=True
                self.kill()
    def animate(self):
        self.image=self.images[int(self.currentImgNum)]
        self.currentImgNum+=self.animSpeed
        if self.currentImgNum>3:
            self.currentImgNum=0



