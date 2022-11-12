import pygame
from Setting import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,tileGroup):
        super().__init__()
        self.image=PlayerImage
        self.rect=self.image.get_rect(topleft=(x,y))

        self.direction=pygame.math.Vector2()
        self.tileGroup=tileGroup
        print(self.direction)
        self.jumpSpeed=PlayerJumpSpeed
        self.speed=PlayerSpeed
        self.gravity=Gravity
    def setDirection(self):

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x=-1

        elif keys[pygame.K_RIGHT]:
            self.direction.x=1
        else:
            self.direction.x=0
        if keys[pygame.K_SPACE]:
            self.jump()

    def update(self):
        self.setDirection()
        self.horizontalMovement()
        self.horizontalCollision()
        self.gravityFun()
        self.verticalCollision()
    def horizontalMovement(self):
        self.rect.x += self.direction.x * self.speed

    def horizontalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x>0:
                    self.rect.right=sprite.rect.left
                if self.direction.x<0:
                    self.rect.left=sprite.rect.right

    def verticalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
    def jump(self):
        self.direction.y=-self.jumpSpeed
    def gravityFun(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y

    def verticalMovement(self):
        self.direction.y+=4
        self.rect.y+=self.direction.y