import pygame
from Setting import *

class FireBall(pygame.sprite.Sprite):
    def __init__(self,x,y,player,enemies,speed,imagesLeft,imagesRight,mode=0):
        super().__init__()
        self.lifeTime=KunaiLifetime
        if player.left:
            self.direction=-1
            self.images = imagesLeft
        else:
            self.direction=1
            self.images=imagesRight
        self.rect = self.images[0].get_rect(center=(x, y))
        self.player=player
        self.speed=speed
        self.enemies=enemies
        self.lifeTime = 600
        self.currentImgNum=0
        self.animSpeed=0.5
        self.mode=mode
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
                sprite.health-=15
                if self.mode==1:
                    sprite.health -= 15  # doing it twice
                if sprite.health<=0:
                    sprite.dead=True
                self.kill()
    def animate(self):
        self.image=self.images[int(self.currentImgNum)]
        self.currentImgNum+=self.animSpeed
        if self.currentImgNum>=len(self.images):
            self.currentImgNum=0

        if self.mode==1:
           self.changeColor(0)

    def changeColor(self,hue):
        self.tempImage = self.image.copy()
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        color = pygame.Color(0)
        color.hsla = (hue, 100, 60, 100)
        colorImage.fill(color)
        self.tempImage.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.image = self.tempImage


