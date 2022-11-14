import pygame
from Setting import *
from Kunai import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,tileGroup,kunaiGroup):
        super().__init__()
        self.image=PlayerImage
        self.rect=self.image.get_rect(topleft=(x,y))
        self.direction=pygame.math.Vector2()
        self.tileGroup=tileGroup
        self.kunaiGroup=kunaiGroup
        print(self.direction)
        self.jumpSpeed=PlayerJumpSpeed
        self.speed=PlayerSpeed
        self.gravity=Gravity
        self.state="idle"
        self.currentimageNum=0
        self.left=False
        self.onGround=False
    def setDirection(self):

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x=-1
            self.state="run"
        elif keys[pygame.K_RIGHT]:
            self.direction.x=1
            self.state="run"

        else:
            self.direction.x=0
            self.state="idle"

        if keys[pygame.K_SPACE] and self.onGround:
            self.jump()
            self.state="jump"
        if keys[pygame.K_f]:
            self.kunaiGroup.add(Kunai(self.rect.centerx,self.rect.centery,self))
    def update(self):
        self.setDirection()
        self.onGround=False
        self.horizontalMovement()
        self.horizontalCollision()
        self.gravityFun()
        self.verticalCollision()
        self.checkJump()
        self.animate()
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
                    self.onGround=True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

    def jump(self):
        self.direction.y=-self.jumpSpeed
    def gravityFun(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y
    def checkJump(self):
        if self.direction.y>0:
            self.onGround=False
        if self.direction.y <0:
            self.state="jump"
    def verticalMovement(self):
        self.direction.y+=4
        self.rect.y+=self.direction.y
    def animate(self):
        if self.state=="idle":
            if not self.left:
                self.image=PlayerIdleImages[self.currentimageNum]
            elif self.left:
                self.image = PlayerIdleImagesLeft[self.currentimageNum]
            self.currentimageNum += 1
            if self.currentimageNum==10:
                self.currentimageNum=0
        if self.state=="run":
            if self.direction.x > 0:
                self.left=False
                self.image=PlayerRunImages[self.currentimageNum]
            if self.direction.x < 0:
                self.left = True
                self.image=PlayerRunImagesLeft[self.currentimageNum]
            self.currentimageNum += 1
            if self.currentimageNum==10:
                self.currentimageNum=0
        if self.state=="jump":
            if not self.left:
                self.image=PlayerJumpImages[self.currentimageNum]
                self.currentimageNum+=1
            else:
                self.image=PlayerJumpImagesLeft[self.currentimageNum]
                self.currentimageNum += 1
            if self.currentimageNum==10:
                self.currentimageNum=0
